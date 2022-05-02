from __future__ import annotations
from dataclasses import dataclass
from typing import ClassVar
from typing import List
from typing import Generator




@dataclass
class Point:
    col: int
    row: int

    def __add__(self, other):
        return Point(self.col + other.col, self.row + other.row)

    def neighbors(self) -> Generator[Point]:
        for other in DIRS:
            yield self + other

    @staticmethod
    def generate(cols: int, rows: int) -> List[Point]:
        for i in range(cols):
            for j in range(rows):
                yield Point(i, j)
        return


DIRS: ClassVar[List[Point]] = [Point(0, 1), Point(0, -1), Point(1, 0), Point(-1, 0),
                               Point(1, 1), Point(1, -1), Point(-1, 1), Point(-1, -1)]
