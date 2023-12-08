from typing import Iterator, List, Tuple
import re
from pathlib import Path

# Compile the regex pattern
pattern = re.compile(r'\d+')


def get_numbers_and_start_positions(line: str) -> dict[int, str]:
    # Find all matches of the compiled pattern in the string
    matches = pattern.finditer(line)
    return {match.start(): match.group() for match in matches}


def append_block(text_block: str) -> str:
    first_line_length = text_block.find('\n')
    line_append = '.' * first_line_length
    return line_append + '\n' + text_block + '\n' + line_append


def yield_line_groups(text_block: str) -> Iterator[List[str]]:
    lines = text_block.splitlines()
    for i in range(len(lines) - 2):
        yield lines[i:i + 3]


def check_for_symbol_in_line(original_line: str, number_positions: dict[int, str], verbose: bool = False) -> dict[int, str]:
    machine_ids = {}
    for pos, num in number_positions.items():
        if pos > 0:
            if original_line[pos - 1] != '.':
                machine_ids[pos] = num
        if pos + len(num) < len(original_line):
            end_pos = pos + len(num)
            if original_line[end_pos] != '.':
                machine_ids[pos] = num
    if verbose:
        print(f'check_for_symbol_in_line: {machine_ids}')
    return machine_ids


def check_for_symbol_in_adjacent_line(adjacent_line: str, number_positions: dict[int, str], verbose: bool = False) -> dict[int, str]:
    machine_ids = {}
    for pos, num in number_positions.items():
        start_pos = pos
        if pos > 0:
            start_pos -= 1
        end_pos = pos + len(num) + 1
        if len(set(adjacent_line[start_pos:end_pos]).difference(set('.123456789'))) > 0:
            machine_ids[pos] = num
    if verbose:
        print(f'check_for_symbol_in_adjacent_line: {machine_ids}')
    return machine_ids


def sum_machine_ids_from_line_group(line_group: Tuple[str, str, str], verbose: bool = False) -> int:
    line_above = line_group[0]
    line_middle = line_group[1]
    line_below = line_group[2]
    # Get the numbers and their start positions
    number_positions = get_numbers_and_start_positions(line_middle)
    machine_ids = {}
    machine_ids.update(check_for_symbol_in_line(line_middle, number_positions, verbose))
    machine_ids.update(check_for_symbol_in_adjacent_line(line_above, number_positions, verbose))
    machine_ids.update(check_for_symbol_in_adjacent_line(line_below, number_positions, verbose))
    if verbose:
        print(machine_ids)
    if len(machine_ids) != len(set(machine_ids.values())):
        print(machine_ids)
    return sum([int(x) for _, x in machine_ids.items()])


def solution(text_block: str, step: bool = False) -> int:
    text_block = append_block(text_block)
    if not step:
        return sum(sum_machine_ids_from_line_group(line_group) for line_group in yield_line_groups(text_block))

    running_sum = 0
    for line_group in yield_line_groups(text_block):
        for line in line_group:
            print(line)
        _ = sum_machine_ids_from_line_group(line_group, verbose=True)
        print(_)
        val = input()
        if val == 'q':
            break
        running_sum += _
    return running_sum
