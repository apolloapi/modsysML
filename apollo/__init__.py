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

import importlib

from apollo.database.supabase.base import AbstractSupabaseClient
from apollo.database.firebase.base import AbstractFirebaseClient
from apollo.service.json.base import AbstractRestClient
from apollo.connectors.openai.base import AbstractOpenAIProvider

from .const import (
    SUPABASE_CLIENT_CLASS,
    FIREBASE_CLIENT_CLASS,
    REST_CLIENT_CLASS,
    OPENAI_CLIENT_CLASS,
)

from django.utils.module_loading import import_string


def get_supabase_client(connection_string) -> AbstractSupabaseClient:
    client = import_string(SUPABASE_CLIENT_CLASS)
    return client(connection_string)


def get_firebase_client(service_account_key) -> AbstractFirebaseClient:
    client = import_string(FIREBASE_CLIENT_CLASS)
    return client(service_account_key)


def get_json_client(api_key) -> AbstractRestClient:
    client = import_string(REST_CLIENT_CLASS)
    return client(api_key)


def get_openai_client(provider_path: str) -> AbstractOpenAIProvider:
    client = import_string(OPENAI_CLIENT_CLASS)
    if provider_path.startswith("openai:"):
        path_parts = provider_path.split(":")
        model_name = path_parts[0]
        model_type = path_parts[1]
        if model_type == "chat":
            print(f"Connected to {provider_path}")
            return client("gpt-3.5-turbo")
        elif model_type == "completion":
            print(f"Connected to {provider_path}")
            return client("text-davinci-003")
        else:
            raise ValueError(f"Unknown OpenAI model type: {model_type}")
    else:
        return importlib.import_module(provider_path).default()
