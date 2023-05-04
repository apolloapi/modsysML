# Copyright 2022 Adrian Brown
# Copyright 2023 Apollo API, Inc.
#
#    Licensed under the Elastic License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         https://www.elastic.co/licensing/elastic-license
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import requests

from apollo.service.json.base import AbstractRestClient
from apollo.const import test_token


class RestClient(AbstractRestClient):
    def __init__(self, api_key):
        self.api_key = api_key

    @staticmethod
    def make_http_request():
        return None

    def make_https_request(self, body):
        response = requests.post(
            "https://api.apolloapi.io/api/v1/apollo/",
            headers={"Authorization": f"Token {self.api_key}"},
            json=body,
            timeout=10,
        )
        return response.json()
