import pytest

from day_2 import get_upper_half_pattern_bound, get_lower_half_pattern_bound, get_all_possible_invalid_ids


@pytest.mark.parametrize("maximum,nreps,exp",
                         [
                             (9999, 2, 99),
                             (99, 2, 9),
                             (100, 2, 9),
                             (0, 1, 0),
                             (0, 2, None)
                         ])
def test_get_upper_half_pattern_bound(maximum, nreps, exp):
    assert get_upper_half_pattern_bound(maximum, nreps) == exp


@pytest.mark.parametrize("minimum,nreps,exp",
                         [
                             (9999, 2, 99),
                             (100, 2, 10),  # min is 1010
                             (0, 1, 0),
                             (0, 2, 1),  # min is 11
                             (1000, 2, 10),
                             (565653, 2, 566)
                         ])
def test_get_lower_half_pattern_bound(minimum, nreps, exp):
    assert get_lower_half_pattern_bound(minimum, nreps) == exp


@pytest.mark.parametrize("s,e,nreps,exp",
                         [
                             (11, 22, 2, [11, 22]),
                             (95, 115, 2, [99]),
                             (998, 1012, 2, [1010]),
                             (2121212118, 2121212124, 2, []),
                             (824824821, 824824827, 2, []),
                             (565653, 565659, 2, []),
                             (1188511880, 1188511890, 2, [1188511885]),
                             (222220, 222224, 2, [222222]),
                             (1698522, 1698528, 2, [])
                         ])
def test_get_upper_half_pattern_bound(s, e, nreps, exp):
    assert get_all_possible_invalid_ids(s, e, nreps) == exp
