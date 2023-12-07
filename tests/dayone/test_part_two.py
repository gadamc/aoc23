from pathlib import Path
from typing import Iterator

import pytest

from aoc23.dayone.part_two import solution

_input_data = (Path(__file__).parent / "data.dat").open().readlines()
_example_data = """
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen""".strip().splitlines()


@pytest.mark.parametrize(
    "input_data,expected_output",
    [
        pytest.param(
            _example_data,
            281,
            id="example data",
        ),
        pytest.param(
            _input_data,
            54530,
            id="challenge data",
        ),
    ],
)
def test_runner(input_data: Iterator[str], expected_output: int) -> None:
    assert solution(input_data) == expected_output
