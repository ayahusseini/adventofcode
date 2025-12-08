"""Solution to advent of code day 1 2015"""

INPUT_FILE = "inputs/day_1_input.txt"


def load_file(filename: str) -> str:
    """Loads the input as a string"""
    with open(filename, "r") as f:
        return f.readline().replace("\n", "").strip()


def get_net_floor(string: str) -> int:
    """Returns the net floor"""
    net = 0
    directions = {"(": 1, ")": -1}
    for k, sf in directions.items():
        net += string.count(k) * sf
    return net


def find_basement_instruction_pos(string: str) -> int:
    """Returns the index of the first character that causes the net floor to become negative."""
    counts = {"(": 0, ")": 0}
    for i, char in enumerate(string):
        counts[char] += 1
        if counts[")"] > counts["("]:
            return i + 1
    return "not found"


def one_star(filename: str):
    """Returns the one star solution"""
    instructions = load_file(filename)

    return get_net_floor(instructions)


def two_star(filename: str):
    """Returns the one star solution"""
    instructions = load_file(filename)

    return find_basement_instruction_pos(instructions)


if __name__ == "__main__":
    print(f"One star solution is {one_star(INPUT_FILE)}")
    print(f"Two star solution is {two_star(INPUT_FILE)}")
