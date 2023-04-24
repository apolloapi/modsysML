from clients import get_psql_client
from clients.exceptions import ExecutionError

import itertools
import logging


logger = logging.getLogger(__name__)

# SQL Queries
QUERY_CONTEXT = {
    "asc": "",
    "desc": "",
    "all_tables": "select table_name from information_schema.tables where table_schema='public'",
}


class PostgresConnectionManager:
    @staticmethod
    def connect_to_prefix(uri):
        return get_psql_client(uri)

    @staticmethod
    def convert_dict(items):
        if not items:
            logger.warning("Empty query results detected, %s", items)
            return

        vector = []

        for i in items:
            vector.append(dict(i))

        return vector


class QueryManager(PostgresConnectionManager):

    # hard code sql queries to prevent injection
    # set context for query with a batch of 10 items.
    def set_context(self, query_type, table, col):

        # oldest order
        if query_type == "asc":
            QUERY_CONTEXT[
                query_type
            ] = f"SELECT * FROM {table} ORDER BY {col} ASC LIMIT 100;"

        # newest
        if query_type == "desc":
            QUERY_CONTEXT[
                query_type
            ] = f"SELECT * FROM {table} ORDER BY {col} DESC LIMIT 100;"

        return QUERY_CONTEXT[query_type]

    # fetch all available tables
    def fetch_tables(self, uri):
        curs = self.connect_to_prefix(uri)
        try:
            response = curs.execute(QUERY_CONTEXT["all_tables"])
        except Exception as err:
            logger.warning("Error executing query")
            raise ExecutionError(err)

        return list(itertools.chain.from_iterable(response))

    # execute a sql query
    def query(self, uri, query_type, table, col):
        curs = self.connect_to_prefix(uri)
        query_string = self.set_context(query_type, table, col)

        try:
            response = curs.execute(query_string)
        except Exception as err:
            logger.warning("Error executing query")
            raise ExecutionError(err)

        return self.convert_dict(response)
