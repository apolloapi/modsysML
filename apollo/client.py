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

from apollo.resource import General
from apollo.exceptions import ExecutionError, EmptyResultsWarning

import itertools


class Apollo(General):
    @classmethod
    def set_context(cls, query_type, table, col):
        # oldest order
        if query_type == "asc":
            cls._context[
                query_type
            ] = f"SELECT * FROM {table} ORDER BY {col} ASC LIMIT 100;"

        # newest
        if query_type == "desc":
            cls._context[
                query_type
            ] = f"SELECT * FROM {table} ORDER BY {col} DESC LIMIT 100;"

        return cls._context[query_type]

    # fetch all available tables
    @classmethod
    def fetch_tables(cls):
        """
        Fetch all the tables for your external resource using Apollo

        Args:
        None

        Returns:
        list: All the available tables for your resource

        Next steps:
        [Success]: Run a query with query
        """
        try:
            response = cls.psql_curs.execute(cls._context["all_tables"])
        except Exception as err:
            raise ExecutionError(err)

        return list(itertools.chain.from_iterable(response))

    # # execute a sql query
    @classmethod
    def query(cls, query_type, table, col):
        """
        Query your external resource using Apollo

        Args:
        query_type (str): The sort order for your query
        table (str): The table to query
        col (str): The column to sort by

        Returns:
        dict: result of query
        """
        query_string = cls.set_context(query_type, table, col)

        try:
            response = cls.psql_curs.execute(query_string)
        except Exception as err:
            raise ExecutionError(err)

        return cls._manager.convert_dict(response)

    @classmethod
    def connect(cls, db_url, *args, **kwargs):
        """
        Sync data with Apollo to begin building decision trees

        Args:
        db_url (str): The database URL to connect to

        Returns:
        str: A message indicating that the connection was successful

        Next steps:
        [Success]: Syncing data to Apollo, next steps below;
            1. Apollo.fetch_tables()
            2. Apollo.query([desc/asc], [table], [column])
        """
        cls.psql_curs = cls._manager.connect_to_prefix(db_url)
        return "Syncing data with Apollo"

    @classmethod
    def use(cls, provider, token=None, *args, **kwargs):
        if provider.lower() == "apollo":
            cls.model = "Apollo"
            if token:
                cls._auth_token = token
                print(f"Connected to {provider} provider, using Safety model")
            else:
                print("Please set a auth token")
        else:
            return f"Provider {provider} not found"

    @classmethod
    def detectText(cls, text, operator, threshold):
        if cls.model:
            # print(cls.model)
            conn = cls._service_manager.connect(cls._auth_token)
            return conn.make_https_request({"rule": f"{text} {operator} {threshold}"})
        else:
            return "No provider connected"
