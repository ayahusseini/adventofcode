'''Solution to advent of code day 10 2021
'''
import re
INPUT_FILE = "inputs/day_8_input.txt"
TEST_FILE = "inputs/day_8_test_input_2.txt"


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

    return len(line)


def num_characters_of_code_after_encoding(line: str):
    count = len(line)  # for the quotations
    count += line.count('"')*2
    count += len([f for f in re.findall(r"\\x..", line) if f is not None])

    print(len(line))
    print(line, r"{}".format(line[1:-1]))
    return len(r"{}".format(line))


def one_star(filename: str):
    '''Returns the one star solution'''
    lines = load_file(filename)

    chars_of_code = sum([get_num_characters_of_code(l) for l in lines])
    chars_of_string = sum([get_num_characters_of_string(l) for l in lines])
    return chars_of_code - chars_of_string


def two_star(filename: str):
    '''Returns the two star solution'''
    lines = load_file(filename)
    print(lines)
    chars_of_code = sum([get_num_characters_of_code(l) for l in lines])

    chars_after_encoding = sum(
        [num_characters_of_code_after_encoding(l) for l in lines])

    return chars_after_encoding - chars_of_code


if __name__ == "__main__":
    print(f"One star solution is {one_star(TEST_FILE)}")
    print(f"Two star solution is {two_star(TEST_FILE)}")
    # print(f"One star solution is {one_star(INPUT_FILE)}")
    # print(f"Two star solution is {two_star(INPUT_FILE)}")
