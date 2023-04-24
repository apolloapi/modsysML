from clients.postgresql.base import AbstractPostgresClient


class FakePostgresClient(AbstractPostgresClient):
    def execute(self, sql):
        return sql
