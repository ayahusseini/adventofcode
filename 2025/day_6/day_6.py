"""Solution to advent of code day 6 2025"""

import re
import numpy as np
import operator as op

INPUT_FILE = "inputs/day_6_input.txt"
TEST_FILE = "inputs/day_6_test_input.txt"

OPERATORS = {"+": op.add, "*": op.mul}


def load_file(filename: str, sep_all_chars: bool = False):
    """Load the puzzle input, returning stripped lines."""
    nums = []
    with open(filename, "r") as f:
        for l in f:
            if set(["+", "-", "*", "/"]).intersection(set(l.strip())):
                operator = re.sub(r"\s+", " ", l.strip()).split(" ")
            elif l.strip():
                if sep_all_chars:
                    cleaned = list(l.replace("\n", ""))
                else:
                    cleaned = re.sub(r"\s+", " ", l.strip()).split(" ")
                nums.append([int(char) if char.strip() else np.nan for char in cleaned])

    return operator, np.array(nums)


def combine_list(
    row: np.ndarray, operator: str, operator_mapping: dict = OPERATORS
) -> int:
    """Return the combination of a row according to operator"""
    if len(row) == 0:
        return 0

    op = operator_mapping[operator]
    tot = row[0]
    if len(row) == 1:
        return tot

    for r in row[1:]:
        tot = op(tot, r)
    return tot


def one_star(filename: str):
    """Solve part 1 for day 6."""
    ops, nums = load_file(filename)
    nums = nums.T
    tot = 0
    for idx, col in enumerate(nums):
        o = ops[idx]
        tot += combine_list(col, o)

    return tot


def two_star(filename: str):
    """Solve part 2 for day 6."""
    ops, nums = load_file(filename, sep_all_chars=True)
    nums = nums.T
    operator_idx = 0
    tot = 0
    curr_nums = []
    for col in nums:
        o = ops[operator_idx]

        if np.all(np.isnan(col)):
            tot += combine_list(curr_nums, o)
            operator_idx += 1
            curr_nums = []
            continue

        num = int("".join(str(int(digit)) for digit in col if not np.isnan(digit)))

        curr_nums.append(num)

    tot += combine_list(curr_nums, o)
    return tot


if __name__ == "__main__":
    print(f"One star test solution is {one_star(TEST_FILE)}")
    print(f"Two star test solution is {two_star(TEST_FILE)}")
    print(f"One star solution is {one_star(INPUT_FILE)}")
    print(f"Two star solution is {two_star(INPUT_FILE)}")
