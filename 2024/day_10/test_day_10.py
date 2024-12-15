import pytest
from day_10 import Grid


@pytest.fixture
def g1():
    lines = ["0123",
             "1234",
             "8765",
             "9876"]
    return Grid.from_lines(lines)


def test_grid_heights_loaded(g1):
    assert g1.heights[0, 0] == 0


def test_grid_trailheads_loaded(g1):
    assert g1.trailheads == {(0, 0)}
