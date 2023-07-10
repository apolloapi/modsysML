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

from modsys import (
    get_supabase_client,
    get_firebase_client,
    get_json_client,
    get_openai_client,
    get_google_client,
    get_sightengine_client,
)
from modsys.exceptions import EmptyResultsWarning


class PostgresConnectionManager:
    @staticmethod
    def connect_to_prefix(uri):
        return get_supabase_client(uri)

    @staticmethod
    def convert_dict(items):
        if not items:
            raise EmptyResultsWarning(items)

        vector = []

        for i in items:
            vector.append(dict(i))

        return vector


class FirebaseConnectionManager:
    @staticmethod
    def connect_to_prefix(service_account_key):
        return get_firebase_client(service_account_key)


class JSONConnectionManager:
    @staticmethod
    def connect(api_key):
        return get_json_client(api_key)


class OpenAIConnectionManager:
    @staticmethod
    def load_openai_provider(provider_path: str):
        return get_openai_client(provider_path)


class GoogleAIConnectionManager:
    @staticmethod
    def load_google_provider(provider_path: str, *args, **kwargs):
        return get_google_client(
            provider_path, secret=kwargs["secret"] if "secret" in kwargs else None
        )


class SightengineConnectionManager:
    @staticmethod
    def load_sightengine_provider(provider_path, secret, api_user):
        return get_sightengine_client(provider_path, secret=secret, api_user=api_user)
