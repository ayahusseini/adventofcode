import pytest
from day_8 import get_next_step


def test_next_step():
	sequence = get_next_step('RL')
	assert next(sequence) == 'R'
	assert next(sequence) == 'L'
	assert next(sequence) == 'R'
	assert next(sequence) == 'L'
