from time import sleep
from src.core.point import Point
from src.core.game import Game


def run():
    # point = Point(1,1)
    # print(*point.neighbors())

    points = [Point(0, 0), Point(0, 1), Point(0, -1), Point(1, -1)]
    game = Game(6, 6, points)

    print(f"middle {game._middle}")
    for i in points:
        print(f"{game._middle + i}   neigh {game._neighbors_alive(game._middle + i)}")
        f""
    print(game._board)
    print(game._next_board())

    # while True:
    #     print(game._next_board())
    #     sleep(10)