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

from .base import AbstractSightengineProvider
from modsys.exceptions import AuthorizationFailure

import os
import requests
import json


class SightengineProvider(AbstractSightengineProvider):
    api_key_val = os.environ.get("SIGHTENGINE_API_KEY", None)
    api_user_val = os.environ.get("SIGHTENGINE_API_USER", None)

    def __init__(self, model_name: list, secret=None, api_user=None) -> None:
        """
        :arg: secret: can either feed in a secret key and api_user
        or it'll default to using the one set as an ENV variable.
        """
        self.model_name = model_name  # list of models from sightengine
        self.secret = secret
        self.api_user = api_user

        if self.api_key_val is None and self.secret is None:
            raise AuthorizationFailure
        elif self.api_user_val is None and self.api_user is None:
            raise AuthorizationFailure
        elif self.api_user is None and self.api_user_val is not None:
            self.api_user = self.api_user_val
        elif self.secret is None and self.api_key_val is not None:
            self.secret = self.api_key_val

        # public or direct upload methods, default to public
        self.method = "public"

    def id(self) -> str:
        return f"sightengine:{self.model_name}"

    def to_string(self) -> str:
        return f"[Sightengine Provider {self.model_name}]"

    def settings(self) -> str:
        return f"Sightengine model output set to {self.method} upload"

    def call_api(self, url):
        """
        default public upload method, if direct upload needed, extend this.
        """

        body = {
            "url": url,
            "models": ",".join(self.model_name),
            "api_user": f"{self.api_user}",
            "api_secret": f"{self.secret}",
        }

        response = requests.get(
            "https://api.sightengine.com/1.0/check.json",
            params=body,
        )
        if response.status_code == 200:
            data = json.loads(response.text)
            return data
        else:
            raise Exception(
                f"Sightengine API call failed with status code {response.status_code}"
            )
