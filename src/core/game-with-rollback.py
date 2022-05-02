import src.core.game as game
from src.core.point import Point
from src.core.point import Point

class Game(game.Game):
    def __init__(self):
        super(Game, self).__init__()
        self.prev_boards: list[list[Point]] = []

    def _get_points(self) -> list[Point]:
        points: list[Point] = []
        for point in Point.generate(self._rows, self._cols):
            if self._board[point]:
                points.append(point)
        return points

