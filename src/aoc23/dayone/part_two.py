import re
from typing import Iterator

valid_strings = {'zero': 0,
                 'one': 1,
                 'two': 2,
                 'three': 3,
                 'four': 4,
                 'five': 5,
                 'six': 6,
                 'seven': 7,
                 'eight': 8,
                 'nine': 9}

valid_strings = valid_strings | {str(i): i for i in range(10)}
pattern = '|'.join(valid_strings.keys())


def _wrong_solution(line: str) -> int:
    # Perform operations on each line here

    numbers = re.findall(pattern, line)
    first_number = valid_strings[numbers[0]]
    last_number = valid_strings[numbers[-1]]
    return first_number * 10 + last_number


_regex = re.compile(pattern)


def generate_all_valid_numbers(input_line: str) -> Iterator[str]:
    for i in range(len(input_line)):
        if not (val := _regex.search(input_line[i:])):
            return
        yield val.group(0)


def get_number_from_line(input_line: str) -> int:

    numbers = list(generate_all_valid_numbers(input_line))
    first_number = valid_strings[numbers[0]]
    if len(numbers) == 1:
        last_number = first_number
    else:
        last_number = valid_strings[numbers[-1]]
    return first_number * 10 + last_number


def solution(lines: Iterator[str]) -> int:
    return sum(get_number_from_line(line) for line in lines)
