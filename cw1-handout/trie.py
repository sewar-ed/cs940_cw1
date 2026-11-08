"""This module defines Trie class."""

from exceptions import TrieError


class TrieNode:
    def __init__(self):
        self.children = {}
        self.objects = set()  # eow indicator
        self.sub_objs = set()  # all objects in subtree of current node


class Trie:
    def __init__(self):
        """Init trie root."""
        self.root = TrieNode()

    def insert(self, key: str, obj: any) -> None:
        """ 
        Associates obj with key,
        indixes each word of the key in the trie to enable obj recovery by prefix.
        """
        # Reference used: https://stackoverflow.com/questions/11015320/how-to-create-a-trie-in-python
        # validate keys, normalize by using lower case
        if not isinstance(key, str) or key == "" or all([w == "" for w in key.lower().split(" ")]):
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
                # add obj for all nodes along the path
                curr_root.sub_objs.add(obj)
            curr_root.objects.add(obj)  # add obj to end of word character

    def search_by_prefix(self, prefix: str) -> list[any]:
        """
        Returns all objects for which at least one word in the associated key begins with prefix. Return an empty list if there
        are no matches, and every stored object if prefix is empty. 
        """
        # approach 1: traverse path using dfs to get to object per path -> recursive might time out, iterative does not meet the requirements.
        # approach 2: utilize sub_obj set for each TrieNode to find all obj in its subtree in linear time.
        pointer = self.root  # we want to traverse trie
        # find node at end of prefix
        for c in prefix:
            if c not in pointer.children:
                return []  # no such prefix in our trie
            # find children of the last node in prefix
            pointer = pointer.children[c]
        return list(pointer.sub_objs)
