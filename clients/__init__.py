from clients.postgresql.base import AbstractPostgresClient

from .settings import POSTGRES_CLIENT_CLASS
from django.utils.module_loading import import_string


def get_psql_client(connection_string) -> AbstractPostgresClient:
    client = import_string(POSTGRES_CLIENT_CLASS)
    return client(connection_string)
