import pytest

from day_4 import is_complete_overlap, get_pairs, load_file

INPUT_FILE = 'inputs/day_4_input.txt'


@pytest.fixture
def input1():
	return get_pairs(load_file(INPUT_FILE))


@pytest.fixture
def example_lines():
	return ['2-4,6-8', '2-3,4-5', '5-7,7-9', '2-8,3-7', '6-6,4-6', '2-6,4-8']


@pytest.fixture
def example_pairs():
	return [
		[[2, 4], [6, 8]],
		[[2, 3], [4, 5]],
		[[5, 7], [7, 9]],
		[[2, 8], [3, 7]],
		[[6, 6], [4, 6]],
		[[2, 6], [4, 8]],
	]


def test_pairs(example_lines, example_pairs):
	assert get_pairs(example_lines) == example_pairs


@pytest.mark.parametrize(
	'range1,range2,expected',
	[
		([2, 4], [6, 8], False),
		([6, 8], [2, 4], False),
		([-3, 0], [-2, -1], True),
		([6, 6], [4, 6], True),
		([2, 8], [3, 7], True),
		([1, 1], [1, 1], True),
		([1, 82], [1, 82], True),
		([5, 7], [7, 9], False),
		([6, 22], [6, 17], True),
		([24, 92], [25, 93], False),
	],
)
def test_complete_overlap(range1, range2, expected):
	assert is_complete_overlap(range1, range2) == expected


def test_correct_num_pairs(input1):
	assert len(input1) == 1000


def test_all_pairs(input1):
	assert all(len(p) == 2 for p in input1)
