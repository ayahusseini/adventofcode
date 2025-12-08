"""Solution to advent of code day 5 2023"""

import re

INPUT_FILE = "inputs/day_5_input.txt"
TEST_FILE = "inputs/day_5_test_input.txt"


class Map:
    def __init__(self, source: str, destination: str):
        """Instantiates a Map"""

        self.source = source
        self.destination = destination

        self.mapping = {}

    def get_destination(self, source_location: int):
        """Returns the destination"""

        for sr, change in self.mapping.items():
            if source_location not in range(*sr):
                continue
            else:
                return source_location + change
        return source_location

    def get_destination_from_range(self, start: int, end: int):
        """Returns the destination range"""
        curr = (start, end)
        mapped_ranges = []
        for sr, change in self.mapping.items():
            overlap, curr = split_range(curr, sr)
            if overlap == tuple():
                continue
            mapped_ranges.append((overlap[0] + change, overlap[1] + change))
            if curr == tuple():
                break
        if curr != tuple():
            mapped_ranges.append(curr)
        return mapped_ranges

    def add_rule(self, dest_start: int, source_start: int, limit: int):
        """Adds a rule to the mapping dictionary"""

        source_range = (source_start, source_start + limit)
        difference = dest_start - source_start
        self.mapping.update({source_range: difference})


def load_file(filename: str) -> tuple[list[int], list[Map]]:
    """Loads the file as a list of initial seed positions
    and a list of maps
    """

    with open(filename, "r") as f:
        lines = f.readlines()
    lines = [l.replace("\n", "") for l in lines]
    return process_lines(lines)


def process_lines(lines: str) -> tuple[list[int], list[Map]]:
    """Splits lines up into a list of seeds and a list of maps"""

    seeds = [int(i) for i in lines[0].split("seeds: ")[-1].split(" ")]

    maps = []
    curr = False

    for i, line in enumerate(lines[1:]):
        if not line:
            if not curr:
                continue
            else:
                maps.append(curr)
        elif line[-4:] == "map:":
            names = re.match(r"(\w+)-to-(\w+) map:", line)
            curr = Map(names.group(1), names.group(2))
        else:
            details = [int(i) for i in line.split(" ")]
            curr.add_rule(*details)
            if len(lines[1:]) == i + 1:
                maps.append(curr)

    return seeds, maps


def split_range(range1: tuple, range2: tuple) -> tuple:
    """Split range1 into a part that overlaps with range2
    and a part that doesn't"""
    if range1[1] in range(*range2) and range1[0] in range(*range2):
        return range1, tuple()
    elif range1[0] in range(*range2):
        return (range1[0], range2[1]), (range2[1], range1[1])
    elif range1[1] - 1 in range(*range2):
        return (range2[0], range1[1]), (range1[0], range2[0])
    return tuple(), range1


def one_star(filename: str):
    """Returns the one star solution"""
    seeds, maps = load_file(filename)
    positions = []
    for seed in seeds:
        pos = seed
        for m in maps:
            pos = m.get_destination(pos)

        positions.append(pos)
    return min(positions)


def two_star(filename: str):
    """Returns the two star solution"""
    seed_line, maps = load_file(filename)
    seed_ranges = []
    for i, s in enumerate(seed_line[:-1]):
        if i % 2 != 0:
            continue
        limit = seed_line[i + 1]
        seed_ranges += [(s, s + limit)]

    positions = []
    for r in seed_ranges:
        pos_ranges = [r]
        for m in maps:
            mapped_ranges = []
            for pos_range in pos_ranges:
                mapped_ranges += m.get_destination_from_range(
                    start=pos_range[0], end=pos_range[1]
                )
            pos_ranges = mapped_ranges

        positions += [min(pos_ranges, key=lambda x: x[0])]

    return min(positions)[0]


if __name__ == "__main__":
    print(f"One star test solution is {one_star(TEST_FILE)}")
    print(f"Two star test solution is {two_star(TEST_FILE)}")
    print(f"One star solution is {one_star(INPUT_FILE)}")
    print(f"Two star solution is {two_star(INPUT_FILE)}")
