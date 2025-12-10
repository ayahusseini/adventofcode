"""Solution to advent of code day 3 2025"""

from math import remainder


INPUT_FILE = "inputs/day_3_input.txt"
TEST_FILE = "inputs/day_3_test_input.txt"


def load_file(filename: str) -> list[list[int]]:
    """Load the puzzle input, yielding stripped lines."""
    with open(filename, "r") as f:
        return [[int(char) for char in line.strip()]
                for line in f if line.strip()]


def get_next_digit(idx: int, bank: list[int], leave_room: int) -> tuple[int, int]:
    """Get the next highest digit from bank, starting from idx 
    leave_room is how much room to leave at the end for remaining digits. 
    Returns the next digit and its index
    """
    options = bank[idx:len(bank) - leave_room]
    nextdigit = max(options)
    for j, digit in enumerate(options):
        if nextdigit == digit:
            return idx + j, digit


def get_largest_num(ndigits: int, all_digits: list[int]) -> int:
    """Get the largest number that can be formed of ndigits, 
    selected in the order they appear from bank
    """
    digits = ""
    curridx = 0
    while len(digits) < ndigits:
        to_choose = ndigits - len(digits)
        curridx, digit = get_next_digit(curridx, all_digits, to_choose - 1)
        digits += str(digit)
        curridx += 1
    return int(digits)


def one_star(filename: str):
    """Solve part 1 for day 3."""
    banks = load_file(filename)
    return sum([get_largest_num(2, b) for b in banks])


def two_star(filename: str):
    """Solve part 2 for day 3."""
    return


if __name__ == "__main__":
    print(f"One star test solution is {one_star(TEST_FILE)}")
    print(f"Two star test solution is {two_star(TEST_FILE)}")
    print(f"One star solution is {one_star(INPUT_FILE)}")
    print(f"Two star solution is {two_star(INPUT_FILE)}")
