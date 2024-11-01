"""Solution to day 14 2021"""

INPUT_FILE = "inputs/day_14_input.txt"
TEST_FILE = "inputs/day_14_test_input.txt"


def load_file(filename: str) -> tuple:
    '''Loads the file as a template and a list of rules'''

    with open(filename, "r") as f:
        lines = f.readlines()

    template = lines.pop(0).replace("\n", "")
    rules = [l.replace("\n", "").split(' -> ') for l in lines[1:]]

    return template, rules


def one_star(filename: str):
    '''Returns the one star solution'''
    lines = load_file(filename)

    return


def two_star(filename: str):
    '''Returns the two star solution'''

    return


if __name__ == "__main__":
    print(f"One star solution is {one_star(TEST_FILE)}")
    print(f"Two star solution is {two_star(TEST_FILE)}")
    print(f"One star solution is {one_star(INPUT_FILE)}")
    print(f"Two star solution is {two_star(INPUT_FILE)}")
