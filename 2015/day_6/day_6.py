"""Solution to advent of code day 6 2015"""

import numpy as np

INPUT_FILE = "inputs/day_6_input.txt"


class SquareGrid(np.ndarray):
    """Grid of lights where -1 represents off and 1 represents on."""

    def __init__(self, size: int = 1000):
        """Sets the initial state.
        The way that the square grid responds to instructions depends on the mode."""
        self.state = np.full((size, size), -1)

    def operate(self, operation: str, x1: int, y1: int, x2: int, y2: int):
        """Operates on a subgrid"""
        if x1 > x2:
            x1, x2 = x2, x1
        if y1 > y2:
            y1, y2 = y2, y1
        if operation == "turn on":
            self.__switch_on(x1, y1, x2, y2)
        elif operation == "toggle":
            self.__toggle(x1, y1, x2, y2)
        elif operation == "turn off":
            self.__switch_off(x1, y1, x2, y2)

    def __toggle(self, x1: int, y1: int, x2: int, y2: int):
        self.state[x1 : x2 + 1, y1 : y2 + 1] *= -1

    def __switch_on(self, x1: int, y1: int, x2: int, y2: int):
        self.state[x1 : x2 + 1, y1 : y2 + 1] = 1

    def __switch_off(self, x1: int, y1: int, x2: int, y2: int):
        self.state[x1 : x2 + 1, y1 : y2 + 1] = -1

    def count_on(self):
        return (self.state == 1).sum()


class SquareGridTwoStars(np.ndarray):
    """Implementation of the square grid for the two star part of the question."""

    def __init__(self, size: int = 1000):
        self.state = np.full((size, size), 0)

    def operate(self, operation: str, x1: int, y1: int, x2: int, y2: int):
        """Operates on a subgrid"""
        if x1 > x2:
            x1, x2 = x2, x1
        if y1 > y2:
            y1, y2 = y2, y1
        if operation == "turn on":
            self.__switch_on(x1, y1, x2, y2)
        elif operation == "toggle":
            self.__toggle(x1, y1, x2, y2)
        elif operation == "turn off":
            self.__switch_off(x1, y1, x2, y2)

    def __toggle(self, x1: int, y1: int, x2: int, y2: int):
        self.state[x1 : x2 + 1, y1 : y2 + 1] += 2

    def __switch_on(self, x1: int, y1: int, x2: int, y2: int):
        self.state[x1 : x2 + 1, y1 : y2 + 1] += 1

    def __switch_off(self, x1: int, y1: int, x2: int, y2: int):
        self.state[x1 : x2 + 1, y1 : y2 + 1] -= 1
        self.state[x1 : x2 + 1, y1 : y2 + 1][
            self.state[x1 : x2 + 1, y1 : y2 + 1] < 0
        ] = 0

    def tot_brightness(self):
        return np.sum(self.state)


def load_file(filename: str) -> list[int]:
    """Loads the file as a list of integers"""
    with open(filename, "r") as f:
        lines = f.readlines()

    return [l.replace("\n", "").strip() for l in lines]


def read_coord(coord: str) -> tuple[int]:
    """Convert coordinate string into tuple"""
    return tuple([int(i) for i in coord.split(",")])


def extract_instruction(instruction: str) -> list:
    """Return the instruction 'word' and the list of coordinates"""
    keywords = ["turn on", "toggle", "turn off"]

    for k in keywords:
        if k in instruction:
            through_loc = instruction.find("through")
            x1, y1 = read_coord(instruction[len(k) + 1 : through_loc].strip())

            x2, y2 = read_coord(instruction[through_loc + len("through") :].strip())

            return [k, x1, y1, x2, y2]


def one_star(filename: str):
    """Returns the one star solution"""
    instructions = load_file(filename)
    grid = SquareGrid(1000)
    for line in instructions:
        grid.operate(*extract_instruction(line))
    return grid.count_on()


def two_star(filename: str):
    """Returns the two star solution"""
    instructions = load_file(filename)
    grid = SquareGridTwoStars(1000)
    for line in instructions:
        grid.operate(*extract_instruction(line))
    return grid.tot_brightness()


if __name__ == "__main__":
    print(f"One star solution is {one_star(INPUT_FILE)}")
    print(f"Two star solution is {two_star(INPUT_FILE)}")
