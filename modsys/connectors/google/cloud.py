# Copyright: (c) 2022, Adrian Brown <adrbrownx@gmail.com>
# Copyright: (c) 2023, ModsysML Project
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from modsys.connectors.google.base import AbstractGooglePerspectiveProvider
from modsys.exceptions import AuthorizationFailure

import os
import requests


class GooglePerspectiveProvider(AbstractGooglePerspectiveProvider):
    api_key_val = os.environ.get("PERSPECTIVE_API_KEY", None)
    cache = os.environ.get("PERSPECTIVE_CACHE_OUTPUT", True)

    def __init__(self, model_name: str, secret=None) -> None:
        self.model_name = model_name  # analyze or suggest
        self.secret = secret
        if self.api_key_val is None and self.secret is None:
            raise AuthorizationFailure
        elif self.secret is None and self.api_key_val is not None:
            self.api_key = self.api_key_val
        else:
            self.api_key = self.secret

        self.cache = bool(self.cache)

    def id(self) -> str:
        return f"google_perspective:{self.model_name}"

    def to_string(self) -> str:
        return f"[Google Perspective Provider {self.model_name}]"

    def cache_settings(self) -> str:
        return f"Persist model output set to {self.cache}"

    def get_attribute_scores(self, category, score):
        return {category: {"summaryScore": {"value": score}}}

    def transform(
        self,
        prompt: str,
        content_id: str,
        community_id: str,
        score: float,
        category: str,
    ):
        if self.model_name == "analyze":
            body = {
                "comment": {
                    "text": prompt,
                },
                "requestedAttributes": {
                    "TOXICITY": {},
                    "SEVERE_TOXICITY": {},
                    "INSULT": {},
                    "THREAT": {},
                    "SEXUALLY_EXPLICIT": {},
                    "SPAM": {},
                },
                "doNotStore": self.cache,
                "clientToken": content_id,
                "communityId": community_id,
            }
            url = f"https://commentanalyzer.googleapis.com/v1alpha1/comments:{self.model_name}?key={self.api_key}"
            return {"url": url, "body": body}
        elif self.model_name == "suggest":
            if score is None:
                raise Exception(
                    "'score' must be provided when the model name is 'suggest'"
                )

            body = {
                "comment": {
                    "text": prompt,
                },
                "attributeScores": self.get_attribute_scores(category, score),
                "clientToken": content_id,
                "communityId": community_id,
            }

            url = f"https://commentanalyzer.googleapis.com/v1alpha1/comments:suggestscore?key={self.api_key}"
            return {"url": url, "body": body}
        else:
            raise Exception(
                f"Invailid model_name. Expected 'suggest' or 'analyze' but got {self.model_name}"
            )

    def call_api(
        self,
        prompt: str,
        content_id: str,
        community_id: str,
        score: float,
        category: str,
    ):
        transformed_data = self.transform(
            prompt, content_id, community_id, score, category
        )
        url = transformed_data["url"]
        body = transformed_data["body"]

        headers = {
            "Content-Type": "application/json",
        }
        response = requests.post(
            url=url,
            headers=headers,
            json=body,
        )
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print(response.json())
            raise Exception(
                f"Google Perspective API call failed with status code {response.status_code}"
            )
