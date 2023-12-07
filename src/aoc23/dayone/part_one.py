import re
from typing import Iterator


def get_number_from_line(line):
    # Perform operations on each line here

    numbers = re.findall(r'[0-9]', line)
    first_number = int(numbers[0])
    last_number = int(numbers[-1])
    return first_number * 10 + last_number


def solution(lines: Iterator[str]) -> int:
    return sum(get_number_from_line(line) for line in lines)


# with open(file_path, "r") as file:
#     count = 0
#     for line in file:
#         #print(line.strip())
#         val2 = get_nums2(line.strip())
#         val3 = get_nums3(line.strip())
#         # if val2 != val3:
#         #     print(line.strip())
#         #     print(f'val2: {val2}, val3: {val3}')
#         #     input()
#         #print(val)
#         count += val3
#         #input()
# print(count)
