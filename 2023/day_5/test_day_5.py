import pytest
from day_5 import split_range


def test_split_range1():
	assert split_range((1, 2), (2, 3)) == (tuple(), (1, 2))


def test_split_range2():
	assert split_range((0, 0), (2, 3)) == (tuple(), (0, 0))


def test_split_range3():
	assert split_range((0, 1), (-1, 3)) == ((0, 1), tuple())


def test_split_range4():
	assert split_range((1, 10), (1, 3)) == ((1, 3), (3, 10))
