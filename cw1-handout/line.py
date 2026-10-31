"""This module defines Line class."""


from itertools import chain

from branch import Branch
from exceptions import TubeError


class Line:
    def __init__(self, line_id: str, line_name: str):
        self.id = line_id
        self.name = line_name
        self.branches: dict[int, Branch] = {}

    def add_branch(self, branch: Branch) -> None:
        # is this true?
        if branch in self.branches[self.id]:
            raise TubeError(f"Branch is already present on line {self.name}.")

    def get_branch(self, id: int) -> Branch:
        if id in self.branches:
            return self.branches[id]
        raise TubeError(f"Branch does not exist on line {id}.")

    def get_stations(self) -> set[str]:
        """Returns a list of all stations on all branches on line."""
        # approach 1: use nested for loop to go over branches then
        #  go over stations in each branch to update the set in each such inner iteration.

        # approach 2: create intermidiate list of lists, flatten it and update the set once
        # stations_per_branch = [b.stations for b in self.branches]
        # all_stations = chain(*[stations_per_branch])
        # We will use chain.from_iterable to skip the flattening and intermediate list.
        stations_ids = set()
        all_stations = list(chain.from_iterable(
            [b.stations for b in self.branches]))
        stations_ids.update(all_stations)
        return stations_ids

    def __iter__(self):
        pass

    def __len__(self):
        pass

    def __contains__(self):
        pass

    def __repr__(self):
        pass
