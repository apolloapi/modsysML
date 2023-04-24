import logging

import psycopg as pgi_connector
import psycopg2
import psycopg2.extras

from clients.postgresql.base import AbstractPostgresClient
from clients.exceptions import PostgresConnectionError

logger = logging.getLogger(__name__)


class PostgresClient(AbstractPostgresClient):
    def __init__(self, connection_string: str):
        self.secret = connection_string

    def execute(self, sql):
        if not self.secret:
            logger.warning("Please specify a connection string in uri format")
            return

        try:
            conn_dict = pgi_connector.conninfo.conninfo_to_dict(self.secret)
            con = psycopg2.connect(**conn_dict)
        except Exception as err:
            logger.error("Error connecting to remote environment using connection info")
            raise PostgresConnectionError(err)

        response = None
        with con:

            cursor = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
            cursor.execute(str(sql))

            response = cursor.fetchall()

        return response
