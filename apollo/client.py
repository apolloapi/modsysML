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

from apollo.resource import General
from apollo.exceptions import ExecutionError, EmptyResultsWarning

# from evaluator import evaluate as do_evaluate
# from providers import load_api_provider

# from typing import List, Optional, Union

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

    # execute a sql query
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
    def use(cls, provider, token="Beta_token123", *args, **kwargs):
        provider = provider.lower()
        # TODO: Move apollo connection to its own
        # method like openai once integrated
        if provider == "apollo":
            cls.model = "Apollo"
            if token:
                cls._auth_token = token
                print(f"Connected to {provider} provider, using Safety model")
            else:
                print(
                    "Please set a auth token or use the sandbox: Apollo.sandbox_test()"
                )
        elif provider.startswith(
            "openai:"
        ):  # NOTE update the return method to detectText
            cls.model = "OpenAI"
            cls._provider_path = provider
            return cls._openai_manager.load_openai_provider(cls._provider_path)
        elif provider.startswith("google_perspective:"):
            cls.model = "Google"
            cls._google_perspective_provider_path = provider
            cls._google_perspective_auth_token = (
                kwargs["google_perspective_api_key"]
                if "google_perspective_api_key" in kwargs
                else None
            )
        elif provider.startswith("sightengine:"):
            cls.model = "Sightengine"
            cls._sightengine_provider_path = (
                provider  # provider = "sightengine:[<model/s>]"
            )
            cls._sightengine_auth_token = (
                kwargs["sightengine_api_key"]
                if "sightengine_api_key" in kwargs
                else None
            )
            cls._sightengine_api_user = (
                kwargs["sightengine_api_user"]
                if "sightengine_api_user" in kwargs
                else None
            )
        else:
            return f"Provider {provider} not found"

    @classmethod
    def detectText(cls, *args, **kwargs):
        """
        Detects text using the appropriate provider based on the `model` attribute of the class.

        :param text: The text to be detected (optional).
        :type text: str
        :param operator: The operator to be used (optional).
        :type operator: str
        :param threshold: The threshold value to be used (optional).
        :type threshold: float

        :return: The result of the text detection operation.
        :rtype: str

        """
        text = kwargs.get("text")
        operator = kwargs.get("operator")
        threshold = kwargs.get("threshold")
        if cls.model == "Apollo":  # TODO: changes with sandbox update
            # print(cls.model)
            conn = cls._service_manager.connect(cls._auth_token)
            return conn.make_https_request({"rule": f"{text} {operator} {threshold}"})
        elif cls.model == "Google":
            conn = cls._googleai_manager.load_google_provider(
                cls._google_perspective_provider_path,
                cls._google_perspective_auth_token,
            )
            return conn.call_api(
                kwargs["prompt"] if "prompt" in kwargs else None,
                kwargs["content_id"] if "content_id" in kwargs else None,
                kwargs["community_id"] if "community_id" in kwargs else None,
            )
        else:
            return "No provider connected"

    @classmethod
    def detectImage(cls, url, *args, **kwargs):
        if cls.model == "Sightengine":
            conn = cls._sightengine_manager.load_sightengine_provider(
                cls._sightengine_provider_path,
                cls._sightengine_auth_token,
                cls._sightengine_api_user,
            )
            return conn.call_api(url)
        else:
            raise NotImplementedError

    @classmethod
    def evaluate(providers, options):
        """Evaluates prompts using the specified providers.

        Args:
            providers: The providers to use. Can be a string, a list of strings, or a list of `ApiProvider` objects.
            options: Optional keyword arguments to pass to the `evaluate` function.
        TODO:
        """

        # if not options:
        #     options = {}

        # api_providers = []

        # if isinstance(providers, str):
        #     api_providers.append(load_api_provider(providers))
        # elif isinstance(providers, list):
        #     for provider in providers:
        #         if isinstance(provider, str):
        #             api_providers.append(load_api_provider(provider))
        #         else:
        #             api_providers.append(provider)
        # else:
        #     raise ValueError(f"providers must be a string, a list of strings, or a list of ApiProvider objects, but got {providers!r}")

        # return do_evaluate(options, api_providers)
