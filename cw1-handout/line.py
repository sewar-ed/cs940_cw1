"""This module defines Line class."""


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
        pass
