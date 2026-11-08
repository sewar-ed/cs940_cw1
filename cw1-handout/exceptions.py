"""
This module creates our own Exceptions heirarchy. 1(a)
"""


class TubeError(Exception):
    """ Exception raised for tube related errors."""


class BranchError(TubeError):
    """Exception raised for Branch related errors."""


class LineError(TubeError):
    """Exception raised for Line related errors."""


class PredictionError(TubeError):
    """Exception raised for Prediction related errors."""


class DataStructureError(Exception):
    """ Exception raised for data structure related errors."""


class HeapError(DataStructureError):
    """ Exception raised for heap related errors."""


class TrieError(DataStructureError):
    """ Exception raised for trie related errors."""


class NetworkError(TubeError, DataStructureError):
    """ Exception raised for Network related errors."""
