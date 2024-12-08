"""Solution to advent of code day 8 2023"""

INPUT_FILE = "inputs/day_8_input.txt"
TEST_FILE = "inputs/day_8_test_input.txt"


def get_next_step(steps: str):
    i = 0
    while True:
        yield steps[i]
        i += 1
        if i == len(steps):
            i = 0


def load_file(filename: str) -> list[str]:
    '''Loads the file as a list of strings'''

    with open(filename, "r") as f:
        lines = f.readlines()

    return [l.replace("\n", "").replace(" ", "") for l in lines]


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
