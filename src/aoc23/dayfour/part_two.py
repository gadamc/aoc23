from typing import Iterator
import dataclasses
import re

from . import part_one


@dataclasses.dataclass
class GameCard:
    winning_numbers: list
    game_numbers: list
    copy_counter: int


def extract_card_number(input_string: str) -> str:
    match = re.search(r'Card\s+(\d+):', input_string)
    return match.group(1) if match else None


def build_game_deck(lines: Iterator[str]) -> dict[int, GameCard]:
    game_deck = {}
    for line in lines:
        if 'Card' in line:
            card_number = int(extract_card_number(line))
            data = line.split(':')[1].strip()
            winning_numbers = part_one.get_winning_numbers(data)
            game_numbers = part_one.get_game_numbers(data)
            game_deck[card_number] = GameCard(winning_numbers, game_numbers, 1)
        else:
            raise Exception(f'Invalid line: {line}')
    return game_deck


def create_duplicates(game_deck: dict[int, GameCard]) -> dict[int, GameCard]:
    for i in range(1, len(game_deck) + 1):
        a_game = game_deck[i]
        num_matches = part_one.count_common_elements(a_game.winning_numbers, a_game.game_numbers)
        for _ in range(a_game.copy_counter):
            for j in range(num_matches):
                if i + j + 1 > len(game_deck):
                    break
                game_deck[i + j + 1].copy_counter += 1

    return game_deck


def solution(lines: Iterator[str]) -> int:
    game_deck = build_game_deck(lines)
    game_deck = create_duplicates(game_deck)
    return sum([a_game.copy_counter for game_num, a_game in game_deck.items()])
