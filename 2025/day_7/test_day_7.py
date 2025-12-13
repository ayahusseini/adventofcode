import numpy as np
import pytest

from day_7 import TEST_FILE, load_file, num_ways_to_reach, num_ways_to_reach_next_row


@pytest.fixture
def mock_input():
	return load_file(TEST_FILE)


def test_load(mock_input):
	is_beam, is_splitter = mock_input
	print(is_beam)
	assert is_beam[0] == [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]


@pytest.mark.parametrize(
	'above, is_splitter, exp',
	[
		# No above beams
		([0, 0, 0], [1, 0, 0], 0),
		([0, 0, 0], [0, 0, 0], 0),
		# Central above beams
		([0, 1, 0], [1, 0, 0], 1),
		([0, 1, 0], [0, 1, 0], 0),
		([0, 2, 0], [1, 0, 0], 2),
		([0, 1, 0], [0, 1, 1], 0),
		# Left above beams
		([1, 0, 0], [1, 0, 0], 1),
		([1, 0, 0], [0, 1, 0], 0),
		([2, 0, 0], [1, 0, 0], 2),
		# Right above beams
		([0, 0, 2], [0, 1, 0], 0),
		([0, 0, 2], [0, 0, 1], 2),
		# Beams and multiple splitters
		([0, 0, 2], [1, 0, 1], 2),
		([3, 0, 2], [1, 0, 1], 5),
		([0, 1, 2], [0, 0, 1], 3),
	],
)
def test_num_ways_to_reach(above, is_splitter, exp):
	ways, splits = num_ways_to_reach(above, is_splitter)
	assert ways == exp


@pytest.mark.parametrize(
	'above, is_splitter, exp',
	[
		# No above beams
		([0, 0, 0], [1, 0, 0], [0, 0, 0]),
		([0, 0, 0], [0, 0, 0], [0, 0, 0]),
		# Central above beams
		([0, 1, 0], [1, 0, 0], [0, 1, 0]),
		([0, 1, 0], [0, 1, 0], [1, 0, 1]),
		([0, 2, 0], [1, 0, 0], [0, 2, 0]),
		([0, 1, 0], [0, 1, 1], [1, 0, 0]),
		# Left above beams
		([1, 0, 0], [1, 0, 0], [0, 1, 0]),
		([1, 0, 0], [0, 1, 0], [1, 0, 0]),
		([2, 0, 0], [1, 0, 0], [0, 2, 0]),
		# Right above beams
		([0, 0, 2], [0, 1, 0], [0, 0, 2]),
		([0, 0, 2], [0, 0, 1], [0, 2, 0]),
		# Beams and multiple splitters
		([0, 0, 2], [1, 0, 1], [0, 2, 0]),
		([3, 0, 2], [1, 0, 1], [0, 5, 0]),
		([0, 1, 2], [0, 0, 1], [0, 3, 0]),
		# Large row
		(
			[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
		),
	],
)
def test_num_ways_to_reach_next_row(above, is_splitter, exp):
	ways, splits = num_ways_to_reach_next_row(above, is_splitter)
	assert ways == exp
