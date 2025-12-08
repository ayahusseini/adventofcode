import pytest
from unittest.mock import patch

from day_5 import load_file_lines, map_lines_to_vectors, find_coverage

TEST_FILE = "inputs/day_5_test.txt"


@pytest.fixture
def file_lines():
    return [
        "0,9 -> 5,9",
        "8,0 -> 0,8",
        "9,4 -> 3,4",
        "2,2 -> 2,1",
        "7,0 -> 7,4",
        "6,4 -> 2,0",
        "0,9 -> 2,9",
        "3,4 -> 1,4",
        "0,0 -> 8,8",
        "5,5 -> 8,2",
    ]


@pytest.fixture
def endpoints():
    return [
        [[0, 9], [5, 9]],
        [[8, 0], [0, 8]],
        [[9, 4], [3, 4]],
        [[2, 2], [2, 1]],
        [[7, 0], [7, 4]],
        [[6, 4], [2, 0]],
        [[0, 9], [2, 9]],
        [[3, 4], [1, 4]],
        [[0, 0], [8, 8]],
        [[5, 5], [8, 2]],
    ]


def test_get_endpoints_gives_expected_result(file_lines, endpoints):
    assert map_lines_to_vectors(file_lines) == endpoints


@pytest.mark.parametrize(
    "start, end, coverage",
    [
        ([0, 1], [0, 2], [(0, 1), (0, 2)]),
        ([0, 1], [0, 3], [(0, 1), (0, 2), (0, 3)]),
        ([1, 1], [1, 3], [(1, 1), (1, 2), (1, 3)]),
        ([1, 1], [3, 1], [(1, 1), (2, 1), (3, 1)]),
        ([1, 1], [1, 1], [(1, 1)]),
        ([7, 1], [3, 1], [(3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]),
    ],
)
def test_find_coverage(start, end, coverage):
    assert find_coverage(start, end) == coverage


@pytest.mark.parametrize(
    "start, end, coverage",
    [
        ([0, 1], [1, 2], [(0, 1), (1, 2)]),
        ([0, 1], [1, 0], [(0, 1), (1, 0)]),
        ([1, 1], [3, 3], [(1, 1), (2, 2), (3, 3)]),
        ([9, 7], [7, 9], [(7, 9), (8, 8), (9, 7)]),
    ],
)
def test_find_coverage_for_diagonals(start, end, coverage):
    assert find_coverage(start, end, ignore_diagonals=False) == coverage
