# Copyright 2023 Apollo API, Inc.
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

from apollo.connectors.google.base import AbstractGooglePerspectiveProvider
from apollo.exceptions import AuthorizationFailure


class GooglePerspectiveProvider(AbstractGooglePerspectiveProvider):
    api_key_val = os.environ.get("PERSPECTIVE_API_KEY", None)
    i18n = os.environ.get("PERSPECTIVE_i18n", ["en"])
    cache = os.environ.get("PERSPECTIVE_CACHE_OUTPUT", True)

    def __init__(self, model_name: str, secret=None) -> None:
        self.model_name = model_name  # analyze or suggest

        if self.api_key_val is None and self.secret is None:
            raise AuthorizationFailure
        elif self.secret is None and self.api_key_val is not None:
            self.api_key = self.api_key_val
        else:
            self.api_key = secret

        self.lang = list(self.i18n)
        self.cache = bool(self.cache)

    def id(self) -> str:
        return f"google_perspective:{self.model_name}"

    def to_string(self) -> str:
        return f"[Google Perspective Provider {self.model_name}]"

    def i18n(self) -> str:
        return f"Language set to {self.i18n}"

    def cache_settings(self) -> str:
        return f"Persist model output set to {self.cache}"

    def call_api(self, prompt: str, content_id: str, community_id: str):
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
            "languages": self.lang,
            "doNotStore": self.cache,
            "clientToken": content_id,
            "communityId": community_id,
        }

        headers = {
            "Content-Type": "application/json",
        }
        response = requests.post(
            f"https://commentanalyzer.googleapis.com/v1alpha1/comments:{self.model_name}?key={self.api_key}",
            headers=headers,
            data=body,
        )
        if response.json():
            data = response.json()
            return {
                "output": data["attributeScores"],
                "metadata": {data["clientToken"], data["languages"]},
            }
        else:
            raise Exception(
                f"Google Perspective API call failed with status code {response.json()}"
            )
