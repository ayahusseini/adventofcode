import pytest

from day_1 import (
	parse_instruction,
	get_new_position,
	passes_through_zero,
	get_full_rotations,
)


@pytest.fixture
def test_input():
	return [
		'L68',
		'L30',
		'R48',
		'L5',
		'R60',
		'L55',
		'L1',
		'L99',
		'R14',
		'L82',
	]


@pytest.fixture
def parsed_input():
	return [
		-68,
		-30,
		48,
		-5,
		60,
		-55,
		-1,
		-99,
		14,
		-82,
	]


def test_parse_instruction(test_input, parsed_input):
	for instruction, expected in zip(test_input, parsed_input):
		assert parse_instruction(instruction) == expected


@pytest.mark.parametrize(
	'pos, disp, expected',
	[
		(0, 5, False),
		(0, -5, False),
		(100, 0, False),
		(-100, 0, False),
		(0, 0, False),
		(99, 1, True),
		(100, -1, False),
		(101, -2, True),
		(1, -1, True),
		(-1, 1, True),
		(99, 1, True),
		(99, -101, True),
	],
)
def test_passes_through_zero(pos, disp, expected):
	assert passes_through_zero(pos, disp) == expected


@pytest.mark.parametrize(
	'disp, expected',
	[(100, 1), (0, 0), (-1, 0), (1, 0), (-100, 1), (-101, 1), (205, 2), (-205, 2)],
)
def test_full_rotations(disp, expected):
	assert get_full_rotations(disp) == expected
