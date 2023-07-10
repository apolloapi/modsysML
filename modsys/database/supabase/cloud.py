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

import psycopg as pgi_connector
import psycopg2
import psycopg2.extras

from modsys.database.supabase.base import AbstractSupabaseClient
from modsys.exceptions import PostgresConnectionError, PostgresExecutionError


class SupabaseClient(AbstractSupabaseClient):
    def __init__(self, connection_string: str):
        self.secret = connection_string

    def execute(self, sql):
        if not self.secret:
            raise PostgresExecutionError("empty secret")

        try:
            conn_dict = pgi_connector.conninfo.conninfo_to_dict(self.secret)
            con = psycopg2.connect(**conn_dict)
        except Exception as err:
            raise PostgresConnectionError(err)

        response = None
        with con:

            cursor = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
            cursor.execute(str(sql))

            response = cursor.fetchall()

        return response
