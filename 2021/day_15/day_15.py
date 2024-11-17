'''Solution to advent of code day 15 2021
'''

import numpy as np

INPUT_FILE = "inputs/day_15_input.txt"
TEST_FILE = "inputs/day_15_test_input.txt"


class Grid:
    def __init__(self, array: np.ndarray, allow_diag: bool = False):
        """Instangiate a map of caves"""
        self.array = array
        self.nrows, self.ncols = array.shape

        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        if allow_diag:
            self.directions.extend([(1, 1), (-1, -1)])

    def min_path_length(self, start: tuple, end: tuple):
        """Returns the minimum path length"""
        dist = np.full_like(self.array, fill_value=np.inf)
        visited = np.full_like(self.array, fill_value=False, dtype=bool)
        dist[*start] = 0

        while not visited[*end]:
            node = np.where(dist == dist[~visited].min())[0]
            node_value = dist[node]

            print(f"Visiting index {node}")

            visited[*node] = True
            for dir in self.directions:
                r, c = node[0] + dir[0], node[1] + dir[1]
                print("checking neighbour", r, c)
                if r < 0 or c < 0 or r >= self.nrows or c >= self.ncols:
                    continue
                possible_update = self.array[r, c] + node_value
                if possible_update < dist[r, c]:
                    dist[r, c] = possible_update

        return dist[*end]


def load_file(filename: str) -> np.ndarray:
    '''Loads the file as a numpy array'''

    with open(filename, "r") as f:
        lines = f.readlines()

    return np.array([[int(digit) for digit in l.strip()] for l in lines if l.strip()])


def one_star(filename: str):
    '''Returns the one star solution'''
    grid_values = load_file(filename)
    grid = Grid(grid_values)

    return grid.min_path_length([0, 0], [grid.nrows-1, grid.ncols-1])


def two_star(filename: str):
    '''Returns the two star solution'''

    return


if __name__ == "__main__":
    print(f"One star test solution is \n{one_star(TEST_FILE)}")
    print(f"Two star test solution is {two_star(TEST_FILE)}")
    print(f"One star solution is {one_star(INPUT_FILE)}")
    # print(f"Two star solution is {two_star(INPUT_FILE)}")
