'''Solution to advent of code day 7 2023
'''
from collections import defaultdict

INPUT_FILE = "inputs/day_7_input.txt"
TEST_FILE = "inputs/day_7_test_input.txt"


def load_file(filename: str) -> list:
    '''Loads the file as '''

    with open(filename, "r") as f:
        lines = f.readlines()


def one_star(filename: str) -> int:
    '''Returns the one star solution'''
    reports = load_file(filename)
    return sum([r.is_safe() for r in reports])


def two_star(filename: str):
    '''Returns the two star solution'''
    reports = load_file(filename)
    return sum([r.is_safe_with_removal() for r in reports])


if __name__ == "__main__":
    print(f"One star test solution is {one_star(TEST_FILE)}")
    print(f"Two star test solution is {two_star(TEST_FILE)}")
    print(f"One star solution is {one_star(INPUT_FILE)}")
    print(f"Two star solution is {two_star(INPUT_FILE)}")
