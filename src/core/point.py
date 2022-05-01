from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int

    @staticmethod
    def generate(height: int, width: int):
        for i in range(height):
            for j in range(width):
                yield Point(i, j)