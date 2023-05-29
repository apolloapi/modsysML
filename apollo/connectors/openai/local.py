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

from apollo.connectors.openai.base import AbstractOpenAIProvider


class FakeAbstractOpenAIProvider(AbstractOpenAIProvider):
    def id(self) -> str:
        pass

    def to_string(self) -> str:
        pass

    def token_settings(self) -> str:
        pass

    def temp_settings(self) -> str:
        pass
