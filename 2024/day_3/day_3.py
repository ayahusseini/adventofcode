'''Solution to advent of code day 3 2024
'''
from collections import defaultdict
import re

INPUT_FILE = "inputs/day_3_input.txt"
TEST_FILE = "inputs/day_3_test_input.txt"
TEST_FILE2 = "inputs/day_3_test_input2.txt"

MULTIPLICATION_PATTERN = r"mul\((\d+),(\d+)\)"
CONDITIONAL_MULTIPLICATION_PATTERN = r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))"


def extract_multiplication_instructions(memory: str, pattern: str) -> list[tuple]:
    """Returns a list of multiplication instructions as a list of tuples
    to multiply"""
    return re.findall(pattern, memory)


def read_conditional_instructions(instructions: list[tuple]) -> int:
    """Reads the conditional instructions"""
    multiplier = 1
    total = 0
    for match in instructions:
        if any(match):
            if match[0] and match[1]:
                total += multiplier * int(match[0]) * int(match[1])
            elif match[2]:
                multiplier = 1
            elif match[3]:
                multiplier = 0
    return total


def load_file(filename: str, extraction_pattern: str = r"mul\((\d+),(\d+)\)") -> list[int]:
    '''Loads the file and returns a list of multiplication instructions'''
    with open(filename, 'r') as f:
        instructions = extract_multiplication_instructions(
            f.read(), extraction_pattern)
    return instructions


def one_star(filename: str):
    '''Returns the one star solution'''
    instructions = load_file(filename)
    return sum([int(x)*int(y) for x, y in instructions])


def two_star(filename: str):
    '''Returns the two star solution'''
    instructions = load_file(filename)
    return read_conditional_instructions(instructions)


if __name__ == "__main__":
    print(f"One star test solution is {one_star(TEST_FILE)}")
    print(f"Two star test solution is {two_star(TEST_FILE2)}")
    print(f"One star solution is {one_star(INPUT_FILE)}")
    print(f"Two star solution is {two_star(INPUT_FILE)}")
