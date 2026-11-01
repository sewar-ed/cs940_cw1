"""This module defines our Binary min-heap data structure."""


from typing import Any, List

from exceptions import HeapError


class Heap:
    def __init__(self):
        self.heap = []  # should this be a private attribute?

    def _propagate_up(self, item_idx: int) -> None:
        """Propagates the item up the heap to maintain the heap property."""
        while item_idx > 0 and self.heap[item_idx][0] > self.heap[(item_idx - 1) // 2][0]:
            # while new item has a *strictly* higher priority (to maintain insertion order in case of ties) than its parent,
            # we will swap them and update the new_item_idx, we will calculate current_parent_indx using: (new_item_idx - 1) // 2.
            self.heap[item_idx], self.heap[(
                item_idx - 1) // 2] = self.heap[(item_idx - 1) // 2], self.heap[item_idx]
            item_idx = (item_idx - 1) // 2

    def push(self, key, obj) -> None:
        """
        Inserts obj with priority key and restores the heap.
        """

        # This solution assumes that keys are comparable. Resources used as reference:
        # Introduction to Algorithms, 4th edition, Cormen, Leiserson, Rivest & Stein, The MIT Press, 2022 chapter 6 section 6.1.
        # Lecture 5 slide 14.

        # Step 1: add last to fill lowest level from left to right.
        self.heap.append((key, obj))
        new_item_idx = len(self.heap) - 1

        # Step 2: propagate the new item up the heap to maintain the heap property.
        self._propagate_up(new_item_idx)

    def _propagate_down(self, item_idx: int) -> None:
        """
        Propagates the item down the heap to maintain the heap property.
        """
        while item_idx * 2 + 1 < len(self.heap):
            # using the same logic used in _propagate_up, we will calculate left_child_idx, right_child_idx,
            # unlike _propagate_up we will swap when children have lower or *equal* priority to maintain insertion order
            # (rightmost element is the last inserted using our push method).
            pass

    def pop(self) -> Any:
        """
        Removes and returns the object with the minimum key, restoring
        the heap invariant afterwards. If several objects share the minimum key, return the one
        inserted earliest. This must run in O(log n). Raise HeapError if the heap is empty.
        """

        if len(self.heap) == 0:
            raise HeapError(
                "Heap is empty, cannot pop from an empty heap.")

        # This solution assumes our self.push was used to create the heap (break priority ties by insertion order)
        # and uses: https://stanford-cs161.github.io/winter2025/assets/files/lecture7-notes.pdf as reference.
        # Approach 1: pop root, use heapify on list -> O(n). Does NOT meet the O(log n) requirement in Q2.
        # Approaach 2: pop root, replace with rightmost leaf (to maintain level left to right property) and propagate root down.
        min_item = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._propagate_down(0)
        return min_item[1]

    def peek(self) -> Any:
        """
        Returns, without removing it, the next object according to the same
        priority and tie-breaking rules as pop. Raise HeapError if the heap is empty.
        """
        if len(self.heap) == 0:
            raise HeapError(
                "Heap is empty, cannot peek from an empty heap.")
        # By construction of our heap, this is just the obj of root item, O(1).
        return self.heap[0][1]

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
        return len(self.heap)

    def __bool__(self) -> bool:
        # should this check if heap non empt or check heap property?
        return len(self.heap) > 0

    def __repr__(self) -> str:
        return f"Heap()"
