from typing import Iterator


def count_common_elements(A, B):
    count = 0
    for element in B:
        if element in A:
            count += 1
    return count


def get_winning_numbers(data: str) -> list[int]:
    winning_nums = data.split('|')[0].strip().split(' ')
    winning_nums = list(filter(lambda x: x != '', winning_nums))
    winning_nums = list(map(int, winning_nums))
    return winning_nums


def get_game_numbers(data: str) -> list[int]:
    game_numbers = data.split('|')[1].strip().split(' ')
    game_numbers = list(filter(lambda x: x != '', game_numbers))
    game_numbers = list(map(int, game_numbers))
    return game_numbers


def get_num_matches(game: str) -> int:
    data = game.split(':')[1].strip()
    winning_nums = get_winning_numbers(data)
    game_numbers = get_game_numbers(data)

    return count_common_elements(winning_nums, game_numbers)


def get_game_score(game: str) -> int:
    num_matches = get_num_matches(game)
    if num_matches == 0:
        return 0
    return 2**(num_matches - 1)


def solution(lines: Iterator[str]) -> int:
    return sum(get_game_score(line) for line in lines)
