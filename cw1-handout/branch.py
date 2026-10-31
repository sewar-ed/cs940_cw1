"""This module defines a Branch class."""

from typing import List


class Branch:
    def __init__(self, branch_id: int, next_branch_ids: List[int]):
        self.id = branch_id
        self.next_branches = next_branch_ids
        self.stations: List[str] = []

    def add_station(self, station: str):
        # should we add to end or beg? should we add at index?
        self.stations.append(station)

    def station_edges(self) -> List[tuple[str, str]]:
        pass

    def branch_edges(self) -> List[tuple[int, int]]:
        pass

    def __iter__(self):
        pass

    def __len__(self):
        pass

    def __contains__(self):
        pass

    def __getitem__(self):
        pass

    def __repr__(self):
        pass
