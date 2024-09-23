'''Solution to advent of code day 13 2015
'''
from collections import defaultdict
from itertools import permutations
INPUT_FILE = "inputs/day_13_input.txt"
TEST_FILE = "inputs/day_13_test_input.txt"


def load_file(filename: str) -> list[int]:
    '''Loads the file as a list of integers'''

    with open(filename, "r") as f:
        lines = f.readlines()

    return [l.replace("\n", "") for l in lines]


def map_relations(lines: list[str]) -> tuple[dict, set]:
    '''Return a dictionary containing pairs and the net happiness if they sat next to one another as well as the set of people'''

    relations = defaultdict(lambda: 0)
    people = set()
    for l in lines:
        words = l.split(" ")

        if "gain" in l:
            multiplier = 1
        elif "lose" in l:
            multiplier = -1
        pair = [words[0], words[-1].replace(".", "")]
        people.update(pair)
        pair.sort()
        relations[tuple(pair)] += int(words[3]) * multiplier
    return relations, people


def get_relation(p1: str, p2: str, rmap: dict, allow_fake: bool = False) -> int:
    '''Get the net happiness of person 1 and person 2 sitting next to each other. If allow_fake then any pair which isn't in rmap will return 0 happiness'''
    pair = [p1, p2]
    pair.sort()

    return rmap[tuple(pair)] if not allow_fake else rmap.get(tuple(pair), 0)


def get_all_cycles(people: list, insert_fake: bool = False) -> list[list]:
    '''Return a list of all possible permutations'''
    if not people:
        return []

    first = people.pop(0)
    print(people)
    perms = permutations(people)
    cycles = []

    for p in perms:
        cycles.append([first, *list(p), first])
    return cycles


def get_cycle_length(cycle: list, mapping, allow_fake: bool = False):
    length = 0
    for i, p1 in enumerate(cycle[:-1]):
        length += get_relation(p1, cycle[i+1], mapping, allow_fake)

    return length


def one_star(filename: str):
    '''Returns the one star solution'''
    lines = load_file(filename)
    mapping, people = map_relations(lines)
    possible_cycles = get_all_cycles(list(people))

    return max(get_cycle_length(c, mapping) for c in possible_cycles)


def two_star(filename: str):
    '''Returns the two star solution'''
    lines = load_file(filename)
    mapping, people = map_relations(lines)
    people = ["Me"] + list(people)

    possible_cycles = get_all_cycles(people, insert_fake=True)

    return max(get_cycle_length(c, mapping, allow_fake=True) for c in possible_cycles)


if __name__ == "__main__":
    print(f"One star solution is {one_star(TEST_FILE)}")
    print(f"Two star solution is {two_star(TEST_FILE)}")
    print(f"One star solution is {one_star(INPUT_FILE)}")
    print(f"Two star solution is {two_star(INPUT_FILE)}")
