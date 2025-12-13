import numpy as np
import pytest

from day_4 import get_true_neighbour_count


@pytest.mark.parametrize(
	'arr, expected',
	[
		(
			np.array(
				[
					[0, 1, 0],
					[1, 1, 0],
					[0, 0, 1],
				]
			),
			np.array(
				[
					[3, 2, 2],
					[2, 3, 3],
					[2, 3, 1],
				]
			),
		),
		(np.array([[0, 1, 0]]), np.array([[1, 0, 1]])),
	],
)
def test_true_neighbour_count(arr, expected):
	"""get_true_neighbour_count counts orthogonal neighbours"""
	np.testing.assert_array_equal(get_true_neighbour_count(arr), expected)
