"""Solution to advent of code day 8 2015"""

import re

INPUT_FILE = "inputs/day_8_input.txt"
TEST_FILE = "inputs/day_8_test_input_2.txt"


def load_file(filename: str) -> list[int]:
    """Loads the file as a list of strings.
    The outer quotations are removed."""

    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    return [l.replace("\n", "").replace(" ", "")[1:-1] for l in lines]


def get_num_characters_of_string(text: str) -> int:
    """Return the number of characters in the string data"""
    return len(text.encode("utf-8").decode("unicode-escape"))


def get_num_characters_of_code(text: str) -> int:
    """Return the number of characters of code for a string literal"""
    return len(text) + 2


def num_characters_of_code_after_encoding(text: str) -> int:
    """Return the number of characters after encoding twice"""
    return len(repr(text)) + 4 + repr(text).count('"')


def one_star(filename: str):
    """Returns the one star solution"""
    lines = load_file(filename)
    return sum(
        [
            get_num_characters_of_code(line) - get_num_characters_of_string(line)
            for line in lines
        ]
    )


def two_star(filename: str):
    """Returns the two star solution"""
    lines = load_file(filename)

    return sum(
        [
            num_characters_of_code_after_encoding(line)
            - get_num_characters_of_code(line)
            for line in lines
        ]
    )


if __name__ == "__main__":
    print(f"One star solution is {one_star(TEST_FILE)}")
    print(f"Two star solution is {two_star(TEST_FILE)}")
    print(f"One star solution is {one_star(INPUT_FILE)}")
    print(f"Two star solution is {two_star(INPUT_FILE)}")
