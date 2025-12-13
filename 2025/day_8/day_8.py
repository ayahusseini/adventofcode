"""Solution to advent of code day 8 2025"""

INPUT_FILE = 'inputs/day_8_input.txt'
TEST_FILE = 'inputs/day_8_test_input.txt'


def load_file(filename: str):
    """Load the puzzle input, yielding stripped lines."""
    with open(filename, 'r') as f:
        lines = [l.strip() for l in f if l.strip()]
    return lines


def one_star(filename: str):
    """Solve part 1 for day 8."""
    raise NotImplementedError('Day 8 part 1 not implemented yet')


def two_star(filename: str):
    """Solve part 2 for day 8."""
    raise NotImplementedError('Day 8 part 2 not implemented yet')


if __name__ == '__main__':
    print(f'One star test solution is {one_star(TEST_FILE)}')
    print(f'Two star test solution is {two_star(TEST_FILE)}')
    print(f'One star solution is {one_star(INPUT_FILE)}')
    print(f'Two star solution is {two_star(INPUT_FILE)}')
