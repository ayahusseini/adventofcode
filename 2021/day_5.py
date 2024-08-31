'''Solution to day 5 2021'''
import numpy as np

TEST_FILE = "inputs/day_5_test.txt"
INPUT_FILE = "inputs/day_5_input.txt"
COORDINATE_SEPARATOR = " -> "

# extract coordinates


def get_point_from_string(coords: str) -> list:
    '''Returns a coordinate as a list'''

    return [int(c) for c in coords.split(',')]


def split_line_coords(line: str) -> list[str]:
    '''Split a line into text representing the start and end coordinates'''
    return line.strip().split(COORDINATE_SEPARATOR)


def load_file_lines(filename: str) -> list[str]:
    '''Loads the file lines as a list'''

    with open(filename, "r") as f:
        lines = [l.replace("\n", "").strip() for l in f.readlines()]
    return lines


def map_lines_to_vectors(lines: list) -> list:
    '''Takes a list of strings representing a pair of coordinates, maps them into a list of coordinate pairs.'''

    return list(map(lambda line: [get_point_from_string(s)
                                  for s in split_line_coords(line)], lines))


# determine coverage


def find_coverage(start: list, end: list, ignore_diagonals: bool = True) -> list[tuple]:
    '''Returns a set of coordinates that start -> end would cover.'''

    for idx in (0, 1):

        if start[idx] == end[idx]:

            start, end = sorted([start, end], key=lambda coord: coord[idx-1])

            return [(start[idx], i) if idx == 0 else (i, start[idx]) for i in range(start[idx-1], end[idx-1]+1)
                    ]

    if not ignore_diagonals:
        # lowest horizontal coordinate is 'start'
        start, end = sorted([start, end], key=lambda coord: coord[0])

        vertical_step = -1 if start[1] > end[1] else 1
        return [(start[0] + i, start[1] + i*vertical_step) for i in range(0, end[0]-start[0]+1)]

    return []


def find_double_overlaps(point_pairs: list, ignore_diagonals: bool = True):
    '''Returns the list of points where lines overlap at least twice'''
    covered_once = set([])
    covered_more_than_once = set([])
    for pair in point_pairs:
        coverage = find_coverage(*pair, ignore_diagonals=ignore_diagonals)

        overlaps = covered_once.intersection(coverage)

        covered_more_than_once.update(overlaps)
        covered_once.update(set(coverage) - covered_once)

    return covered_more_than_once


def count_double_overlaps(filename: str, inc_diagonal: bool):
    '''Return the number of points where lines cross more than once'''
    lines = load_file_lines(filename)
    points_list = map_lines_to_vectors(lines)
    return len(find_double_overlaps(points_list, ignore_diagonals=not inc_diagonal))


if __name__ == "__main__":
    print(f"One star solution in test is {
          count_double_overlaps(TEST_FILE, False)}")
    print(f"Two star solution in test is {
          count_double_overlaps(TEST_FILE, True)}")
    print(f"One star solution is {
          count_double_overlaps(INPUT_FILE, False)}")
    print(f"Two star solution is {
          count_double_overlaps(INPUT_FILE, True)}")
