import pytest

from day_11 import (
    get_adjacent,
    get_flashed,
    get_all_idcs,
    get_item,
    update_state,
    count_flashes,
)


@pytest.fixture
def grid2():
    return [[1, 1], [0, 1]]


@pytest.fixture
def grid2_update_once():
    return [[2, 2], [1, 2]]


@pytest.fixture
def grid1():
    return [
        [5, 4, 8, 3, 1, 4, 3, 2, 2, 3],
        [2, 7, 4, 5, 8, 5, 4, 7, 1, 1],
        [5, 2, 6, 4, 5, 5, 6, 1, 7, 3],
        [6, 1, 4, 1, 3, 3, 6, 1, 4, 6],
        [6, 3, 5, 7, 3, 8, 5, 4, 7, 8],
        [4, 1, 6, 7, 5, 2, 4, 6, 4, 5],
        [2, 1, 7, 6, 8, 4, 1, 7, 2, 1],
        [6, 8, 8, 2, 8, 8, 1, 1, 3, 4],
        [4, 8, 4, 6, 8, 4, 8, 5, 5, 4],
        [5, 2, 8, 3, 7, 5, 1, 5, 2, 6],
    ]


@pytest.fixture
def grid1_update_once():
    return [
        [6, 5, 9, 4, 2, 5, 4, 3, 3, 4],
        [3, 8, 5, 6, 9, 6, 5, 8, 2, 2],
        [6, 3, 7, 5, 6, 6, 7, 2, 8, 4],
        [7, 2, 5, 2, 4, 4, 7, 2, 5, 7],
        [7, 4, 6, 8, 4, 9, 6, 5, 8, 9],
        [5, 2, 7, 8, 6, 3, 5, 7, 5, 6],
        [3, 2, 8, 7, 9, 5, 2, 8, 3, 2],
        [7, 9, 9, 3, 9, 9, 2, 2, 4, 5],
        [5, 9, 5, 7, 9, 5, 9, 6, 6, 5],
        [6, 3, 9, 4, 8, 6, 2, 6, 3, 7],
    ]


@pytest.fixture
def grid1_update_twice():
    return [
        [8, 8, 0, 7, 4, 7, 6, 5, 5, 5],
        [5, 0, 8, 9, 0, 8, 7, 0, 5, 4],
        [8, 5, 9, 7, 8, 8, 9, 6, 0, 8],
        [8, 4, 8, 5, 7, 6, 9, 6, 0, 0],
        [8, 7, 0, 0, 9, 0, 8, 8, 0, 0],
        [6, 6, 0, 0, 0, 8, 8, 9, 8, 9],
        [6, 8, 0, 0, 0, 0, 5, 9, 4, 3],
        [0, 0, 0, 0, 0, 0, 7, 4, 5, 6],
        [9, 0, 0, 0, 0, 0, 0, 8, 7, 6],
        [8, 7, 0, 0, 0, 0, 6, 8, 4, 8],
    ]


@pytest.fixture
def grid1_update_thrice():
    return [
        [0, 0, 5, 0, 9, 0, 0, 8, 6, 6],
        [8, 5, 0, 0, 8, 0, 0, 5, 7, 5],
        [9, 9, 0, 0, 0, 0, 0, 0, 3, 9],
        [9, 7, 0, 0, 0, 0, 0, 0, 4, 1],
        [9, 9, 3, 5, 0, 8, 0, 0, 6, 3],
        [7, 7, 1, 2, 3, 0, 0, 0, 0, 0],
        [7, 9, 1, 1, 2, 5, 0, 0, 0, 9],
        [2, 2, 1, 1, 1, 3, 0, 0, 0, 0],
        [0, 4, 2, 1, 1, 2, 5, 0, 0, 0],
        [0, 0, 2, 1, 1, 1, 9, 0, 0, 0],
    ]


@pytest.mark.parametrize(
    "x,y,dim,idcs",
    [
        (0, 0, 1, [(0, 0)]),
        (0, 0, 2, [(0, 1), (1, 0), (1, 1), (0, 0)]),
        (1, 1, 2, [(0, 1), (1, 0), (1, 1), (0, 0)]),
        (
            1,
            1,
            5,
            [(0, 0), (0, 1), (0, 2), (1, 1), (1, 0), (1, 2), (2, 1), (2, 0), (2, 2)],
        ),
    ],
)
def test_adjacent_corner(x, y, dim, idcs):
    assert set(get_adjacent(x, y, dim)) == set(idcs)


def test_get_item():
    assert get_item((1, 1), [[0, 1], [2, 3]]) == 3


def test_get_flashed():
    assert get_flashed([[1, 10, 0], [2, 10, -1]]) == [(0, 1), (1, 1)]


def test_get_flashed_if_none_flashed():
    assert get_flashed([[1, 0, 0], [2, 0, -1]]) == []


def test_get_flashed_with_exclusion():
    assert get_flashed([[9, 1], [1, 1]], to_exclude=[(0, 0)]) == []


def test_update_state(grid1, grid1_update_once):
    update_state(grid1)
    assert grid1 == grid1_update_once


def test_update_state_twice(grid1, grid1_update_twice):
    update_state(grid1)
    update_state(grid1)
    assert grid1 == grid1_update_twice


def test_update_state_small(grid2, grid2_update_once):
    update_state(grid2)
    assert grid2 == grid2_update_once


def test_update_state_thrice(grid1, grid1_update_thrice):
    update_state(grid1)
    update_state(grid1)
    update_state(grid1)
    assert grid1 == grid1_update_thrice


def test_count_flashes_works(grid1):
    assert count_flashes(grid1, 10) == 204


def test_count_flashes_100_steps(grid1):
    assert count_flashes(grid1, 100) == 1656


def test_count_zero_flashes(grid2):
    assert count_flashes(grid2, 1) == 0


def test_count_flashes_after_zero_steps(grid2):
    assert count_flashes(grid2, 0) == 0
