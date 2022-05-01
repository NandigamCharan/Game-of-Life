from point import Point


class Board:
    def __init__(self, height: int = 1000, width: int = 1000, points: set[Point] = []):
        self.height: int = height
        self.width: int = width
        self.board: list[list[int]] = [[0 for _ in range(self.width)] for i in range(self.height)]
        self.setup(points)

    def __getitem__(self, point: Point):
        return self.board[point.x][point.y]

    def __setitem__(self, point: Point, value: bool):
        self.board[point.x][point.y] = value

    def inbound(self, point: Point) -> bool:
        """
        :param point: Point
        :return: bool
        """


        if 0 <= point.x < self.height and 0 <= point.y < self.width:
            return True
        return False
