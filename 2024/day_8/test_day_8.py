"""Tests for day 8"""
import pytest
from day_8 import get_antinode_positions


@pytest.mark.parametrize("pos1, pos2, expected1, expected2", [
    ((2, 1), (4, 2), (0, 0), (6, 3))
])
def test_get_antinode_positions(pos1, pos2, expected1, expected2):
    assert get_antinode_positions(pos1, pos2) == (expected1, expected2)
