'''Solution to advent of code day 6 2024
'''
import numpy as np
INPUT_FILE = "inputs/day_6_input.txt"
TEST_FILE = "inputs/day_6_test_input.txt"


class Grid:
    def __init__(self, is_obstruction: np.ndarray):
        self.obstructions = is_obstruction
        self.nrows = len(is_obstruction)
        self.ncols = len(is_obstruction[0])

    def is_out_of_bounds(self, idx: tuple) -> bool:
        return (not (0 <= idx[0] < self.nrows) or not (0 <= idx[1] < self.ncols))

    def is_obstacle(self, idx: tuple) -> bool:
        return self.obstructions[idx[0], idx[1]]


class Guard:
    _turns = {'^': '>',
              '>': 'v',
              '<': '^',
              'v': '<'}

    _orientations = {
        '^': (-1, 0),
        '>': (0, 1),
        '<': (0, -1),
        'v': (1, 0)
    }

    def __init__(self, grid: Grid, position: tuple, symbol: tuple):
        self.grid = grid
        self.visited = np.zeros_like(self.grid.obstructions, dtype=int)

        self.r, self.c = position
        self.visited[self.r, self.c] = True  # visit initial position

        self.symbol = symbol
        self.dr, self.dc = Guard._orientations[symbol]

    def turn(self) -> bool:
        """Turn to the right by 90 degrees"""
        self.symbol = Guard._turns[self.symbol]
        self.dr, self.dc = Guard._orientations[self.symbol]

    def walk(self) -> bool:
        """Walk forward to the next obstacle or until leaving bounds. 
        Returns True if still in bounds."""
        next_pos = (self.r + self.dr, self.c + self.dc)
        if self.grid.is_out_of_bounds(next_pos):
            return False

        if self.grid.is_obstacle(next_pos):
            self.turn()
        else:
            self.r, self.c = next_pos
            self.visited[self.r, self.c] = True
        return True

    def simulate_walk_out_of_bounds(self) -> bool:
        """Keep walking until out of bounds"""
        in_bounds = True
        while in_bounds:
            in_bounds = self.walk()

    def count_distinct_positions(self) -> int:
        """Counts the number of distinct positions visited"""
        return int(self.visited.sum())

    @classmethod
    def from_lines(cls, lines: list[str]):
        obstructions = np.array(
            [[char == '#' for char in line.replace('\n', '')] for line in lines])
        grid = Grid(obstructions)

        for r, row in enumerate(lines):
            for o in cls._orientations.keys():
                c = row.find(o)
                if c > -1:
                    return cls(grid, (r, c), o)


def load_file(filename: str) -> Guard:
    """Loads a file as a guard"""
    with open(filename, 'r') as f:
        lines = f.readlines()

    return Guard.from_lines(lines)


def one_star(filename: str):
    '''Returns the one star solution'''
    guard = load_file(filename)
    guard.simulate_walk_out_of_bounds()
    return guard.count_distinct_positions()


def two_star(filename: str):
    '''Returns the two star solution'''

    return


if __name__ == "__main__":
    print(f"One star test solution is {one_star(TEST_FILE)}")
    print(f"Two star test solution is {two_star(TEST_FILE)}")
    print(f"One star solution is {one_star(INPUT_FILE)}")
    print(f"Two star solution is {two_star(INPUT_FILE)}")
