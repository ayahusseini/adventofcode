"""Solution for advent of code day 8 2024"""
from collections import namedtuple
INPUT_FILE = "inputs/day_8_input.txt"
TEST_FILE = "inputs/day_8_test_input.txt"

Node = namedtuple("node", ("symbol", "pos"))


def multiply(scalar: int, vector: tuple, ) -> tuple:
    return (vector[0] * scalar, vector[1] * scalar)


def subtract_vector(n1: tuple, n2: tuple) -> tuple:
    return (n2[0]-n1[0], n2[1]-n1[1])


def get_antinode_positions(pos1: tuple, pos2: tuple) -> tuple[tuple, tuple]:
    """Returns a pair of antinode positions"""
    return subtract_vector(multiply(2, pos1), pos2), subtract_vector(multiply(2, pos2), pos1)


def get_antinodes(n1: Node, n2: Node) -> tuple[Node, Node]:
    """Generates a pair of antinodes"""
    if not n1.symbol == n2.symbol:
        raise ValueError("They must have the same symbol.")


def load_file(filename) -> list[str]:
    """Loads the file"""
    with open(filename, 'r') as f:
        lines = f.readlines()
    return lines


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
