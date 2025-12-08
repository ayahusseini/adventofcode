import pytest

from day_9 import (
    get_array,
    is_point_min,
    get_adjacent_indeces,
    find_minima,
    find_size_of_basin_around_min_point,
)


@pytest.fixture
def height():
    return ["2199943210", "3987894921", "9856789892", "8767896789", "9899965678"]


@pytest.fixture
def arr():
    return [
        [2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
        [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
        [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
        [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
        [9, 8, 9, 9, 9, 6, 5, 6, 7, 8],
    ]


@pytest.mark.parametrize(
    "r,c,expected_size", [(0, 1, 3), (2, 2, 14), (0, 9, 9), (4, 9, 9)]
)
def test_find_size_of_basin(r, c, expected_size, arr):
    assert find_size_of_basin_around_min_point(r, c, arr) == expected_size


def test_height_as_array(height, arr):
    assert get_array(height) == arr


@pytest.mark.parametrize(
    "r,c,expected",
    [
        (0, 0, [(1, 0), (0, 1)]),
        (0, 1, [(1, 1), (0, 0), (0, 2)]),
        (2, 2, [(1, 2), (3, 2), (2, 1), (2, 3)]),
    ],
)
def test_get_adjacent(r, c, expected, arr):
    assert set(get_adjacent_indeces(r, c, arr)) == set(expected)


@pytest.mark.parametrize(
    "r,c,expected",
    [
        (4, 0, False),
        (4, 1, False),
        (3, 1, False),
        (0, 0, False),
        (0, 1, True),
        (2, 2, True),
        (0, 9, True),
    ],
)
def test_is_min(r, c, expected, arr):
    assert is_point_min(r, c, arr) == expected


def test_find_minima(arr):
    assert find_minima(arr)[0].sort() == [1, 0, 5, 5].sort()
