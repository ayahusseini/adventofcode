"""Solution to advent of code day 10 2024"""

INPUT_FILE = "inputs/day_10_input.txt"
TEST_FILE = "inputs/day_10_test_input.txt"


class Grid:
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def __init__(self, heights: dict, trailheads: set):
        """Instantiates a grid."""
        self.heights = heights
        self.trailheads = trailheads

    def get_neighbours(self, idx: tuple, memo: dict = dict()) -> set:
        """Returns the set of neighbours to an index as a dictionary of heights"""
        if idx in memo:
            return memo[idx]

        memo[idx] = set()
        for dr, dc in Grid.directions:
            if (idx[0] + dr, idx[1] + dc) in self.heights:
                memo[idx].add((idx[0] + dr, idx[1] + dc))

        return memo[idx]

    @classmethod
    def from_lines(cls, lines: list[str]):
        """Converts a set of lines to a dictionary and a set of trailhead indeces.
        The dictionary maps (row, column) positions to heights."""

        height_map = dict()
        trailheads_indeces = set()
        for row, l in enumerate(lines):
            for col, height in enumerate(l.strip()):
                height = int(height)
                height_map[(row, col)] = height
                if height == 0:
                    trailheads_indeces.add((row, col))

        return cls(height_map, trailheads_indeces)


def load_file(filename: str) -> Grid:
    """Loads the file as a Grid"""

    with open(filename, "r") as f:
        lines = f.readlines()

    return


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
