"""This module defines Trie class."""

from typing import Any, List

# TODO: Implement a trie (prefix tree) data structure as Trie in trie.py. The trie stores objects associated with string keys.
#  A key may contain multiple words, separated by the space character
# ''. Each word in the key must be independently searchable: an object matches a prefix if
# the prefix occurs at the beginning of any word in its key. For example, an object stored with
# the key "data structures" should be found by prefixes such as "dat" and "str", but not by
# "ruc". Prefixes do not span word boundaries.


class Trie:
    def __init__(self):
        pass

    def insert(self, key: str, obj: Any) -> None:
        # TODO: associates obj with key and indexes
        # each word of the key in the trie. Add appropriate validation for key, including malformed
        # or empty keys.
        pass

    def search_by_prefix(self, prefix: str) -> List[Any]:
        # TODO: returns all objects for which
        # at least one word in the associated key begins with prefix. Return an empty list if there
        # are no matches, and every stored object if prefix is empty. Each matching object must
        # occur at most once in the result, even if several words or keys associated with it match.
        # Results must be produced in a deterministic order. The search must run in
        # O(m + size of the matching subtree),
        # where m is the length of prefix.
        pass
