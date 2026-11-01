"""This module defines our Binary min-heap data structure."""


from typing import Any, List


class Heap:
    def __init__(self):
        pass

    def push(self, key, obj) -> None:
        # TODO:  inserts obj with priority key and restores the heap
        # invariant. This must run in O(log n)
        pass
        pass

    def pop(self) -> Any:
        # TODO: removes and returns the object with the minimum key, restoring
        # the heap invariant afterwards. If several objects share the minimum key, return the one
        # inserted earliest. This must run in O(log n). Raise HeapError if the heap is empty.
        pass

    def peek(self) -> Any:
        # TODO: returns, without removing it, the next object according to the same
        # priority and tie-breaking rules as pop. Raise HeapError if the heap is empty
        pass

    def ksmallest(self, k: int) -> List[Any]:
        # TODO: returns the objects associated with the k
        # smallest keys, in non-decreasing key order, without modifying the heap. Objects with
        # equal keys must appear in insertion order. Support k = -1 as a request for all stored
        # objects and k=0 as a request for an empty list. If k is greater than the number of
        # objects in the heap, return all stored objects. Raise HeapError for other negative values.
        # Your solution should exploit the ordering already provided by the binary-heap structure
        # rather than sorting all entries or copying the entire heap and repeatedly calling pop
        pass

    def heapify(cls, items: List) -> "Heap":
        # TODO: constructs and returns a heap from a list of
        # key–object pairs. The order of pairs in items is treated as their insertion order when
        # resolving equal keys. The resulting heap must not alias the input list, and construction
        # must run in O(n) time
        pass

    def __len__(self) -> int:
        pass

    def __bool__(self) -> bool:
        pass

    def __repr__(self) -> str:
        pass
