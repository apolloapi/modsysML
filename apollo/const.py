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

from dotenv import load_dotenv

import os

load_dotenv()


# Supabase support
SUPABASE_CLIENT_CLASS = os.environ.get(
    "SUPABASE_CLIENT_CLASS", "apollo.database.supabase.SupabaseClient"
)

# Firebase support
FIREBASE_CLIENT_CLASS = os.environ.get(
    "FIREBASE_CLIENT_CLASS", "apollo.database.firebase.FirebaseClient"
)

# Service client
REST_CLIENT_CLASS = os.environ.get(
    "REST_CLIENT_CLASS", "apollo.service.json.RestClient"
)

# Hard code sql queries to prevent injection
QUERY_CONTEXT = {
    "asc": "",
    "desc": "",
    "all_tables": "select table_name from information_schema.tables where table_schema='public'",
}

# Test account for firebase
TEST_ACCOUNT = os.environ.get("test_account", None)

# Service SDK test token, THIS IS PUBLIC
test_token = os.environ.get("test_token", None)
