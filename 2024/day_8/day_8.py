
import numpy as np
from collections import defaultdict
INPUT_FILE = "inputs/day_6_input.txt"
TEST_FILE = "inputs/day_6_test_input.txt"


class Grid:
    def __init__(self, obstructions: dict, nrows: int, ncols: int):
        """Instantiates a grid."""
        self.obstructions_row = obstructions
        self.temporary_obstructions = set()
        self.nrows = nrows
        self.ncols = ncols

    def reset(self):
        """Resets any temporary obstructions."""
        for o in self.temporary_obstructions:
            self.obstructions_row[o[0]].remove(o[1])
        self.temporary_obstructions.clear()

    def add_temporary_obstruction(self, idx: tuple):
        """Adds a temporary obstruction."""
        self.temporary_obstructions.add(idx)
        self.obstructions_row[idx[0]].append(idx[1])

    def is_out_of_bounds(self, idx: tuple) -> bool:
        """Whether or not an index is out of bounds."""
        return not (0 <= idx[0] < self.nrows and 0 <= idx[1] < self.ncols)

    def is_obstacle(self, idx: tuple) -> bool:
        """Whether or not an index contains an obstacle."""
        return idx[1] in self.obstructions_row[idx[0]]


class Guard:
    _turns = {'^': '>', '>': 'v', '<': '^', 'v': '<'}
    _orientations = {'^': (-1, 0), '>': (0, 1), '<': (0, -1), 'v': (1, 0)}

    def __init__(self, grid: Grid, position: tuple, symbol: tuple):
        """Instantiates a guard"""
        self.grid = grid
        self.path = [(position, symbol)]

    def turn(self):
        """Turn to the right by 90 degrees"""
        self.path.append((self.path[-1][0], Guard._turns[self.path[-1][1]]))

    def walk(self) -> int:
        """Walk forward, returning the number of steps taken (or -1 if stepping out of bounds)."""
        pos, symbol = self.path[-1]
        d = Guard._orientations[symbol]
        next_pos = (pos[0] + d[0], pos[1] + d[1])

        if self.grid.is_out_of_bounds(next_pos):
            return -1
        if self.grid.is_obstacle(next_pos):
            self.turn()
            return 0
        self.path.append((next_pos, symbol))
        return 1

    def simulate_walk_out_of_bounds(self) -> bool:
        """Keep walking until out of bounds"""
        steps = 0
        while steps >= 0:
            steps = self.walk()

    def detect_loop(self) -> bool:
        """Return True if a loop is detected."""
        visited = set()
        while True:
            current_state = self.path[-1]
            if current_state in visited:
                return True
            visited.add(current_state)
            if self.walk() == -1:
                return False

    def count_distinct_positions(self) -> int:
        """Counts the number of distinct positions visited"""
        return len(set([pos for pos, _ in self.path]))


def load_file(filename: str) -> Guard:
    """Loads a file as a guard"""
    with open(filename, 'r') as f:
        lines = f.readlines()

    obstructions = defaultdict(lambda: [])

    for row, l in enumerate(lines):
        l = l.replace('\n', '')
        for col, char in enumerate(l):
            if char == '#':
                obstructions[row].append(col)
            elif char in ('>', '<', '^', 'v'):
                initial_position = row, col
                symbol = char

    grid = Grid(obstructions, len(
        lines), len(lines[0].replace('\n', '')))
    return Guard(grid, initial_position, symbol)


def one_star(filename: str):
    '''Returns the one star solution'''
    guard = load_file(filename)
    guard.simulate_walk_out_of_bounds()
    return guard.count_distinct_positions()


def two_star(filename: str):
    '''Returns the two star solution'''
    guard = load_file(filename)
    guard.simulate_walk_out_of_bounds()
    original_positions = set([pos for pos, _ in guard.path[1:]])
    count = 0
    for pos in list(original_positions):
        guard.grid.reset()
        guard.path = [guard.path[0]]
        guard.grid.add_temporary_obstruction(pos)
        if guard.detect_loop():
            count += 1
    return count


if __name__ == "__main__":
    print(f"One star test solution is {one_star(TEST_FILE)}")
    print(f"Two star test solution is {two_star(TEST_FILE)}")
    print(f"One star solution is {one_star(INPUT_FILE)}")
    print(f"Two star solution is {two_star(INPUT_FILE)}")
