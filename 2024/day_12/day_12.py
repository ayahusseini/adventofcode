'''Solution to advent of code day 12 2024
'''

INPUT_FILE = "inputs/day_12_input.txt"
TEST_FILE = "inputs/day_12_test_input.txt"


def load_file(filename: str) -> dict[tuple, str]:
    """Loads the file as a dictionary mapping positions to letters"""
    with open(filename, "r") as f:
        positions = read_lines(f)
    return positions


def read_lines(lines: list[str]) -> dict[tuple, str]:
    """Converts a list of strings into a map between positions and letters"""
    positions = dict()
    for r, line in enumerate(lines):
        for c, char in enumerate(line.strip()):
            positions[(r, c)] = char
    return positions


def get_neighbours(idx: tuple, cache: dict = dict():
    """Returns the neighbours of an index"""


def one_star(filename: str):
    '''Returns the one star solution'''
    lines = load_file(filename)

    return


def two_star(filename: str):
    '''Returns the two star solution'''

    return


if __name__ == "__main__":
    print(f"One star test solution is {one_star(TEST_FILE)}")
    print(f"Two star test solution is {two_star(TEST_FILE)}")
    print(f"One star solution is {one_star(INPUT_FILE)}")
    print(f"Two star solution is {two_star(INPUT_FILE)}")
