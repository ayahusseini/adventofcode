import pytest
from day_10 import Grid


@pytest.fixture
def g1():
    lines = ["0123",
             "1234",
             "8765",
             "9876"]
    return Grid.from_lines(lines)


@pytest.fixture
def g2():
    lines = ["89010123",
             "78121874",
             "87430965",
             "96549874",
             "45678903",
             "32019012",
             "01329801",
             "10456732"]
    return Grid.from_lines(lines)


@pytest.mark.parametrize("trailhead, score", [
    ((0, 2), 5),
    ((0, 4), 6),
    ((2, 4), 5),
])
def test_trailhead_scores(g2, trailhead, score):
    print(g2.trailheads)
    assert g2.get_trailhead_scores()[trailhead] == score


def test_grid_heights_loaded(g1):
    assert g1.heights[0, 0] == 0


def test_grid_trailheads_loaded(g1):
    assert g1.trailheads == {(0, 0)}


@pytest.mark.parametrize("idx, neighbours", [
    ((0, 0), {(0, 1), (1, 0)}),
    ((3, 1), {(2, 1), (3, 0), (3, 2)})
])
def test_neighbours(g1, idx, neighbours):
    assert g1.get_neighbours(idx) == neighbours
