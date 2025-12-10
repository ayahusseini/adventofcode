import pytest

from day_2 import get_upper_half_pattern_bound, get_lower_half_pattern_bound, get_all_possible_invalid_ids, get_all_multiples


@pytest.mark.parametrize("n, exp",
                         [
                             (2, [1, 2]),
                             (3, [1, 3]),
                             (5, [1, 5]),
                             (10, [1, 2, 5, 10])

                         ])
def test_get_all_multiples(n, exp):
    assert set(get_all_multiples(n)) == set(exp)


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
                             (1698522, 1698528, 2, []),
                             (998, 1012, 3, [999]),
                             (824824821, 824824827, 3, [824824824]),
                         ])
def test_get_upper_half_pattern_bound(s, e, nreps, exp):
    assert get_all_possible_invalid_ids(s, e, nreps) == exp


def test_large_range():
    rng = (2121212118, 2121212124)
    ndigits = (len(str(rng[0])), len(str(rng[1])))
    if ndigits[0] == ndigits[1]:
        possible_reps = get_all_multiples(ndigits[0])
    else:
        possible_reps = get_all_multiples(
            ndigits[0]) + get_all_multiples(ndigits[1])
    assert set(possible_reps) == set([1, 10, 2, 5])

    total = 0
    for nreps in set(possible_reps):
        if nreps == 1:
            continue
        total += sum(get_all_possible_invalid_ids(rng[0], rng[1], nreps))
    assert total == 2121212121


def test_multi_digit_range():
    rng = (95, 115)
    ndigits = (len(str(rng[0])), len(str(rng[1])))
    if ndigits[0] == ndigits[1]:
        possible_reps = get_all_multiples(ndigits[0])
    else:
        possible_reps = get_all_multiples(
            ndigits[0]) + get_all_multiples(ndigits[1])
    assert set(possible_reps) == set([1, 2, 3])

    total = 0
    for nreps in set(possible_reps):
        if nreps == 1:
            continue
        total += sum(get_all_possible_invalid_ids(rng[0], rng[1], nreps))
    assert total == 99 + 111


def test_multi_digit_range2():
    rng = (565653, 565659)
    ndigits = (len(str(rng[0])), len(str(rng[1])))
    if ndigits[0] == ndigits[1]:
        possible_reps = get_all_multiples(ndigits[0])
    else:
        possible_reps = get_all_multiples(
            ndigits[0]) + get_all_multiples(ndigits[1])
    total = []
    for nreps in set(possible_reps):
        if nreps == 1:
            continue
        total += get_all_possible_invalid_ids(rng[0], rng[1], nreps)
    assert set(total) == set([565656])


def test_single_digit_range():
    rng = (38593856, 38593862)
    ndigits = (len(str(rng[0])), len(str(rng[1])))
    if ndigits[0] == ndigits[1]:
        possible_reps = get_all_multiples(ndigits[0])
    else:
        possible_reps = get_all_multiples(
            ndigits[0]) + get_all_multiples(ndigits[1])
    total = []
    for nreps in set(possible_reps):
        if nreps == 1:
            continue
        total += get_all_possible_invalid_ids(rng[0], rng[1], nreps)
    assert set(total) == set([38593859])


def test_single_digit_range2():
    rng = (1188511880, 1188511890)
    ndigits = (len(str(rng[0])), len(str(rng[1])))
    if ndigits[0] == ndigits[1]:
        possible_reps = get_all_multiples(ndigits[0])
    else:
        possible_reps = get_all_multiples(
            ndigits[0]) + get_all_multiples(ndigits[1])
    total = []
    for nreps in set(possible_reps):
        if nreps == 1:
            continue
        total += get_all_possible_invalid_ids(rng[0], rng[1], nreps)
    assert set(total) == set([1188511885])
