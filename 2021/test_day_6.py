import pytest

from day_6 import simulate_day, simulate_n_days


@pytest.mark.parametrize("current_state,next_state", [
    ([3, 4, 3, 1, 2], [2, 3, 2, 0, 1]),
    ([2, 3, 2, 0, 1], [1, 2, 1, 6, 0, 8]),
    ([0, 1, 0, 5, 6, 0, 1, 2, 2, 3, 7, 8], [
     6, 0, 6, 4, 5, 6, 0, 1, 1, 2, 6, 7, 8, 8, 8]),
    ([0, 1, 0, 5, 6, 0, 1, 2, 2, 3, 0, 1, 2, 2, 2, 3, 3, 4, 4, 5, 7, 8], [6, 0, 6, 4, 5, 6, 0, 1, 1, 2, 6, 0, 1, 1, 1, 2, 2, 3, 3, 4, 6, 7, 8, 8, 8, 8
                                                                          ])
])
def test_simulate_one_day(current_state, next_state):
    assert simulate_day(current_state) == next_state


@pytest.mark.parametrize("num_days,expected_state", [
    (0, [3, 4, 3, 1, 2]),
    (1, [2, 3, 2, 0, 1]),
    (2, [1, 2, 1, 6, 0, 8]),
    (11, [
     6, 0, 6, 4, 5, 6, 0, 1, 1, 2, 6, 7, 8, 8, 8]),
    (18, [6, 0, 6, 4, 5, 6, 0, 1, 1, 2, 6, 0, 1, 1, 1, 2, 2, 3, 3, 4, 6, 7, 8, 8, 8, 8
          ])
])
def test_simulate_n_days(num_days, expected_state):
    assert simulate_n_days(num_days, [3, 4, 3, 1, 2]) == expected_state
