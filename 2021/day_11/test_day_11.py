import pytest

from day_11 import get_adjacent, get_flashed, get_all_idcs, get_item


@pytest.fixture
def grid1():
    return [[5, 4, 8, 3, 1, 4, 3, 2, 2, 3],
            [2, 7, 4, 5, 8, 5, 4, 7, 1, 1],
            [5, 2, 6, 4, 5, 5, 6, 1, 7, 3],
            [6, 1, 4, 1, 3, 3, 6, 1, 4, 6],
            [6, 3, 5, 7, 3, 8, 5, 4, 7, 8],
            [4, 1, 6, 7, 5, 2, 4, 6, 4, 5],
            [2, 1, 7, 6, 8, 4, 1, 7, 2, 1],
            [6, 8, 8, 2, 8, 8, 1, 1, 3, 4],
            [4, 8, 4, 6, 8, 4, 8, 5, 5, 4],
            [5, 2, 8, 3, 7, 5, 1, 5, 2, 6]]


@pytest.mark.parametrize(
    "x,y,dim,idcs",
    [
        (0, 0, 1, [(0, 0)]),
        (0, 0, 2, [(0, 1), (1, 0), (1, 1), (0, 0)]),
        (1, 1, 2, [(0, 1), (1, 0), (1, 1), (0, 0)]),
        (1, 1, 5, [
            (0, 0), (0, 1), (0, 2), (1, 1), (1, 0), (1, 2), (2, 1), (2, 0), (2, 2)
        ])
    ]
)
def test_adjacent_corner(x, y, dim, idcs):
    assert set(get_adjacent(x, y, dim)) == set(idcs)


def test_get_item():
    assert get_item(1, 1, [[0, 1], [2, 3]]) == 3


def test_get_flashed():
    assert get_flashed([
        [1, 10, 0],
        [2, 10, -1]]) == [(0, 1), (1, 1)]


def test_get_flashed_if_none_flashed():
    assert get_flashed([
        [1, 0, 0],
        [2, 0, -1]]) == []


def test_get_flashed_with_exclusion():
    assert get_flashed([[9, 1], [1, 1]], to_exclude=[(0, 0)]) == []
