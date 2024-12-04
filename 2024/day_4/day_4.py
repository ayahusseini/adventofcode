'''Solution to advent of code day 4 2024
'''
import numpy as np
from collections import defaultdict, namedtuple

INPUT_FILE = "inputs/day_4_input.txt"
TEST_FILE = "inputs/day_4_test_input.txt"


Word = namedtuple('Word', ['orientation', 'word', 'is_backwards'])


class WordSearch:
    """Word search class"""
    __directions = [(1, 1), (1, -1), (-1, 1), (-1, -1),
                    (1, 0), (-1, 0), (0, 1), (0, -1)]

    def __init__(self, lines: list[list]):
        """Instantiates a word search object"""
        self.lines = np.array(lines)
        self.nrows = self.lines.shape[0]
        self.ncols = self.lines.shape[1]

    def count_target(self, target) -> int:
        """Finds the number of times a target word appears in lines"""
        # find the first letter of the target word
        start_letter = np.where(self.lines == target[0])

        if len(target) == 1:
            return len(start_letter)

        stack = [(r, c, 0, None) for r, c in zip(*start_letter)]
        count = 0

        while stack:
            row, col, letteridx, direction = stack.pop()
            if direction is None:
                for d in WordSearch.__directions:
                    dr, dc = d
                    if 0 <= row + dr < self.nrows and 0 <= col + dc < self.ncols:
                        if self.lines[row + dr, col + dc] == target[1]:
                            stack.append((row + dr, col + dc, 1, d))
            elif letteridx < len(target) - 1:
                dr, dc = direction
                if 0 <= row + dr < self.nrows and 0 <= col + dc < self.ncols and self.lines[row + dr, col + dc] == target[letteridx + 1]:
                    stack.append((row + dr, col + dc, letteridx+1, direction))
            elif letteridx == len(target) - 1:
                count += 1

        return count

    def __str__(self) -> str:
        """Returns a string representation of the lines"""
        return '\n'.join(''.join(row) for row in self.lines)


def load_file(filename: str) -> WordSearch:
    '''Loads the file'''
    with open(filename, "r") as f:
        lines = f.readlines()

    return WordSearch([list(l.replace('\n', '')) for l in lines if l])


def one_star(filename: str):
    '''Returns the one star solution'''
    ws = load_file(filename)
    return ws.count_target('XMAS')


def two_star(filename: str):
    '''Returns the two star solution'''
    return


if __name__ == "__main__":
    print(f"One star test solution is {one_star(TEST_FILE)}")
    print(f"Two star test solution is {two_star(TEST_FILE)}")
    print(f"One star solution is {one_star(INPUT_FILE)}")
    print(f"Two star solution is {two_star(INPUT_FILE)}")
