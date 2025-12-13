import pytest
import numpy as np

from day_6 import SquareGrid, extract_instruction


def test_extract_instruction():
	assert extract_instruction('turn on 0,0 through 999,999') == (
		'turn on',
		[0, 0, 999, 999],
	)


def test_switch_on():
	grid = SquareGrid(2)
	grid.operate('turn on', 0, 0, 1, 1)
	np.testing.assert_array_equal(grid.state, np.array([[1, 1], [1, 1]]))


def test_switch_on_2():
	grid = SquareGrid(2)
	grid.operate('turn on', 1, 1, 0, 1)
	np.testing.assert_array_equal(grid.state, np.array([[-1, 1], [-1, 1]]))


def test_switch_on_3():
	grid = SquareGrid(2)
	grid.operate('turn on', 0, 0, 1, 1)
	np.testing.assert_array_equal(grid.state, np.array([[1, 1], [1, 1]]))
