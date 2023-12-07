from typing import Iterator

"""
Condition
only 12 red cubes, 13 green cubes, and 14 blue cubes
"""
max_values_per_color = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def color_counts_per_grab(line: str) -> Iterator[dict[str, int]]:
    """
    Example input
    3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    """
    for color_count in line.split(";"):
        color_counts = {}
        color_count = color_count.strip()
        for color_pair in color_count.split(","):
            count, color = color_pair.strip().split(" ")
            count = int(count)
            color_counts[color] = count
        yield color_counts


def get_game_id_if_valid(line: str) -> int:
    """
    Example input
    Game 1: 1 red, 3 blue, 11 green; 1 blue, 5 red; 3 blue, 5 green, 13 red; 6 red, 1 blue, 4 green; 16 red, 12 green
    """
    game_id, bag_grabs = line.split(":")
    game_id = game_id.strip()
    if not game_id.startswith("Game "):
        return 0
    game_id = int(game_id.split(" ")[1])

    for a_grab in color_counts_per_grab(bag_grabs.strip()):
        for color, count in a_grab.items():
            if count > max_values_per_color[color]:
                return 0

    return game_id


def solution(lines: Iterator[str]) -> int:
    return sum(get_game_id_if_valid(line) for line in lines)
