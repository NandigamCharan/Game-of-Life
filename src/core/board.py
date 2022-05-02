from __future__ import annotations
from src.core.point import Point
from typing import List


class Board:
    def __init__(self, cols: int = 1000, rows: int = 1000):
        self._cols: int = cols
        self._rows: int = rows
        self._board: List[List[int]] = [[0 for _ in range(self._cols)] for _ in range(self._rows)]

    def __getitem__(self, point: Point) -> int:
        return self._board[point.row][point.col]

    def __setitem__(self, point: Point, value: int):
        self._board[point.row][point.col] = value

    def __contains__(self, point: Point) -> bool:
        """
        Checks if point is in the bounds.

        USEAGE
        >>> board = Board()
        >>> point in board
        """

        if 0 <= point.row < self._rows and 0 <= point.col < self._cols:
            return True
        return False

    def __str__(self) -> str:
        x = "\n ".join(str(i) for i in self._board)
        return f' cols = {self._cols} \n rows = {self._rows} \n {x}'
