import numpy as np
INPUT_FILE = "inputs/day_6_input.txt"
TEST_FILE = "inputs/day_6_test_input.txt"


class Grid:
    def __init__(self, is_obstruction: np.ndarray):
        self.obstructions = is_obstruction
        self.nrows = len(is_obstruction)
        self.ncols = len(is_obstruction[0])

    def is_out_of_bounds(self, idx: tuple) -> bool:
        return not (0 <= idx[0] < self.nrows and 0 <= idx[1] < self.ncols)

    def is_obstacle(self, idx: tuple, temporary_obstacles=set()) -> bool:
        return self.obstructions[idx[0], idx[1]] or idx in temporary_obstacles


class Guard:
    _turns = {'^': '>', '>': 'v', '<': '^', 'v': '<'}
    _orientations = {'^': (-1, 0), '>': (0, 1), '<': (0, -1), 'v': (1, 0)}

    def __init__(self, grid: Grid, position: tuple, symbol: tuple):
        self.grid = grid
        self.r, self.c = position
        self.visited = {(self.r, self.c)}
        self.symbol = symbol
        self.dr, self.dc = Guard._orientations[symbol]
        self.original_state = (self.symbol, self.r, self.c, self.dr, self.dc)

    def reset(self):
        self.symbol, self.r, self.c, self.dr, self.dc = self.original_state
        self.visited.clear()
        self.visited.add((self.r, self.c))

    def turn(self):
        """Turn to the right by 90 degrees"""
        self.symbol = Guard._turns[self.symbol]
        self.dr, self.dc = Guard._orientations[self.symbol]

    def walk(self, temporary_obstacles=set()) -> int:
        """Walk forward"""
        next_pos = (self.r + self.dr, self.c + self.dc)
        if self.grid.is_out_of_bounds(next_pos):
            return -1

        if self.grid.is_obstacle(next_pos, temporary_obstacles):
            self.turn()
            return 0

        self.r, self.c = next_pos
        self.visited.add((self.r, self.c))
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
    guard = load_file(filename)
    guard.simulate_walk_out_of_bounds()

    # Instead of using np.argwhere, just iterate over visited positions
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
