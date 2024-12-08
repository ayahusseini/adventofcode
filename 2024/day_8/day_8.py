"""Solution for advent of code day 8 2024"""
INPUT_FILE = "inputs/day_8_input.txt"
TEST_FILE = "inputs/day_8_test_input.txt"


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
