import pytest

from day_1 import parse_instruction, get_new_position


@pytest.fixture
def test_input():
    return [
        "L68",
        "L30",
        "R48",
        "L5",
        "R60",
        "L55",
        "L1",
        "L99",
        "R14",
        "L82",
    ]


@pytest.fixture
def parsed_input():
    return [
        -68,
        -30,
        48,
        -5,
        60,
        -55,
        -1,
        -99,
        14,
        -82,
    ]


def test_parse_instruction(test_input, parsed_input):
    for instruction, expected in zip(test_input, parsed_input):
        assert parse_instruction(instruction) == expected


@pytest.mark.parametrize("position, displacement, expected", [
    (50, -68, 82),
    (82, -30, 52),
    (55, -55, 0),
    (0, -1, 99),
    (0, 14, 14)
])
def test_get_new_position(position, displacement, expected):
    assert get_new_position(position, displacement) == expected
