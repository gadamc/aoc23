from pathlib import Path

import pytest

import aoc23.dayfour.part_one as test_module

_challenge_data = (Path(__file__).parent / "data.dat").open().readlines()
_challenge_solution = 17782

_example_data = """
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11""".strip().splitlines()
_example_solution = 13


@pytest.mark.parametrize(
    "input_data,expected_output",
    [
        pytest.param(
            _example_data,
            _example_solution,
            id="example",
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
