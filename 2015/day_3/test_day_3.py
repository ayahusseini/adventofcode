import pytest

from day_3 import (
	map_instruction_to_direction,
	get_path,
	count_visits,
	split_instructions,
	two_star,
)
from unittest.mock import patch


def test_map_instruction_to_direction():
	assert map_instruction_to_direction() == {
		'>': [1, 0],
		'<': [-1, 0],
		'^': [0, 1],
		'v': [0, -1],
	}


@pytest.mark.parametrize(
	'instruction, expected_houses_visited',
	[
		('>', [(0, 0), (1, 0)]),
		('', [(0, 0)]),
		('^>v<', [(0, 0), (0, 1), (1, 1), (1, 0), (0, 0)]),
		('^v^v^', [(0, 0), (0, 1), (0, 0), (0, 1), (0, 0), (0, 1)]),
	],
)
def test_houses_visited(instruction, expected_houses_visited):
	assert get_path(instruction) == expected_houses_visited


@pytest.mark.parametrize(
	'instruction, expected_repeats', [('>', 2), ('', 1), ('^>v<', 4), ('^v^v^', 2)]
)
def test_count_repeats(instruction, expected_repeats):
	assert count_visits(instruction) == expected_repeats


@pytest.mark.parametrize(
	'instruction, expected',
	[
		('>', ('>', '')),
		('', ('', '')),
		('^>v<', ('^v', '><')),
		('^v^v^', ('^^^', 'vv')),
	],
)
def test_split(instruction, expected):
	assert split_instructions(instruction) == expected


@pytest.mark.parametrize(
	'instruction, expected',
	[('>', 2), ('', 1), ('^v', 3), ('^>v<', 3), ('^v^v^v^v^v', 11)],
)
@patch('day_3.load_file')
def test_two_star(fake_load_file, instruction, expected):
	fake_load_file.return_value = instruction
	assert two_star('fake_file') == expected
