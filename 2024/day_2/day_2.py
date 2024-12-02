'''Solution to advent of code day 2 2024
'''
from collections import defaultdict

INPUT_FILE = "inputs/day_2_input.txt"
TEST_FILE = "inputs/day_2_test_input.txt"


def load_file(filename: str) -> list[int]:
    '''Loads the file as two lists of integers'''
    with open(filename, "r") as f:
        lines = f.readlines()


def one_star(filename: str):
    '''Returns the one star solution'''


def two_star(filename: str):
    '''Returns the two star solution'''


if __name__ == "__main__":
    print(f"One star test solution is {one_star(TEST_FILE)}")
    print(f"Two star test solution is {two_star(TEST_FILE)}")
    print(f"One star solution is {one_star(INPUT_FILE)}")
    print(f"Two star solution is {two_star(INPUT_FILE)}")
