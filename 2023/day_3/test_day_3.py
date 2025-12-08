import pytest
from day_3 import Grid


@pytest.fixture
def testgrid():
    return Grid([["A", "*", "C"], ["D", "E", "F"], ["G", "*", "I"]])


@pytest.fixture
def numeric_grid():
    return Grid([["1", "2", "."], ["3", "4", "5"], [".", "*", "."]])


def test_extract_num(numeric_grid):
    assert numeric_grid.extract_full_num((0, 0)) == 12
    assert numeric_grid.extract_full_num((0, 1)) == 12


def test_extract_num_full(numeric_grid):
    assert numeric_grid.extract_full_num((1, 0)) == 345
    assert numeric_grid.extract_full_num((1, 1)) == 345
    assert numeric_grid.extract_full_num((1, 2)) == 345


def test_extract_num_none(numeric_grid):
    with pytest.raises(ValueError):
        numeric_grid.extract_full_num((2, 0))


@pytest.mark.parametrize(
    "grid, expected",
    [
        ([["4", "6", "7", ".", ".", "1", "1", "4", ".", "."]], []),
        ([["4", "*", "7", ".", ".", "1", "1", "4", ".", "."]], [(0, 1)]),
        ([["4", "*"], [".", "*"]], [(0, 1), (1, 1)]),
    ],
)
def test_get_symbol_idx_positions(grid, expected):
    assert Grid.get_symbol_idx(grid) == expected


def test_get_adjacent_middle(testgrid):
    assert set(testgrid.get_adjacent((1, 1))) == set(
        [(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)]
    )


def test_get_adjacent_edge(testgrid):
    assert set(testgrid.get_adjacent((0, 0))) == set([(0, 1), (1, 0), (1, 1)])
