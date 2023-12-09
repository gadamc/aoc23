from typing import Tuple
import re

from . import part_one

# Compile the regex pattern
pattern = re.compile(r'\*')


def get_gear_positions(line: str) -> list[int]:
    # Find all matches of the compiled pattern in the string
    matches = pattern.finditer(line)
    return [match.start() for match in matches]


def check_machineids_near_gears_in_line(a_line: str, verbose: bool = False) -> dict[int, list[str]]:
    '''
    returns position of gear and list of machine ids that are adjacent to it in the same line
    '''
    gear_positions_and_ids = {}
    numbers_pos = part_one.get_numbers_and_start_positions(a_line)
    gear_positions = get_gear_positions(a_line)
    for gpos in gear_positions:
        gear_positions_and_ids[gpos] = []
        for npos, val in numbers_pos.items():
            if npos < gpos:
                if npos + len(val) == gpos:
                    gear_positions_and_ids[gpos].append(val)
            else:
                if npos == gpos + 1:
                    gear_positions_and_ids[gpos].append(val)
    if verbose:
        print(f'check_machineids_near_gears_in_line: {gear_positions_and_ids}')
    return gear_positions_and_ids


def get_machine_ids_in_adjacent_line(adjacent_line: str, gear_positions: list[int], verbose: bool = False) -> dict[int, str]:

    gear_positions_and_ids = {}
    for gpos in gear_positions:
        gear_positions_and_ids[gpos] = []

        for npos, val in part_one.get_numbers_and_start_positions(adjacent_line).items():
            if npos == gpos or npos == gpos + 1:
                gear_positions_and_ids[gpos].append(val)
            elif npos < gpos and npos + len(val) >= gpos:
                gear_positions_and_ids[gpos].append(val)
    if verbose:
        print(f'get_machine_ids_in_adjacent_line: {gear_positions_and_ids}')
    return gear_positions_and_ids


def sum_gear_ratios_from_line_group(line_group: Tuple[str, str, str], verbose: bool = False) -> int:
    line_above = line_group[0]
    line_middle = line_group[1]
    line_below = line_group[2]

    gear_positions = check_machineids_near_gears_in_line(line_middle, verbose)
    if len(gear_positions) == 0:
        return 0

    adjacent_machine_ids = get_machine_ids_in_adjacent_line(line_above, list(gear_positions.keys()), verbose)
    for gpos, ids in adjacent_machine_ids.items():
        gear_positions[gpos].extend(ids)

    adjacent_machine_ids = get_machine_ids_in_adjacent_line(line_below, list(gear_positions.keys()), verbose)
    for gpos, ids in adjacent_machine_ids.items():
        gear_positions[gpos].extend(ids)

    if verbose:
        print(gear_positions)

    valid_gears = {}
    for gpos, ids in gear_positions.items():
        if len(ids) == 2:
            valid_gears[gpos] = ids

    if verbose:
        print(valid_gears)

    return sum([int(x[0]) * int(x[1]) for _, x in valid_gears.items()])


def solution(text_block: str, step: bool = False) -> int:
    text_block = part_one.append_block(text_block)
    if not step:
        return sum(sum_gear_ratios_from_line_group(line_group) for line_group in part_one.yield_line_groups(text_block))

    running_sum = 0
    for line_group in part_one.yield_line_groups(text_block):
        for line in line_group:
            print(line)
        _ = sum_gear_ratios_from_line_group(line_group, verbose=True)
        print(_)
        val = input()
        if val == 'q':
            break
        running_sum += _
    return running_sum
