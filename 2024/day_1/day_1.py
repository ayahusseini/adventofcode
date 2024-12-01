'''Solution to advent of code day 1 2024
'''

INPUT_FILE = "inputs/day_1_input.txt"
TEST_FILE = "inputs/day_1_test_input.txt"


def load_file(filename: str) -> list[int]:
    '''Loads the file as two lists of integers'''
    l1 = []
    l2 = []
    with open(filename, "r") as f:
        lines = f.readlines()
        for line in lines:
            ints = line.split("   ")
            l1.append(int(ints[0]))
            l2.append(int(ints[0]))
    return l1, l2 


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
