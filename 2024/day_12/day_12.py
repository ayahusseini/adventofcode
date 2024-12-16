'''Solution to advent of code day 12 2024
'''

INPUT_FILE = "inputs/day_12_input.txt"
TEST_FILE = "inputs/day_12_test_input.txt"
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def load_file(filename: str) -> dict[tuple, str]:
    """Loads the file as a dictionary mapping positions to letters"""
    with open(filename, "r") as f:
        positions = read_lines(f.readlines())
    return positions


def read_lines(lines: list[str]) -> dict[tuple, str]:
    """Converts a list of strings into a map between positions and letters"""
    positions = dict()
    for r, line in enumerate(lines):
        for c, char in enumerate(line.strip()):
            positions[(r, c)] = char
    return positions


def get_neighbours(idx):
    """Generates the neighbours of an index"""
    neighbours = []
    for dr, dc in DIRECTIONS:
        neighbours.append((idx[0] + dr, idx[1] + dc))
    return neighbours


def dfs(start_idx: tuple, all_positions: dict, visited: set) -> tuple[int, int]:
    """Returns the area and perimeter of the region. 
    The exploration starts at start_idx and only considers univisited positions.
    The set of visited positions is updated."""

    if start_idx in visited:
        raise ValueError("The start index has already been visited.")
    if start_idx not in all_positions:
        raise ValueError("The start index is not on the map.")

    area = 1
    perimeter = 0
    char = all_positions[start_idx]
    visited.add(start_idx)
    queue = [start_idx]

    while queue:
        current = queue.pop(0)

        for n in get_neighbours(current):
            if n not in all_positions:
                perimeter += 1
                continue
            if all_positions[n] != char:
                perimeter += 1
                continue

            if n not in visited:
                area += 1
                visited.add(n)
                queue.append(n)

    return area, perimeter


def find_all_regions(positions: dict) -> list[tuple[str, int, int]]:
    """Returns a list containing the letter, area and perimeter of all the regions"""

    if (0, 0) not in positions:
        raise ValueError("Starting position (0, 0) not in positions")

    visited = set()
    final = []

    for start, letter in positions.items():
        if start in visited:
            continue
        area, perimeter = dfs(start, positions, visited)
        final += [(letter, area, perimeter)]
    return final


def one_star(filename: str):
    '''Returns the one star solution'''
    pos = load_file(filename)
    regions = find_all_regions(pos)
    return sum([area * perimeter for _, area, perimeter in regions])


def two_star(filename: str):
    '''Returns the two star solution'''
    pos = load_file(filename)

    return


if __name__ == "__main__":
    print(f"One star test solution is {one_star(TEST_FILE)}")
    print(f"Two star test solution is {two_star(TEST_FILE)}")
    print(f"One star solution is {one_star(INPUT_FILE)}")
    print(f"Two star solution is {two_star(INPUT_FILE)}")
