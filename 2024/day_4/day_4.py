'''Solution to advent of code day 4 2024
'''
import numpy as np
from collections import defaultdict, namedtuple

INPUT_FILE = "inputs/day_4_input.txt"
TEST_FILE = "inputs/day_4_test_input.txt"


Word = namedtuple('Word', ['orientation', 'word', 'is_backwards'])


class WordSearch:
    """Word search class"""
    diagonal = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    horizontal = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    all_directions = diagonal + horizontal

    def __init__(self, lines: list[list]):
        """Instantiates a word search object"""
        self.lines = np.array(lines)
        self.nrows = self.lines.shape[0]
        self.ncols = self.lines.shape[1]

    def _is_index_valid(self, row: int, col: int) -> bool:
        """Returns True if an index is within the array"""
        return 0 <= row < self.nrows and 0 <= col < self.ncols

    def _is_next_letter(self, row: int, col: int, direction: tuple, nextletter: str) -> bool:
        """Returns True if moving in a direction gives the correct next letter"""
        nr, nc = row + direction[0], col + direction[1]
        return self._is_index_valid(nr, nc) and self.lines[nr, nc] == nextletter

    def find_target(self, target: str, directions: list[tuple]) -> list:
        """Finds the start index and direction where a target word appears in some lines"""

        if not target:
            raise ValueError("Target must be at least one letter")

        start_letter = np.where(self.lines == target[0])

        if len(target) == 1:
            return [(r, c, None) for r, c in zip(*start_letter)]

        stack = [(r, c, 0, None) for r, c in zip(*start_letter)]
        indeces = []

        while stack:

            r, c, letteridx, change = stack.pop()

            if change is None:
                for d in directions:
                    if self._is_next_letter(r, c, d, target[1]):
                        stack.append((r + d[0], c + d[1], 1, d))

            elif letteridx < len(target) - 1:
                expected = target[letteridx + 1]
                if self._is_next_letter(r, c, change, expected):
                    stack.append(
                        (r + change[0], c + change[1], letteridx+1, change))

            elif letteridx == len(target) - 1:
                indeces.append([r, c, change])

        return indeces

    def count_target(self, word: str, allowed_directions: list[tuple]) -> int:
        """Finds the number of times a target word appears in lines"""

        return len(self.find_target(word, allowed_directions))

    def count_crosses(self, word: str):
        """Counts the number of times a target word appears in a crossed pattern"""

        last_letter = self.find_target(word, directions=WordSearch.diagonal)

        if len(word) % 2 == 0:
            raise ValueError(
                "The target word must have an odd number of letters")
        steps = len(word) // 2

        middles = set()

        count = 0

        for r, c, change in last_letter:

            centre = (r - change[0] * steps,
                      c - change[1] * steps)
            if centre in middles:
                count += 1
            else:
                middles.add(centre)

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
    return ws.count_target('XMAS', allowed_directions=WordSearch.all_directions)


def two_star(filename: str):
    '''Returns the two star solution'''
    ws = load_file(filename)
    return ws.count_crosses('MAS')


if __name__ == "__main__":
    print(f"One star test solution is {one_star(TEST_FILE)}")
    print(f"Two star test solution is {two_star(TEST_FILE)}")
    print(f"One star solution is {one_star(INPUT_FILE)}")
    print(f"Two star solution is {two_star(INPUT_FILE)}")
