from dataclasses import dataclass
# from src.utils.neighbor_directions import DIRS


DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, 1)]

@dataclass
class Point:
    x: int
    y: int

    @staticmethod
    def generate(height: int, width: int):
        for i in range(height):
            for j in range(width):
                yield Point(i, j)

    @staticmethod
    def neighbors(point: Point):
        for x, y in DIRS:
            yield Point(point.x - x, point.y - y)