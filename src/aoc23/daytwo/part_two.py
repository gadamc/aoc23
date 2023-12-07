from typing import Iterator

from functools import reduce
import operator

from aoc23.daytwo.part_one import color_counts_per_grab


def get_minimum_power_of_cubes(line: str) -> int:
    """
    Example input
    Game 1: 1 red, 3 blue, 11 green; 1 blue, 5 red; 3 blue, 5 green, 13 red; 6 red, 1 blue, 4 green; 16 red, 12 green
    """
    game_id, bag_grabs = line.split(":")
    game_id = game_id.strip()
    if not game_id.startswith("Game "):
        return 0
    game_id = int(game_id.split(" ")[1])

    max_values_per_color = {'red': 0, 'green': 0, 'blue': 0}

    for a_grab in color_counts_per_grab(bag_grabs.strip()):
        for color, count in a_grab.items():
            max_values_per_color[color] = max(max_values_per_color[color], count)

    product = reduce(operator.mul, max_values_per_color.values())
    return product


def solution(lines: Iterator[str]) -> int:
    return sum(get_minimum_power_of_cubes(line) for line in lines)
