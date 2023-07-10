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

import requests

from modsys.service.json.base import AbstractRestClient
from modsys.const import test_token


class RestClient(AbstractRestClient):
    def __init__(self, api_key):
        self.api_key = api_key

    @staticmethod
    def call_api(self):
        return None

    # TODO: change this to http and update this to be sending us content ( can rename and shrink to two functions)
    def make_https_request(self, body):
        response = requests.post(
            "https://api.apolloapi.io/api/v1/sandbox/",  # Access to sandbox env
            # headers={"Authorization": f"Token {self.api_key}"},
            json=body,
            timeout=10,
        )
        return response.json()
