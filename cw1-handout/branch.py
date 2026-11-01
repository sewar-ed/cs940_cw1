"""This module defines a Branch class."""

from typing import List

from exceptions import DataStructureError
from station import Station


class Branch:

    def __init__(self, branch_id: int, next_branch_ids: List[int]):
        self.id = branch_id
        self.next_branches_ids = next_branch_ids
        self.stations: List[str] = []

    def add_station(self, station: str) -> None:
        self.stations.append(station)

    def station_edges(self) -> List[tuple[str, str]]:
        """
        Returns station edges along the branch.
        Output: [(station_on_branch, next_station_reachable_on_branch),..]
        """
        # Approach 1: [(self.stations[i], self.stations[i+1]) for i in range(len(self.stations)-1)]
        # Approach 2 / more efficient:
        return [*zip(self.stations, self.stations[1:])]

    def branch_edges(self) -> List[tuple[int, int]]:
        """
        Returns the edges between current branch and its next branches.
        Output: [(current_branch_id, next_branch_id),..]
        """
        return [*zip([self.id]*len(self.next_branches), self.next_branches_ids)]

    def __iter__(self):
        """
        Iterates over Branch by going over stations in branch.
        """
        return iter(self.stations)

    def __len__(self):
        """
        Returns len of Branch by number of edges between stations in branch.
        """
        return len(self.station_edges)

    def __contains__(self, station: Station):
        return station.station_name in self.stations

    def __getitem__(self, idx):
        if idx > len(self.stations) or idx < 0:
            raise DataStructureError(
                "Index is out of bounds for this branch.")
        return self.stations[idx]

    def __repr__(self):
        return f"Branch('{self.branch_id}','{self.next_branches_ids}')"
