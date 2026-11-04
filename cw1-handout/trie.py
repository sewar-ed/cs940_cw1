"""This module defines Trie class."""

from exceptions import TrieError


class TrieNode:
    children = {}
    objects = set()


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
        words = [w for w in key.split(" ") if w != ""]
        # build trie
        for word in words:
            root = self.root  # for each word in keys we have the same root
            for c in word:
                if c not in root.children:
                    self.root.children[c] = TrieNode()
                root = root.children[c]  # move pointer down
            root.objects.add(obj)

    def _dfs(self, root: TrieNode, visited: set, matching_objects: list[any]):
        """
        DFS to traverse trie from given root to leaf.
        """
        for obj in root.objects:
            if obj not in visited:  # ensures no duplicates
                visited.add(obj)
                matching_objects.append(obj)  # to preserve order
        sorted_keys = sorted(root.children.keys())  # det. order
        for c in sorted_keys:
            self._defs(root.children[c], visited, matching_objects)

    def search_by_prefix(self, prefix: str) -> list[any]:
        """
        Returns all objects for which at least one word in the associated key begins with prefix. Return an empty list if there
        are no matches, and every stored object if prefix is empty. 
        """
        pointer = self.root  # we want to traverse trie
        # find node at end of prefix
        # TODO: CHECK IF I NEED TO DEAL WITH EMPTY PREFIX
        for c in prefix:
            if c not in pointer.children:
                return []  # no such prefix in our trie
            # find children of the last node in prefix
            pointer = pointer.children[c]

        visited = set()
        matching_objects = []
        # our leaves are our corresponding key objects, find all paths to leaves using dfs
        self._dfs(visited, matching_objects, pointer)
        return matching_objects
