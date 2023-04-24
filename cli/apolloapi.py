from clients.controller import QueryManager


class HeadlessSDK(QueryManager):
    @classmethod
    def connect(cls, uri):
        query_manager = cls()
        return f"syncing tables {query_manager.fetch_tables(uri)}"

    @classmethod
    def query_table(cls, uri, sort, table, col):
        query_manager = cls()
        return query_manager.query(uri, sort, table, col)

    @classmethod
    def use():
        query_manager = cls()
        return "Using Apollo's model"

    @classmethod
    def detectText():
        pass
