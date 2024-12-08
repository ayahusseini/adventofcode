"""Solution for advent of code day 8 2024"""

from collections import defaultdict

INPUT_FILE = "inputs/day_8_input.txt"
TEST_FILE = "inputs/day_8_test_input.txt"


def multiply(scalar: int, vector: tuple, ) -> tuple:
    """Returns scalar * vector"""
    return (vector[0] * scalar, vector[1] * scalar)


def subtract_vector(n1: tuple, n2: tuple) -> tuple:
    """Returns n1 - n2"""
    return (n1[0]-n2[0], n1[1]-n2[1])


def get_antinode_positions(pos1: tuple, pos2: tuple) -> tuple[tuple, tuple]:
    """Returns a pair of antinode positions"""
    return subtract_vector(multiply(2, pos1), pos2), subtract_vector(multiply(2, pos2), pos1)


def is_in_bounds(position: tuple, numrows: int, numcols: int) -> bool:
    return (0 <= position[0] < numrows) and (0 <= position[1] < numcols)


def get_all_pairs(full_list: list, memo: dict = dict()) -> list:
    numitems = len(full_list)
    if memo.get(numitems) is not None:
        return [(full_list[i], full_list[j]) for i, j in memo[numitems]]
    memo[numitems] = []
    all_pairs = []

    for i in range(numitems):
        for j in range(i + 1, numitems):
            memo[numitems].append((i, j))
            all_pairs.append((full_list[i], full_list[j]))
    return all_pairs


def get_antinodes(antennas: list[tuple], nrows: int, ncols: int):
    """Generates antinodes given a list of antennas with the same symbol"""
    antinodes = []
    for pair in get_all_pairs(antennas):
        positions = get_antinode_positions(*pair)
        for pos in positions:
            if is_in_bounds(pos, nrows, ncols):
                antinodes += [pos]
    return antinodes


def load_file(filename) -> tuple[dict[list], int, int]:
    """Loads the file"""
    frequencies = defaultdict(lambda: [])
    with open(filename, 'r') as f:
        lines = f.readlines()

    nrows = len(lines)
    ncols = len(lines[0].replace('\n', ''))
    for r, l in enumerate(lines):
        l = l.replace('\n', '')
        for c, char in enumerate(l):
            if char != '.':
                frequencies[char].append((r, c))
    return frequencies, nrows, ncols


def one_star(filename: str):
    '''Returns the one star solution'''
    antennas, nrows, ncols = load_file(filename)
    antinodes = set()
    for _, positions in antennas.items():
        antinodes.update(get_antinodes(positions, nrows, ncols))
    return len(antinodes)


def two_star(filename: str):
    '''Returns the two star solution'''
    return


if __name__ == "__main__":
    print(f"One star test solution is {one_star(TEST_FILE)}")
    print(f"Two star test solution is {two_star(TEST_FILE)}")
    print(f"One star solution is {one_star(INPUT_FILE)}")
    print(f"Two star solution is {two_star(INPUT_FILE)}")
