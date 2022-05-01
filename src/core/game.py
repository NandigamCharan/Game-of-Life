from src.core.point import Point
from src.core.board import Board


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
    def __init__(self, height: int = 1000, width: int = 1000, points: list[Point] = []):
        self.height = height
        self.width = width
        self.board = Board(height, width)
        self.old_board = Board(height, width)  # To avoid constructing new board everytime!
        self._set_points(points)

    def _set_points(self, points: list[Point]) -> None:
        for point in points:
            self.curr_board[point] = True

    def _get_points(self) -> list[Point]:
        points: list[Point] = []
        for point in Point.generate(self.width, self.height):
            if self.curr_board[point]:
                points.append(point)
        return points

    def _neighbors_alive(self, point: Point) -> int:
        alive_count = 0

        for new_point in Point.neighbors(point):
            if new_point in self.board.inbound(new_point) and self.old_board[new_point] == 1:
                alive_count += 1
        return alive_count

    def _next_frame(self) -> Board:
        self.board, self.old_board = self.old_board, self.board

        for point in Point.generate(self.height, self.width):
            alive_count = self._neighbors_alive(point)

            if self.old_board[point] == 1: # if alive
                if alive_count == 2 or alive_count == 3:
                    self.board[point] = 1
                else:
                    self.board[point] = 0
            else:
                if alive_count == 3:         # if dead
                    self.board[point] = 1
                else:
                    self.board[point] = 0
        return self.board

    def __next__(self):
        ...
