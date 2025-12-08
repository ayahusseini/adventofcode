"""Solution to advent of code day 1 2025"""
import regex as re

INPUT_FILE = "inputs/day_2_input.txt"
TEST_FILE = "inputs/day_2_test_input.txt"


def is_repeated_twice(id: int) -> bool:
    """Return True if an id contains a sequence of digits repeated twice"""
    txt = str(id)
    # immediately filter out cases with non-even lengths
    if len(txt) % 2 != 0:
        return False
    substring_length = len(txt) // 2
    return txt[:substring_length] == txt[substring_length:]


def get_multiples_of_11(s: int, e: int):
    """Return the multiples of 11 within a range [s,e] - inclusive"""
    curr = 11 * (s//11 + 1) if s % 11 != 0 else ...


def parse_range(range_str: str) -> tuple[int, int]:
    """Returnt the first and last IDs in a range"""
    nums = range_str.split('-')
    return int(nums[0]), int(nums[1])


def load_file(filename: str) -> list[str]:
    """Loads the file"""
    with open(filename, "r") as f:
        ranges = f.readline().replace("\n", "").replace(" ", "").split(',')
    for r in ranges:
        yield parse_range(r)


def one_star(filename: str):
    """Returns the one star solution"""
    sum = 0
    for rng in load_file(filename):
        print(f'rng = {rng}')
        for id in range(*rng):
            if is_repeated_twice(id):
                print(f'id {id} is invalid')
                sum += id
    return sum


def two_star(filename: str):
    """Returns the two star solution"""
    return


if __name__ == "__main__":
    print(f"One star test solution is {one_star(TEST_FILE)}")
    print(f"Two star test solution is {two_star(TEST_FILE)}")
    print(f"One star solution is {one_star(INPUT_FILE)}")
    print(f"Two star solution is {two_star(INPUT_FILE)}")
