from math import exp
import pytest

from day_3 import TEST_FILE, load_file, get_next_digit, get_largest_num


@pytest.fixture
def mock_banks():
    return load_file(TEST_FILE)


@pytest.mark.parametrize(
    "idx, bank, room, exp",
    [
        (0, [1, 8, 9], 0, (2, 9)),
        (0, [9, 8, 1], 0, (0, 9)),
        (0, [1, 8, 9], 1, (1, 8)),
        (1, [1, 8, 9], 0, (2, 9)),
        (1, [9, 8, 1], 0, (1, 8)),
        (1, [1, 8, 9], 1, (1, 8)),
    ],
)
def test_get_next_digit(idx, bank, room, exp):
    assert get_next_digit(idx, bank, room) == exp


def test_get_next_digit_with_sample(mock_banks):
    assert get_next_digit(0, mock_banks[0], 1) == (0, 9)
    assert get_next_digit(1, mock_banks[0], 0) == (1, 8)
    assert get_next_digit(0, mock_banks[1], 1) == (0, 8)
    assert get_next_digit(1, mock_banks[1], 0) == (14, 9)


def test_get_largest_num_with_sample_and_length_2(mock_banks):
    expected = [98, 89, 78, 92]
    actual = []
    for b in mock_banks:
        actual += [get_largest_num(2, b)]
    assert actual == expected
