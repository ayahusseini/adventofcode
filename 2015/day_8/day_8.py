'''Solution to advent of code day 10 2021
'''
import re
INPUT_FILE = "inputs/day_8_input.txt"
TEST_FILE = "inputs/day_8_test_input.txt"


def load_file(filename: str) -> list[int]:
    '''Loads the file as a list of integers'''

    with open(filename, "r") as f:
        lines = f.readlines()

    return [l.replace("\n", "").replace(" ", "") for l in lines]


def get_num_characters_of_code(line: str):
    return len(line)


def get_num_characters_of_string(line: str):
    # remove quotation marks
    line = line[1:-1]
    # reformat
    line = line.encode().decode("unicode-escape")
    print(line)

    return len(line)


def one_star(filename: str):
    '''Returns the one star solution'''
    lines = load_file(filename)
    print(lines)
    return


def two_star(filename: str):
    '''Returns the two star solution'''

    return


if __name__ == "__main__":
    print(f"One star solution is {one_star(TEST_FILE)}")
    print(f"Two star solution is {two_star(TEST_FILE)}")
    # print(f"One star solution is {one_star(INPUT_FILE)}")
    print(f"Two star solution is {two_star(INPUT_FILE)}")
