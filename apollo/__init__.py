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

from apollo.database.supabase.base import AbstractSupabaseClient
from apollo.database.firebase.base import AbstractFirebaseClient
from apollo.service.json.base import AbstractRestClient
from .const import SUPABASE_CLIENT_CLASS, FIREBASE_CLIENT_CLASS, REST_CLIENT_CLASS

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
