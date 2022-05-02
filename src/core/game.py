from src.core.point import Point
from src.core.board import Board
from typing import *


class Game:
    """
    =====
    RULES
    =====
    1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
    2. Any live cell with two or three live neighbours lives on to the next generation.
    3. Any live cell with more than three live neighbours dies, as if by overpopulation.
    4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
    """

    def __init__(self, height: int = 1000, width: int = 1000, points: List[Point] = None):
        if points is None:
            points = []
        self._cols = height
        self._rows = width
        self._middle: Point = Point(self._cols//2, self._rows//2)

        self._board = Board(height, width)
        self._old_board = Board(height, width)  # To avoid constructing new board everytime!
        self._set_points(points)

    def _set_points(self, points: List[Point]) -> None:
        for point in points:
            print(self._middle + point)
            self._board[self._middle + point] = 1

    def _neighbors_alive(self, point: Point) -> int:
        alive_count = 0

        for new_point in point.neighbors():
            if new_point in self._board and self._board[new_point] == 1:
                alive_count += 1
        return alive_count

    def _next_board(self) -> Board:
        new_board = self._old_board

        for point in Point.generate(self._cols, self._rows):
            alive_count = self._neighbors_alive(point)

            if self._board[point] >= 1:   # if alive
                if alive_count == 2 or alive_count == 3:
                    new_board[point] = 1
                else:
                    new_board[point] = 0
            else:
                if alive_count == 3:         # if dead
                    new_board[point] = 1
                else:
                    new_board[point] = 0

        self._old_board = self._board
        self._board = new_board
        return self._board

    def __next__(self):
        ...
