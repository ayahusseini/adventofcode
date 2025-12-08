"""Solution to day 2.

Each instruction of the form [direction] [X] represents a change in orientation and a translation of the submarine in the direction of the new orientation.

For example, in the one star case, "forward" flips the orientation to (1,0), "up" and "down" switch the orientation to (0,-1) and (0,1). The submarine then changes it's position by X units in the new orientation direction.

In the two star case, the new orientation after an instruction depends on a separate "aim" parameter. Suppose we start with aim x; "forward y" will change the orientation to (1,x). The submarine is translated y units in this direction, so its position changes by y * (1,x) points.

"""

import numpy as np

FILE = "inputs/day_2_input.txt"


def read_input_file(filename: str) -> list[list]:
    """Read the input file and return a list of instructions."""

    instructions = []
    with open(filename, "r") as f:
        for line in f.readlines():
            direction, amount = line.replace("\n", "").strip().split(" ")
            instructions.append([direction, int(amount)])

    return instructions


def map_direction_to_new_orientation_one_star(direction_name: str):
    directions = {
        "forward": np.array([1, 0]),
        "up": np.array([0, -1]),
        "down": np.array([0, 1]),
    }
    return directions[direction_name]


def map_direction_to_new_orientation_two_star(direction_name: str, current_aim: int):
    return (
        np.array([1, current_aim]) if direction_name == "forward" else np.array([0, 0])
    )


def get_aim_increment(direction_name: str, distance: int) -> int:
    """Returns the change in aim after a particular instruction."""
    directions = {"forward": 0, "up": -1, "down": 1}
    return directions[direction_name] * distance


def get_final_position_one_star(instructions: list[list]):
    """Each instruction is a list of the form [direction,distance].
    Given a list of such instructions, find the final position of the submarine."""

    return sum(
        [i[1] * map_direction_to_new_orientation_one_star(i[0]) for i in instructions]
    )


def get_final_position_two_stars(instructions: list[list]):
    """Returns the final position for the two star problem."""
    current_aim = 0
    current_pos = np.array([0, 0])
    for i in instructions:
        current_pos = sum(
            [
                current_pos,
                i[1] * map_direction_to_new_orientation_two_star(i[0], current_aim),
            ]
        )
        current_aim += get_aim_increment(i[0], i[1])
    return current_pos


if __name__ == "__main__":
    instructions = read_input_file(FILE)
    final_pos = get_final_position_one_star(instructions)
    print(f"One star solution: {final_pos[0] * final_pos[1]}")

    new_final_pos = get_final_position_two_stars(instructions)
    print(f"Two star solution: {new_final_pos[0] * new_final_pos[1]}")
