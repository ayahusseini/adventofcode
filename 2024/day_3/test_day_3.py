import pytest
from day_3 import (
	extract_multiplication_instructions,
	read_conditional_instructions,
	MULTIPLICATION_PATTERN,
	CONDITIONAL_MULTIPLICATION_PATTERN,
)


@pytest.fixture
def conditional_line():
	return "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"


@pytest.mark.parametrize(
	'line,instructions',
	[
		(
			'xmul(2,4)%&mul[3,7]!@ ^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))',
			[('2', '4'), ('5', '5'), ('11', '8'), ('8', '5')],
		),
		('mul(a,b)', []),
		('mul(11,20)', [('11', '20')]),
	],
)
def test_find_mul_instructions(line, instructions):
	assert extract_multiplication_instructions(line, MULTIPLICATION_PATTERN) == instructions


def test_conditional_instructions(conditional_line):
	instructions = extract_multiplication_instructions(
		conditional_line, CONDITIONAL_MULTIPLICATION_PATTERN
	)
	assert read_conditional_instructions(instructions) == 48
