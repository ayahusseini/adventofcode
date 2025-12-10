"""Solution to advent of code day 4 2025"""

INPUT_FILE = "inputs/day_4_input.txt"
TEST_FILE = "inputs/day_4_test_input.txt"


def load_file(filename: str):
    """Load the puzzle input, yielding stripped lines."""
    with open(filename, "r") as f:
        for line in f:
            yield line.strip()


def one_star(filename: str):
    """Solve part 1 for day 4."""
    raise NotImplementedError("Day 4 part 1 not implemented yet")


def two_star(filename: str):
    """Solve part 2 for day 4."""
    raise NotImplementedError("Day 4 part 2 not implemented yet")


if __name__ == "__main__":
    print(f"One star test solution is {one_star(TEST_FILE)}")
    print(f"Two star test solution is {two_star(TEST_FILE)}")
    print(f"One star solution is {one_star(INPUT_FILE)}")
    print(f"Two star solution is {two_star(INPUT_FILE)}")
