from enum import Enum


class ShapePoints(Enum):
    X = 1
    Y = 2
    Z = 3


class ResultPoints(Enum):
    Win = 6
    Draw = 3
    Lose = 0


def points_for_shape(shape: str) -> int:
    return ShapePoints[shape].value


def points_for_result(result: str) -> int:
    return ResultPoints[result].value


def determine_game_result(game: list) -> str:
    if game[0] == 'A':
        if game[1] == 'X':
            return 'Draw'
        elif game[1] == 'Y':
            return 'Win'
        else:
            return 'Lose'

    elif game[0] == 'B':
        if game[1] == 'X':
            return 'Lose'
        elif game[1] == 'Y':
            return 'Draw'
        else:
            return 'Win'

    else:
        if game[1] == 'X':
            return 'Win'
        elif game[1] == 'Y':
            return 'Lose'
        else:
            return 'Draw'


with open("game_input.txt") as f:
    strategies = [list(map(str, line.split())) for line in f.read().split("\n")]
    points = []
    for strategy in strategies:
        points.append(points_for_shape(strategy[1]) + points_for_result(determine_game_result(strategy)))

    print(sum(points))
