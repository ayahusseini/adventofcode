"""Tests for day 8"""
import pytest
from day_8 import get_antinode_positions


@pytest.mark.parameterize
def test_get_antinode_positions(pos1, pos2, expected1, expected2)
