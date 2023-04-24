class SpecialistNotFoundError(Exception):
    """
    Wrapper to raise exception for specialist not found.
    """

    def __init__(
        self, obj, message="Unable to find specialist or specialist doesn't exist."
    ):
        self.obj = obj
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.obj} -> {self.message}"


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
