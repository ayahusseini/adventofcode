'''Solution to advent of code day 7 2015

Each WIRE
- Has an identifier (lowercase str)
- Carries a 16 bit SIGNAL (number from 0 to 65535)
- Can give its signal to multiple WIREs 

SIGNAL is given to each WIRE via one of three sources:
- GATE
- Another WIRE
- Some specific value 

GATE 
- Can give a signal after all of its imputs have a signal


'''

INPUT_FILE = "inputs/day_7_input.txt"
TEST_FILE = "inputs/day_7_test_input.txt"


def load_file(filename: str) -> list[int]:
    '''Loads the file as a list of integers'''

    with open(filename, "r") as f:
        lines = f.readlines()

    return [l.replace("\n", "").replace(" ", "") for l in lines]


def get_and(signal1: int, signal2: int) -> int:
    '''Return the bitwise and'''
    return signal1 & signal2


def get_left_shift(signal1: int, signal2: int) -> int:
    '''Left shift signal 1 by signal 2'''
    return signal1 << signal2


def get_complement(signal1: int) -> int:
    '''Return the bitwise complement'''
    return ~ signal1


def get_right_shift(signal1: int, signal2: int) -> int:
    '''Return signal1 shifted to the right by signal 2'''
    return signal1 >> signal2


def get_or(signal1: int, signal2: int) -> int:
    '''Return the bitwise or of signal1 and signal2'''
    return signal1 | signal2


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
