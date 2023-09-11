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

from modsys.connectors.scam_advisor.base import AbstractScamAdvisorProvider
from modsys.exceptions import AuthorizationFailure

import os
import requests


class ScamAdvisorProvider(AbstractScamAdvisorProvider):
    api_key_val = os.environ.get("SCAMADVISOR_API_KEY", None)

    def __init__(self, api_key=None):
        self.base_url = "https://api.scamadviser.cloud/v2/trust/single"
        self.refresh = True
        self.api_key = api_key

        if self.api_key_val is None and self.api_key is None:
            raise AuthorizationFailure
        elif self.api_key_val is None and self.api_key is not None:
            self.api_key = api_key
        else:
            self.api_key = self.api_user_val

    def set_preferrences(self, boolean):
        self.refresh = boolean
        return f"set refresh to {boolean}, if true performing new scan."

    def call_api(self, domain):
        response = requests.get(
            f"{self.base_url}?apikey={self.api_key}&domain={domain}&refresh={self.refresh}"
        )
        if response.status_code == 200:
            return response
        else:
            raise Exception(
                f"Sightengine API call failed with status code {response.status_code}"
            )
