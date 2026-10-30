"""
This module creates our own exceptions heirarchy. 1(a)
"""
def TubeError(Exception):
    """ Exception raised for tube related errors."""

    def __init__(self, error_message: str = ""):
        self.message = error_message
        super().__init__(self.message)

def DataStructureError(Exception):
    """ Exception raised for data structure related errors."""

    def __init__(self, error_message: str = ""):
        self.message = error_message
        super().__init__(self.message)