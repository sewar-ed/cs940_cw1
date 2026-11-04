"""This module defines our Binary min-heap data structure."""


from exceptions import HeapError


class Heap:
    def __init__(self):
        self.heap = []  # should this be a private attribute?

    def _propagate_up(self, item_idx: int) -> None:
        """
        Propagates the item up the heap to maintain the heap property.
        """
        while item_idx > 0 and self.heap[item_idx][0] < self.heap[(item_idx - 1) // 2][0]:
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
        child_idx = item_idx * 2 + \
            1  # updated later to whichever child has the lowest priority in *
        while child_idx < len(self.heap):
            # using the same logic used in _propagate_up, we will calculate left_child_idx, right_child_idx,
            # we will swap when children have *strictly* lower priority to maintain insertion order

            if child_idx + 1 < len(self.heap) and self.heap[child_idx+1][0] < self.heap[child_idx][0]:
                # *: right child exists and its priority is < then left child.
                child_idx += 1

            if self.heap[child_idx][0] < self.heap[item_idx][0]:
                self.heap[child_idx], self.heap[item_idx] = self.heap[item_idx], self.heap[child_idx]
                item_idx = child_idx
                child_idx = item_idx * 2 + 1
            else:
                break

    def pop(self) -> any:
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

    def peek(self) -> any:
        """
        Returns, without removing it, the next object according to the same
        priority and tie-breaking rules as pop. Raise HeapError if the heap is empty.
        """
        if len(self.heap) == 0:
            raise HeapError(
                "Heap is empty, cannot peek from an empty heap.")
        # By construction of our heap, this is just the obj of root item, O(1).
        return self.heap[0][1]

    def ksmallest(self, k: int) -> list[any]:
        """
        Returns the objects associated with the k
        smallest keys, in non-decreasing key order, without modifying the heap.
        """
        # approach 1: shallow copy heap and pop K times O(n+klogn).

        # approach 2: use bfs with modifications. Since elements in the heap guarantee order with respect to level (parent-children),
        #  we can find insertion order of the children to our queue/list by comparing their priority. \
        # However, the complexity of this is O(k^2) since for each item we will have to scan its children.

        # approach 3: use our min heap class with a helper heap that would only contain candidates to be in ksmallest and not the whole list,
        # which would bring our extraction down from O(logn) to O(logk).
        if k == 0:
            return []
        if k == -1 or k > len(self.heap):
            k = len(self.heap)
        if k < 0:
            raise HeapError(
                "Cannot extract negative number of K elements from Heap.")
        ksmallest = []
        helper_heap = Heap()
        # push curr min item and its index
        # since our pop only returns obj we will use (key, obj=(index,obj)) tuples
        helper_heap.push(self.heap[0][0], (0, self.heap[0]))
        while len(ksmallest) < k:
            curr_idx, curr_obj = helper_heap.pop()  # current min
            print(curr_obj)
            ksmallest.append(curr_obj[1])
            left_child, right_child = 2*curr_idx+1, 2 * \
                curr_idx+2  # if children exist, push to heap
            if left_child < len(self.heap):
                helper_heap.push(
                    self.heap[left_child], (left_child, self.heap[left_child]))
            if right_child < len(self.heap):
                helper_heap.push(
                    self.heap[right_child], (right_child, self.heap[right_child]))
        return ksmallest

    @classmethod
    def heapify(cls, items: list) -> "Heap":
        """
        Constructs and returns a heap from a list of key,object pairs. The order of pairs in items is 
        treated as their insertion order when resolving equal keys.
        """
        result_items = cls()
        result_items.heap = items[:]
        # leaves already satisfy heap property, we will look for last parent and propagate down using its key,
        # the path from parent to leaves is shorter than root to some node considering the heap is dense on lower levels,
        # therefore the requirement of O(n) is satisfied. Resources used as reference:
        # https://stackoverflow.com/questions/9755721/how-can-building-a-heap-be-on-time-complexity
        for i in range(len(result_items.heap) // 2 - 1, -1, -1):
            result_items._propagate_down(i)
        return result_items

    def __len__(self) -> int:
        return len(self.heap)

    def __bool__(self) -> bool:
        # should this check if heap non empt or check heap property?
        return len(self.heap) > 0

    def __repr__(self) -> str:
        return f"Heap()"


# if __name__ == '__main__':
#     import random
#     print("Running Heap Class tests...")
#     my_heap = Heap()
#     print(f"initial heap: {my_heap}")
    # objs = [(1, "a"), (2, "b"), (3, "c"), (4, "d"), (5, "e")]
    # objs = [(1, "a"), (2, "b"), (3, "c"), (4, "d"), (5, "e")]
    # results:
    # Running Heap Class tests...
    # initial heap: Heap()
    # shuffled objs: [(2, 'b'), (2, 'c'), (5, 'e'), (4, 'd'), (1, 'a')]
    # pushed (2, b), heap: [(2, 'b')]
    # pushed (2, c), heap: [(2, 'b'), (2, 'c')]
    # pushed (5, e), heap: [(2, 'b'), (2, 'c'), (5, 'e')]
    # pushed (4, d), heap: [(2, 'b'), (2, 'c'), (5, 'e'), (4, 'd')]
    # pushed (1, a), heap: [(1, 'a'), (2, 'b'), (5, 'e'), (4, 'd'), (2, 'c')]
    # popped, heap: [(2, 'b'), (2, 'c'), (5, 'e'), (4, 'd')]
    # random.shuffle(objs)
    # print(f"shuffled objs: {objs}")
    # for key, obj in objs:
    #     my_heap.push(key, obj)
    #     print(f"pushed ({key}, {obj}), heap: {my_heap.heap}")
    # my_heap.pop()
    # print(f"popped, heap: {my_heap.heap}")
    # print(f"peek: {my_heap.peek()}")
    # print("=================")
    # print("Running Heapify tests...")
    # # TODO: debug this does not preserve insertion order for equal keys
    # list_to_heapify = [(1, 'e'), (1, 'a'), (1, 'c'), (1, 'd'), (1, 'b')]
    # print(f"list to heapify: {list_to_heapify}")
    # heap_from_list = Heap.heapify(list_to_heapify)
    # print(f"ksmallest from heap: {my_heap.ksmallest(3)}")
    # print(f"number of swaps: {swaps}")
