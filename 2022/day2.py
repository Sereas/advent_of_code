from enum import Enum


class ShapePoints(Enum):
    Rock = 1
    Paper = 2
    Scissors = 3


class ResultPoints(Enum):
    Win = 6
    Draw = 3
    Lose = 0


def points_for_shape(shape: str) -> int:
    return ShapePoints[shape].value


def points_for_result(result: str) -> int:
    return ResultPoints[result].value


def mapping(strategy: str) -> str:
    if strategy == 'X' or strategy == 'A':
        return 'Rock'
    elif strategy == 'Y' or strategy == 'B':
        return 'Paper'
    else:
        return 'Scissors'


def mapping_task2(strategy: str) -> str:
    if strategy == 'A':
        return 'Rock'
    elif strategy == 'B':
        return 'Paper'
    elif strategy == 'C':
        return 'Scissors'
    elif strategy == 'X':
        return 'Lose'
    elif strategy == 'Y':
        return 'Draw'
    elif strategy == 'Z':
        return 'Win'


def determine_game_result(game: list) -> str:
    if game[0] == 'Rock':
        if game[1] == 'Rock':
            return 'Draw'
        elif game[1] == 'Paper':
            return 'Win'
        else:
            return 'Lose'

    elif game[0] == 'Paper':
        if game[1] == 'Rock':
            return 'Lose'
        elif game[1] == 'Paper':
            return 'Draw'
        else:
            return 'Win'

    else:
        if game[1] == 'Rock':
            return 'Win'
        elif game[1] == 'Paper':
            return 'Lose'
        else:
            return 'Draw'


def determine_shape(game: list) -> str:
    if game[0] == 'Rock':
        if game[1] == 'Lose':
            return 'Scissors'
        elif game[1] == 'Win':
            return 'Paper'
        else:
            return 'Rock'

    elif game[0] == 'Paper':
        if game[1] == 'Lose':
            return 'Rock'
        elif game[1] == 'Win':
            return 'Scissors'
        else:
            return 'Paper'

    else:
        if game[1] == 'Lose':
            return 'Paper'
        elif game[1] == 'Win':
            return 'Rock'
        else:
            return 'Scissors'


with open("game_input.txt") as f:
    strategies = [list(map(mapping, line.split())) for line in f.read().split("\n")]
    points = [points_for_shape(strategy[1]) + points_for_result(determine_game_result(strategy)) for strategy in
              strategies]

    print('Sum of points: ', sum(points))

with open("game_input.txt") as f:
    task2_strategies = [list(map(mapping_task2, line.split())) for line in f.read().split("\n")]
    task2_points = [points_for_shape(determine_shape(strategy)) + points_for_result(strategy[1]) for strategy in
                    task2_strategies]
    print('Sum of points task 2: ', sum(task2_points))
