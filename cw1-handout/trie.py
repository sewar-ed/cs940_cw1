"""This module defines Trie class."""

from exceptions import TrieError


class TrieNode:
    children = {}
    objects = set()
    sub_objs = set()  # all objects in subtree of root


class Trie:
    def __init__(self):
        """Init trie root."""
        self.root = TrieNode()

    def insert(self, key: str, obj: any) -> None:
        """ 
        Associates obj with key,
        indixes each word of the key in the trie to enable obj recovery by prefix.
        """
        # validate keys
        if not isinstance(key, str) or key == "" or all([w == "" for w in key.split(" ")]):
            raise TrieError("Key is empty or is malformed.")
        # extract words from key, remove any empty ones
        words = [w for w in key.lower().split(" ") if w != ""]
        # build trie
        for word in words:
            curr_root = self.root  # for each word in keys we have the same root
            for c in word:
                if c not in curr_root.children:
                    curr_root.children[c] = TrieNode()
                curr_root = curr_root.children[c]  # move pointer down
            curr_root.objects.add(obj)
        curr_root.sub_objs.add(obj)

    def search_by_prefix(self, prefix: str) -> list[any]:
        """
        Returns all objects for which at least one word in the associated key begins with prefix. Return an empty list if there
        are no matches, and every stored object if prefix is empty. 
        """
        # approach 2: utilize sub_obj set for each TrieNode to find all obj in its subtree in linear time
        pointer = self.root  # we want to traverse trie
        # find node at end of prefix
        for c in prefix:
            if c not in pointer.children:
                return []  # no such prefix in our trie
            # find children of the last node in prefix
            pointer = pointer.children[c]
        return list(pointer.sub_objs)

    # approach 1: does not meet complexity requirements
    # def _dfs(self, visited: set, matching_objects: list[any], root: TrieNode):
    #     """
    #     DFS to traverse trie from given root to leaf.
    #     """
    #     for obj in root.objects:
    #         if obj not in visited:  # ensures no duplicates
    #             visited.add(obj)
    #             matching_objects.append(obj)  # to preserve order
    #     sorted_keys = sorted(root.children.keys())  # det. order
    #     for c in sorted_keys:
    #         self._defs(root.children[c], visited, matching_objects)
    #     # iterative approach:
    #     # to_visit = [root]
    #     # while to_visit:
    #     #     curr_root = to_visit.pop()
    #     #     # push unseen obj
    #     #     for obj in curr_root.objects:
    #     #         if obj not in visited:
    #     #             visited.add(obj)
    #     #             matching_objects.append(obj)
    #     #     # to maintain det. order
    #     #     sorted_keys = sorted(root.children.keys())
    #     #     for c in sorted_keys:
    #     #         to_visit.append(root.children[c])
    #    Inside function:
        # visited = set()
        # matching_objects = []
        # # our leaves are our corresponding key objects, find all paths to leaves using dfs
        # self._dfs(visited, matching_objects, pointer)
        # return matching_objects
