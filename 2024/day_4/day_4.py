'''Solution to advent of code day 4 2024
'''
import numpy as np
from collections import defaultdict, namedtuple

INPUT_FILE = "inputs/day_4_input.txt"
TEST_FILE = "inputs/day_4_test_input.txt"


Word = namedtuple('Word', ['orientation', 'word', 'is_backwards'])


class WordSearch:
    """Word search class"""

    def __init__(self, lines: list[list]):
        """Instantiates a word search object"""
        self.lines = np.array(lines)
        self.nrows = self.lines.shape[0]

    def count_target(self, target) -> int:
        """Finds the number of times a target word appears in lines"""
        # find the first letter of the target word
        start_letter = np.where(self.lines == target[0])
        stack = [np.unravel_index(s,)]

    def __str__(self) -> str:
        """Returns a string representation of the lines"""


def load_file(filename: str) -> WordSearch:
    '''Loads the file'''
    with open(filename, "r") as f:
        lines = f.readlines()
    print(lines)
    return WordSearch([list(l.replace('\n', '')) for l in lines if l])


def one_star(filename: str):
    '''Returns the one star solution'''

    return


def two_star(filename: str):
    '''Returns the two star solution'''
    return


if __name__ == "__main__":
    ws = load_file(TEST_FILE)
    print(str(ws))
    # print(f"One star test solution is {one_star(TEST_FILE)}")
    # print(f"Two star test solution is {two_star(TEST_FILE)}")
    # print(f"One star solution is {one_star(INPUT_FILE)}")
    # print(f"Two star solution is {two_star(INPUT_FILE)}")
