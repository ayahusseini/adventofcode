'''Solution to advent of code day 4 2024
'''
from collections import defaultdict
import re

INPUT_FILE = "inputs/day_4_input.txt"
TEST_FILE = "inputs/day_4_test_input.txt"


def extract_multiplication_instructions(memory: str) -> list[tuple[str, str]]:
    """Returns a list of multiplication instructions as a list of tuples
    to multiply"""
    return re.findall(r"mul\((\d+),(\d+)\)", memory)


def load_file(filename: str) -> list[int]:
    '''Loads the file and returns a list of multiplication instructions'''
    with open(filename, 'r') as f:
        instructions = extract_multiplication_instructions(f.read())
    return instructions


def one_star(filename: str):
    '''Returns the one star solution'''


def two_star(filename: str):
    '''Returns the two star solution'''


if __name__ == "__main__":
    print(f"One star test solution is {one_star(TEST_FILE)}")
    print(f"Two star test solution is {two_star(TEST_FILE)}")
    print(f"One star solution is {one_star(INPUT_FILE)}")
    print(f"Two star solution is {two_star(INPUT_FILE)}")
