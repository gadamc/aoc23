from pathlib import Path
from typing import Iterator

import pytest

from aoc23.dayone.part_one import solution

_input_path = (Path(__file__).parent / "data.dat")
print(_input_path)
_input_data = _input_path.open().readlines()
_example_data = """
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet""".strip().splitlines()


@pytest.mark.parametrize(
    "input_data,expected_output",
    [
        pytest.param(
            _example_data,
            142,
            id="example data",
        ),
        pytest.param(
            _input_data,
            56049,
            id="challenge data",
        ),
    ],
)
def test_runner(input_data: Iterator[str], expected_output: int) -> None:
    assert solution(input_data) == expected_output
