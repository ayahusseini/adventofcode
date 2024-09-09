'''Solution to advent of code day 3 2015.

House positions are given as tuples (east,north) with starting
position (0,0)'''

INPUT_FILE = "inputs/day_3_input.txt"


def map_instruction_to_direction() -> dict:
    '''Return a dict indicating the change in position for each instruction.'''
    return {'>': [1, 0], '<': [-1, 0], '^': [0, 1], 'v': [0, -1]}


def get_path(instructions: str) -> list[tuple]:
    '''Return a list of positions visited.'''
    instruction_map = map_instruction_to_direction()
    path = [(0, 0)]
    for i in instructions:
        curr_x, curr_y = path[-1]

        change = instruction_map[i]

        path.append((curr_x + change[0], curr_y + change[1]))
    return path


def count_visits(instructions: str) -> int:
    '''Return the number of houses visited at least once'''
    path = get_path(instructions)
    return len(set(path))


def count_visits_two_paths(instructions1: str, instructions2: str) -> int:
    path = []
    for i in (instructions1, instructions2):
        path += get_path(i)
    return len(set(path))


def split_instructions(instructions: str) -> tuple[str, str]:
    '''Split the instructions into two strings. The first contains even positions, the second contains odd positions.'''
    i1 = "".join([l for i, l in enumerate(instructions) if i % 2 == 0])
    i2 = "".join([l for i, l in enumerate(instructions) if i % 2 != 0])
    return i1, i2


def load_file(filename: str) -> str:
    '''Loads the input as a string'''
    with open(filename, 'r') as f:
        return f.readline().replace("\n", "").strip()


def one_star(filename: str):
    '''Returns the one star solution'''
    instructions = load_file(filename)

    return count_visits(instructions)


def two_star(filename: str):
    '''Returns the one star solution'''
    instructions = load_file(filename)

    i1, i2 = split_instructions(instructions)

    return count_visits_two_paths(i1, i2)


if __name__ == "__main__":
    print(f"One star solution is {one_star(INPUT_FILE)}")
    print(f"Two star solution is {two_star(INPUT_FILE)}")
