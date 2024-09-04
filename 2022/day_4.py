'''Solution to advent of code day 4 2022

Puzzle input = pairs of ranges
'''

INPUT_FILE = "inputs/day_4_input.txt"
TEST_FILE = "inputs/day_4_test_input.txt"


def load_file(filename: str) -> list[str]:
    '''Loads the file as a list of integers'''

    with open(filename, "r") as f:
        lines = f.readlines()

    return [l.replace("\n", "").replace(" ", "") for l in lines]


def get_pairs(lines: str) -> list[list]:
    '''Return a list of lists. Each sub-list contains a pair of lists
    representing the ranges.'''
    pairs = []
    for line in lines:
        pair = line.split(",")
        ranges = []
        for r in pair:
            e = r.split("-")
            ranges.append([int(e[0]), int(e[1])])
        pairs.append(ranges)
    return pairs


def is_overlap(range1: list, range2: list) -> bool:
    s, l = range1, range2

    if range1[0] > range2[0]:
        s = range2
        l = range1
    if range1[0] == range2[0]:
        return True
    return l[1] <= s[1] or l[0] <= s[1]


def is_complete_overlap(range1: list, range2: list) -> bool:
    '''Return true if there's a complete overlap'''
    s, l = range1, range2

    if range1[0] > range2[0]:
        s = range2
        l = range1
    if range1[0] == range2[0]:
        return True
    return l[1] <= s[1] and l[0] <= s[1]


def one_star(filename: str):
    '''Returns the one star solution'''
    lines = load_file(filename)
    pairs = get_pairs(lines)
    print(len(pairs))
    return sum([1 for p in pairs if is_complete_overlap(p[0], p[1])])


def two_star(filename: str):
    '''Returns the two star solution'''
    lines = load_file(filename)
    pairs = get_pairs(lines)
    print(len(pairs))
    return sum([1 for p in pairs if is_overlap(p[0], p[1])])


if __name__ == "__main__":
    print(f"One star solution is {one_star(TEST_FILE)}")
    print(f"Two star solution is {two_star(TEST_FILE)}")
    print(f"One star solution is {one_star(INPUT_FILE)}")
    print(f"Two star solution is {two_star(INPUT_FILE)}")
