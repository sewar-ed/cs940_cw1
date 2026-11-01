"""
This module creates our own Exceptions heirarchy. 1(a)
"""


class TubeError(Exception):
    """ Exception raised for tube related errors."""

    def __init__(self, error_message: str = ""):
        self.message = error_message
        super().__init__(self.message)


class DataStructureError(Exception):
    """ Exception raised for data structure related errors."""

    def __init__(self, error_message: str = "", type: str = ""):
        self.message = error_message
        self.type = type
        super().__init__(
            f"Error for data structure of type {self.type}: {self.message}")
