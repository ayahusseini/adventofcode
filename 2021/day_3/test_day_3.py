import pytest

from day_3 import (
    extract_report,
    convert_binary_to_decimal,
    get_most_freq_nth_letter,
    get_gamma_rate,
    get_epsilon_rate,
    get_filtered_down,
)

TEST_FILE = "inputs/day_3_test_input.txt"


@pytest.fixture
def test_binary():
    return """00100,11110,10110,10111,10101,01111,00111,11100,10000,11001,00010,01010""".split(
        ","
    )


@pytest.mark.parametrize("bin,expected", [("10110", 22), ("01001", 9)])
def test_bin_to_decimal(bin, expected):
    assert convert_binary_to_decimal(bin) == expected


def test_extract_report(test_binary):
    print(test_binary)
    assert extract_report(TEST_FILE) == test_binary


@pytest.mark.parametrize(
    "n,expected", [(0, "1"), (1, "0"), (2, "1"), (3, "1"), (4, "0")]
)
def test_most_frequent_nth_letter(n, expected, test_binary):
    assert get_most_freq_nth_letter(test_binary, n) == expected


def test_get_gamma_rate(test_binary):
    assert get_gamma_rate(test_binary) == 22


def test_get_epsilon_rate(test_binary):
    assert get_epsilon_rate(test_binary) == 9


def test_get_oxygen_rate_in_binary(test_binary):
    assert get_filtered_down(test_binary, opposite=False) == "10111"


def test_get_co2_rate_in_binary(test_binary):
    assert get_filtered_down(test_binary, opposite=True) == "01010"
