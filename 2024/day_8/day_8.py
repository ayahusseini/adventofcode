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


def get_antinodes(antennas: list[tuple], nrows: int, ncols: int):
    """Generates antinodes given a list of antennas with the same symbol"""

    for i, antennna in antennas
    positions = get_antinode_positions(n1.pos, n2.pos)

    for pos in positions:
        if is_in_bounds(pos, nrows, ncols):
            yield Node(symbol='#', pos=pos)


def load_file(filename) -> dict[Node]:
    """Loads the file"""
    frequencies = defa
    with open(filename, 'r') as f:
        lines = f.readlines()
    return lines


def calculate_antinodes(filename)


def one_star(filename: str):
    '''Returns the one star solution'''
    guard = load_file(filename)
    return


def two_star(filename: str):
    '''Returns the two star solution'''
    return


if __name__ == "__main__":
    print(f"One star test solution is {one_star(TEST_FILE)}")
    print(f"Two star test solution is {two_star(TEST_FILE)}")
    print(f"One star solution is {one_star(INPUT_FILE)}")
    print(f"Two star solution is {two_star(INPUT_FILE)}")
