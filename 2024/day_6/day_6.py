import numpy as np
from collections import defaultdict
INPUT_FILE = "inputs/day_6_input.txt"
TEST_FILE = "inputs/day_6_test_input.txt"


def load_file(filename: str) -> Guard:
    """Loads a file as a guard"""
    with open(filename, 'r') as f:
        lines = f.readlines()

    obstructions = defaultdict(lambda: [])
    obstructionsT = defaultdict(lambda: [])

    for row, l in enumerate(lines):
        l = l.replace('\n', '')
        for col, char in enumerate(l):
            if char == '#':
                obstructions[row].append(col)
                obstructionsT[col].append(row)
            elif char in ('>', '<', '^', 'v'):
                initial_position = row, col
                symbol = char

    return Grid(obstructions, obstructionsT, len(lines), len(lines[0].replace('\n', '')))


class Grid:
    def __init__(self, obstructions: dict, obstructions_T: dict, nrows: int, ncols: int):
        """Instantiates a grid."""
        self.obstructions_row = obstructions
        self.obstructions_col = obstructions_T
        self.nearest = defaultdict(lambda: dict())

        self.temporary_obstructions = set()
        self.nrows = nrows
        self.ncols = ncols

    def get_nearest_obstruction(self, idx: tuple, direction: tuple) -> list:
        """Returns the nearest obstructions for the up, down, left, right orientations"""

        if self.nearest[idx].get(direction) is not None:
            return self.nearest[idx][direction]
        r, c = idx
        up, left = direction
        if up == 0:
            nearest_col = min(
                self.obstructions_row[r], key=lambda x: left * (c - x))

            self.nearest[idx][direction] = r, nearest_col
            return r, nearest_col
        elif left == 0:
            nearest_row = min(
                self.obstructions_col[c], key=lambda x: up * (r - x))
            self.nearest[idx][direction] = nearest_row, c
            return nearest_row, c

    def reset(self):
        """Resets any temporary obstructions."""
        self.temporary_obstrcutions.clear()

    def add_temporary_obstruction(self, idx: tuple):
        """Adds a temporary obstruction."""
        self.temporary_obstructions.add(idx)

    def is_out_of_bounds(self, idx: tuple) -> bool:
        """Whether or not an index is out of bounds."""
        return not (0 <= idx[0] < self.nrows and 0 <= idx[1] < self.ncols)

    def is_obstacle(self, idx: tuple) -> bool:
        """Whether or not an index contains an obstacle."""
        return idx in self.temporary_obstructions or idx[1] in self.obstructions[idx[0]]


class Guard:
    _turns = {'^': '>', '>': 'v', '<': '^', 'v': '<'}
    _orientations = {'^': (-1, 0), '>': (0, 1), '<': (0, -1), 'v': (1, 0)}

    def __init__(self, grid: Grid, position: tuple, symbol: tuple):
        """Instantiates a guard"""
        self.grid = grid
        self.pos = position
        self.visited = {(position)}

        self.symbol = symbol
        self.original_state = (self.symbol, self.pos)

    def reset(self):
        """Reset the guard state"""
        self.symbol, self.pos = self.original_state

        self.visited.clear()
        self.visited.add((self.pos))

    def turn(self):
        """Turn to the right by 90 degrees"""
        self.symbol = Guard._turns[self.symbol]

    def walk(self, temporary_obstacles=set()) -> int:
        """Walk forward until you reach the nearest obstacle, returning the number of steps taken
        (or -1 if stepping out of bounds)."""

        direction = Guard._orientations[self.symbol]
        next_pos = (self.pos[0] + direction[0], self.pos[1] + direction[1])

        if self.grid.is_out_of_bounds(next_pos):
            return -1

        if self.grid.is_obstacle(next_pos, temporary_obstacles):
            self.turn()
            return 0

        nearest_obstacle = self.grid.get_nearest_obstruction(
            self.pos, direction)
        newly_visited = ()
        return 1

    def simulate_walk_out_of_bounds(self) -> bool:
        """Keep walking until out of bounds"""
        while True:
            state = self.walk()
            if state == -1:  # Out of bounds
                return False

    def detect_loop(self, temporary_obstacles=set()) -> bool:
        seen_positions = set()  # A set to track visited states
        pos = (self.r, self.c, self.symbol)
        while True:
            if pos in seen_positions:
                return True  # Loop detected
            seen_positions.add(pos)
            if self.walk(temporary_obstacles) == -1:
                return False  # Reached out of bounds, no loop
            pos = (self.r, self.c, self.symbol)

    def count_distinct_positions(self) -> int:
        """Counts the number of distinct positions visited"""
        return len(self.visited)


def one_star(filename: str):
    '''Returns the one star solution'''
    guard = load_file(filename)
    guard.simulate_walk_out_of_bounds()
    return guard.count_distinct_positions()


def two_star(filename: str):
    '''Returns the two star solution'''
    guard = load_file(filename)
    guard.simulate_walk_out_of_bounds()

    count = 0
    visited_positions = guard.visited

    newguard = load_file(filename)
    for r, c in visited_positions:
        newguard.grid.obstructions[r, c] = True
        if newguard.detect_loop():
            count += 1
        newguard.grid.obstructions[r, c] = False
        newguard.reset()

    return count


if __name__ == "__main__":
    print(f"One star test solution is {one_star(TEST_FILE)}")
    print(f"Two star test solution is {two_star(TEST_FILE)}")
    print(f"One star solution is {one_star(INPUT_FILE)}")
    print(f"Two star solution is {two_star(INPUT_FILE)}")
