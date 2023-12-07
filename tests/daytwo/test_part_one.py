from pathlib import Path
from typing import Iterator

import pytest

from aoc23.daytwo.part_one import solution

_challenge_data = (Path(__file__).parent / "data.dat").open().readlines()
_challenge_solution = 1931

_example_data = """
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green""".strip().splitlines()
_example_solution = 8


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
def test_runner(input_data: Iterator[str], expected_output: int) -> None:
    assert solution(input_data) == expected_output
