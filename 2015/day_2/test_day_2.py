import pytest

from day_2 import (
	get_surface_area,
	get_smallest_side_area,
	get_dimensions_from_string,
	get_smallest_side_perimeter,
)


@pytest.mark.parametrize('l,w,h,area', [(1, 1, 1, 6), (2, 3, 4, 52), (1, 1, 10, 42)])
def test_surface_area(l, w, h, area):
	assert get_surface_area(l, w, h) == area


@pytest.mark.parametrize('l,w,h,area', [(1, 1, 1, 1), (2, 3, 4, 6), (1, 1, 10, 1)])
def test_smallest_side(l, w, h, area):
	assert get_smallest_side_area(l, w, h) == area


@pytest.mark.parametrize('string, out', [('2x3x4', (2, 3, 4))])
def test_smallest_side(string, out):
	assert get_dimensions_from_string(string) == out


@pytest.mark.parametrize('l,w,h,smallest', [(1, 1, 1, 4), (2, 3, 4, 10), (1, 1, 10, 4)])
def test_smallest_perimeter(l, w, h, smallest):
	assert get_smallest_side_perimeter(l, w, h) == smallest
