"""Solution to advent of code day 7 2025"""
INPUT_FILE = "inputs/day_7_input.txt"
TEST_FILE = "inputs/day_7_test_input.txt"


def load_file(filename: str):
    """
    Load the puzzle input, returning processed lines

    Returns:
        is_beam : 2D array which is '1' at the source 
        is_splitted: 2D array which is '1' at any splitters
    """

    with open(filename, "r") as f:
        lines = [list(l.strip()) for l in f if l.strip()]

    is_beam = [[1 for char in l if char == 'S'] for l in lines]
    is_splitter = [[1 for char in l if char == '^'] for l in lines]
    return is_beam, is_splitter


def is_diag(idx1: tuple[int, int], idx2: tuple[int, int]):
    """Return True if idx1 is directly diagonal to idx2"""
    r1, c1 = idx1
    r2, c2 = idx2
    return abs(r1 - r2) == 1 and abs(c1 - c2) == 1


def one_star(filename: str):
    """
    Solve part 1 for day 7.
    Returns:
        num_splits : The number of time the beam gets split
    """

    is_beam, is_splitter = load_file(filename)


def two_star(filename: str):
    """
    Solve part 2 for day 7.
    """
    raise NotImplementedError("Day 7 part 2 not implemented yet")


if __name__ == "__main__":
    print(f"One star test solution is {one_star(TEST_FILE)}")
    # print(f"Two star test solution is {two_star(TEST_FILE)}")
    # print(f"One star solution is {one_star(INPUT_FILE)}")
    # print(f"Two star solution is {two_star(INPUT_FILE)}")
