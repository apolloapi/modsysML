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

from apollo.manager import (
    PostgresConnectionManager,
    FirebaseConnectionManager,
    JSONConnectionManager,
    OpenAIConnectionManager,
    GoogleAIConnectionManager,
)
from apollo.const import QUERY_CONTEXT


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


class General(Postgres, JSONService, OpenAI, GoogleAI):

    # Current LLM to be used
    model = None
