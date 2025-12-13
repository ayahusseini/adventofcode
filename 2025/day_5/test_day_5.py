import pytest

from day_5 import load_file, TEST_FILE, merge_two_ranges, merge_all_ranges


@pytest.fixture
def sample_data():
	return load_file(TEST_FILE)


@pytest.mark.parametrize(
	'r1,r2,exp',
	[
		([1, 2], [2, 3], [[1, 3]]),
		([1, 2], [3, 5], [[1, 5]]),
		([0, 0], [2, 3], [[0, 0], [2, 3]]),
		([0, 0], [1, 5], [[0, 5]]),
	],
)
def test_merge_two_ranges(r1, r2, exp):
	assert merge_two_ranges(r1, r2) == exp


@pytest.mark.parametrize(
	'r,exp',
	[
		([[1, 2]], [[1, 2]]),
		([], []),
		([[1, 2], [2, 3], [2, 5], [10, 20]], [[1, 5], [10, 20]]),
		([[11, 12], [1, 1], [-10, 1]], [[-10, 1], [11, 12]]),
	],
)
def test_merge_all_ranges(r, exp):
	assert merge_all_ranges(r) == exp
