from src.core.point import Point
from src.core.board import Board


class Game:
    def __init__(self, height: int = 1000, width: int = 1000, points: list[Point] = []):
        self.height = height
        self.width = width
        self.curr_board = Board(height, width)
        self.prev_boards: list[list[Point]] = []
        self._set_points(points)

    def _set_points(self, points: list[Point]):
        for point in points:
            self.curr_board[point] = True

    def _get_points(self):
        points: list[Point] = []
        for point in Point.generate(self.width, self.height):
            if self.curr_board[point]:
                points.append(point)
        return points

    def _next_frame(self):
        new_board = Board(self.height, self.width)

    def __next__(self):
        ...
