class FirebaseConnectionError(Exception):
    """
    There was an error connecting to the firebase client.
    """

    def __init__(self, obj, message="Unable to reach the firebase client"):
        self.obj = obj
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.obj} -> {self.message}"


class PostgresConnectionError(Exception):
    """
    There was an error connecting to the postgres client.
    """

    def __init__(self, obj, message="Unable to reach the postgres client"):
        self.obj = obj
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.obj} -> {self.message}"


class ClientSDKSetupError(Exception):
    """
    There was an error accepting your auth token.
    """

    def __init__(self, obj, message="Unable to init the headless sdk"):
        self.obj = obj
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.obj} -> {self.message}"


class ExecutionError(Exception):
    """
    There was an error executing sql query.
    """

    def __init__(
        self, obj, message="Unable to execute sql query, check your connection info"
    ):
        self.obj = obj
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.obj} -> {self.message}"
