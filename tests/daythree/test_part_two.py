from pathlib import Path

import pytest

import aoc23.daythree.part_two as test_module

_challenge_data = (Path(__file__).parent / "data.dat").open().read()
_challenge_solution = 77509019

_example_data = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.*""".strip()
_example_solution = 467835
# sum of the gear ratios.
# gear ratios are the product of part numbers are adjacent, including diagonally, to a "*" symbol, which defines a "gear"
# also, a gear is only adjacent to exactly two part numbers.
# Find all of the gears, then sum their ratios.
# 467*35 + 755*598 = 467835

_test2_data = """
467..114.1
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.*""".strip()
_test2_solution = 467835


@pytest.mark.parametrize(
    "input_data,expected_output",
    [
        pytest.param(
            _example_data,
            _example_solution,
            id="example",
        ),
        pytest.param(
            _test2_data,
            _test2_solution,
            id="test2",
        ),
        pytest.param(
            _challenge_data,
            _challenge_solution,
            id="challenge",
        ),
    ],
)
def test_runner(input_data: str, expected_output: int) -> None:
    assert test_module.solution(input_data) == expected_output


in_line_test_1 = "617*......"
in_line_test_solution1 = {3: ['617']}

in_line_test_2 = "..&*45...."
in_line_test_solution2 = {3: ['45']}

in_line_test_3 = "...*......"
in_line_test_solution3 = {3: []}

in_line_test_4 = ".........*"
in_line_test_solution4 = {9: []}

in_line_test_5 = "....123*"
in_line_test_solution5 = {7: ['123']}

in_line_test_6 = "....123*45"
in_line_test_solution6 = {7: ['123', '45']}

in_line_test_7 = "....123*45*67"
in_line_test_solution7 = {7: ['123', '45'], 10: ['45', '67']}

in_line_test_8 = "*........."
in_line_test_solution8 = {0: []}

in_line_test_9 = "*9........"
in_line_test_solution9 = {0: ['9']}

@pytest.mark.parametrize(
    "input_data,expected_output",
    [
        pytest.param(
            in_line_test_1,
            in_line_test_solution1,
            id="in_line_test_1",
        ),
        pytest.param(
            in_line_test_2,
            in_line_test_solution2,
            id="in_line_test_2",
        ),
        pytest.param(
            in_line_test_3,
            in_line_test_solution3,
            id="in_line_test_3",
        ),
        pytest.param(
            in_line_test_4,
            in_line_test_solution4,
            id="in_line_test_4",
        ),
        pytest.param(
            in_line_test_5,
            in_line_test_solution5,
            id="in_line_test_5",
        ),
        pytest.param(
            in_line_test_6,
            in_line_test_solution6,
            id="in_line_test_6",
        ),
        pytest.param(
            in_line_test_7,
            in_line_test_solution7,
            id="in_line_test_7",
        ),
        pytest.param(
            in_line_test_8,
            in_line_test_solution8,
            id="in_line_test_8",
        ),
        pytest.param(
            in_line_test_9,
            in_line_test_solution9,
            id="in_line_test_9",
        ),
    ],
)
def test_in_line_positions(input_data: str, expected_output: dict) -> None:
    assert test_module.check_machineids_near_gears_in_line(input_data) == expected_output


in_line_test_1 =       "617*......"
adjacent_line_test_1 = "467..114.."
in_line_test_1_gear_pos_solutions = {3: ['617', '467']}

in_line_test_2 =       ".17*......"
adjacent_line_test_2 = "...5.114.."
in_line_test_2_gear_pos_solutions = {3: ['17', '5']}

in_line_test_3 =       ".17*......"
adjacent_line_test_3 = "....5.114."
in_line_test_3_gear_pos_solutions = {3: ['17', '5']}

in_line_test_4 =       ".........*"
adjacent_line_test_4 = "......114."
in_line_test_4_gear_pos_solutions = {9: ['114']}

in_line_test_5 =       ".....12*.."
adjacent_line_test_5 = "......114."
in_line_test_5_gear_pos_solutions = {7: ['12','114']}

in_line_test_6 =       ".17*......"
adjacent_line_test_6 = "..5...114."
in_line_test_6_gear_pos_solutions = {3: ['17', '5']}

in_line_test_7 =       "..17*....."
adjacent_line_test_7 = ".51....114"
in_line_test_7_gear_pos_solutions = {4: ['17']}


@pytest.mark.parametrize(
    "middle_line, adjacent_line, expected_output",
    [
        pytest.param(
            in_line_test_1,
            adjacent_line_test_1,
            in_line_test_1_gear_pos_solutions,
            id="in_line_test_1_gear_pos_solutions",
        ),
        pytest.param(
            in_line_test_2,
            adjacent_line_test_2,
            in_line_test_2_gear_pos_solutions,
            id="in_line_test_2_gear_pos_solutions",
        ),
        pytest.param(
            in_line_test_3,
            adjacent_line_test_3,
            in_line_test_3_gear_pos_solutions,
            id="in_line_test_3_gear_pos_solutions",
        ),
        pytest.param(
            in_line_test_4,
            adjacent_line_test_4,
            in_line_test_4_gear_pos_solutions,
            id="in_line_test_4_gear_pos_solutions",
        ),
        pytest.param(
            in_line_test_5,
            adjacent_line_test_5,
            in_line_test_5_gear_pos_solutions,
            id="in_line_test_5_gear_pos_solutions",
        ),
        pytest.param(
            in_line_test_6,
            adjacent_line_test_6,
            in_line_test_6_gear_pos_solutions,
            id="in_line_test_6_gear_pos_solutions",
        ),
        pytest.param(
            in_line_test_7,
            adjacent_line_test_7,
            in_line_test_7_gear_pos_solutions,
            id="in_line_test_7_gear_pos_solutions",
        ),
    ],
)
def test_in_adjacent_line_positions(middle_line: str, adjacent_line: str, expected_output: dict) -> None:
    gear_positions = test_module.check_machineids_near_gears_in_line(middle_line)
    adjacent_machine_ids = test_module.get_machine_ids_in_adjacent_line(adjacent_line, list(gear_positions.keys()))
    for gpos, ids in adjacent_machine_ids.items():
        gear_positions[gpos].extend(ids)

    assert gear_positions == expected_output
