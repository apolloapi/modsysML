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

from modsys.manager import (
    PostgresConnectionManager,
    FirebaseConnectionManager,
    JSONConnectionManager,
    OpenAIConnectionManager,
    GoogleAIConnectionManager,
    SightengineConnectionManager,
    ProviderConnectionManager,
)
from modsys.const import QUERY_CONTEXT


class Postgres:

    # Specific sql queries
    _context = QUERY_CONTEXT

    # Database utility class
    _manager = PostgresConnectionManager()

    # curosr instance
    psql_curs = None


class Firebase:
    pass


class JSONService:

    # Service utility class
    _service_manager = JSONConnectionManager()

    # Token
    _auth_token = None


class OpenAI:

    # connection manager
    _openai_manager = OpenAIConnectionManager()

    # model type definition
    _provider_path = None


class GoogleAI:
    # connection manager
    _googleai_manager = GoogleAIConnectionManager()

    # model type definition
    _google_perspective_provider_path = None

    # API key
    _google_perspective_auth_token = None


class SightengineAI:
    _sightengine_manager = SightengineConnectionManager()
    _sightengine_provider_path = None
    _sightengine_auth_token = None
    _sightengine_api_user = None


class General(Postgres, JSONService, OpenAI, GoogleAI, SightengineAI):

    # Current LLM to be used
    model = None

    # Class instance connection manager to AI providers
    _api_manager = ProviderConnectionManager()
