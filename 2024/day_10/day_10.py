"""Solution to advent of code day 10 2024"""

INPUT_FILE = "inputs/day_10_input.txt"
TEST_FILE = "inputs/day_10_test_input.txt"


class Grid:
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def __init__(self, heights: dict, trailheads: set):
        """Instantiates a grid."""
        self.heights = heights
        self.trailheads = trailheads

        self.neighbours = dict()

    def get_neighbours(self, idx: tuple) -> set:
        """Returns the set of neighbours to an index as a dictionary of heights"""
        if idx in self.neighbours:
            return self.neighbours[idx]

        self.neighbours[idx] = set()
        for dr, dc in Grid.directions:
            if (idx[0] + dr, idx[1] + dc) in self.heights:
                self.neighbours[idx].add((idx[0] + dr, idx[1] + dc))

        return self.neighbours[idx]

    def get_paths(self) -> dict[tuple, list[list]]:
        """Returns a dictionary mapping each trailhead to a list of paths"""
        queue = [[idx] for idx in self.trailheads]
        found = {idx: [] for idx in self.trailheads}

        while queue:
            current_path = queue.pop(0)

            last_idx = current_path[-1]

            if self.heights[last_idx] == 9:
                found[current_path[0]].append(current_path)
                continue

            for neighbour in self.get_neighbours(last_idx):
                if self.heights[neighbour] - self.heights[last_idx] == 1:
                    new_path = current_path + [neighbour]
                    queue.append(new_path)

        return found

    def get_trailhead_scores(self) -> dict[tuple, int]:
        """Returns a map of trailheads to their scores"""
        scores = dict()
        paths = self.get_paths()
        for start_idx, path_list in paths.items():
            scores[start_idx] = len(set([p[-1] for p in path_list]))
        return scores

    def get_trailhead_ratings(self) -> dict[tuple, int]:
        """Returns a map of trailheads to their ratings"""
        scores = dict()
        paths = self.get_paths()
        for start_idx, path_list in paths.items():
            scores[start_idx] = len(path_list)
        return scores

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

    return Grid.from_lines(lines)


def one_star(filename: str):
    """Returns the one star solution"""

    grid = load_file(filename)
    scores = grid.get_trailhead_scores()
    return sum(scores.values())


def two_star(filename: str):
    """Returns the two star solution"""

    grid = load_file(filename)
    ratings = grid.get_trailhead_ratings()
    return sum(ratings.values())


if __name__ == "__main__":
    print(f"One star test solution is {one_star(TEST_FILE)}")
    print(f"Two star test solution is {two_star(TEST_FILE)}")
    print(f"One star solution is {one_star(INPUT_FILE)}")
    print(f"Two star solution is {two_star(INPUT_FILE)}")
