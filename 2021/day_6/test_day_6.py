import pytest

from day_6 import update_state_one_day, update_state_n_days


@pytest.mark.parametrize("initial_state, final_state", [
    ([3, 4, 3, 1, 2], [2, 3, 2, 0, 1]),
    ([1, 2, 1, 6, 0, 8], [0, 1, 0, 5, 6, 7, 8]),
    ([0, 1, 0, 5, 6, 0, 1, 2, 2, 3, 7, 8], [
     6, 0, 6, 4, 5, 6, 0, 1, 1, 2, 6, 7, 8, 8, 8]),
    ([0, 1, 0, 5, 6, 0, 1, 2, 2, 3, 0, 1, 2, 2, 2, 3, 3, 4, 4, 5, 7, 8], [6, 0, 6, 4, 5, 6, 0, 1, 1, 2, 6, 0, 1, 1, 1, 2, 2, 3, 3, 4, 6, 7, 8, 8, 8, 8
                                                                          ])
])
def test_state_updates(initial_state, final_state):
    assert update_state_one_day({i: initial_state.count(i) for i in initial_state}) == {
        i: final_state.count(i) for i in final_state}


@pytest.mark.parametrize("initial_state, final_state,n", [
    ([3, 4, 3, 1, 2], [3, 4, 3, 1, 2], 0),
    ([3, 4, 3, 1, 2], [2, 3, 2, 0, 1], 1),
    ([3, 4, 3, 1, 2], [1, 2, 1, 6, 0, 8], 2),
    ([3, 4, 3, 1, 2], [0, 1, 0, 5, 6, 7, 8], 3),
    ([3, 4, 3, 1, 2], [6, 0, 6, 4, 5, 6, 0, 1, 1, 2, 6,
     0, 1, 1, 1, 2, 2, 3, 3, 4, 6, 7, 8, 8, 8, 8], 18)
])
def test_state_updates_after_n_days(initial_state, final_state, n):
    assert update_state_n_days({i: initial_state.count(i) for i in initial_state}, n) == {
        i: final_state.count(i) for i in final_state}
