from pathlib import Path

import pytest

from aoc23.daythree.part_one import solution

_challenge_data = (Path(__file__).parent / "data.dat").open().read()
_challenge_solution = 529618

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
_example_solution = 4361
# sum of the part numbers.
# part numbers are any number in the text that is adjacent, including diagonally,
# to a symbol other than a "."
# only 58 and 114 are NOT part numbers.

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
_test2_solution = 4361

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
    assert solution(input_data) == expected_output
