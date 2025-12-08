import pytest

from day_3 import (
    get_rucksacks,
    get_compartments,
    get_match,
    get_alphabetic_position,
    get_priority,
    group_into_three,
)

TEST_FILE = "inputs/day_3_test.txt"


@pytest.fixture
def rucksacks():
    return [
        "vJrwpWtwJgWrhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg",
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
        "ttgJtRGJQctTZtZT",
        "CrZsJsPPZsGzwwsLwLmpwMDw",
    ]


def test_file_load(rucksacks):
    assert get_rucksacks(TEST_FILE) == rucksacks


@pytest.mark.parametrize(
    "l,expected",
    [
        ("vJrwpWtwJgWrhcsFMMfFFhFp", ["vJrwpWtwJgWr", "hcsFMMfFFhFp"]),
        ("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", ["jqHRNqRjqzjGDLGL", "rsFMfFZSrLrFZsSL"]),
        ("1234", ["12", "34"]),
    ],
)
def test_get_rucksack_compartments(l, expected):
    assert get_compartments(l) == expected


@pytest.mark.parametrize(
    "l,expected",
    [
        (["vJrwpWtwJgWr", "hcsFMMfFFhFp"], "p"),
        (["jqHRNqRjqzjGDLGL", "rsFMfFZSrLrFZsSL"], "L"),
        (["123", "1"], "1"),
        (["1234", "1pl", "1kl"], "1"),
        (
            [
                "vJrwpWtwJgWrhcsFMMfFFhFp",
                "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
                "PmmdzqPrVvPwwTWBwg",
            ],
            "r",
        ),
    ],
)
def test_matches(l, expected):
    assert get_match(l) == expected


@pytest.mark.parametrize(
    "l",
    [
        (["vJrwpWtwJgWrph", "hcsFMMfFFhFp"]),
        (["jqHRNqRjqzjGDLGLr", "rsFMfFZSrLrFZsSL"]),
        (["23", "1"]),
    ],
)
def test_matches_raises_error_if_more_than_1(l):
    with pytest.raises(ValueError):
        get_match(l)


ALPHABET = "abcdefghijklmnopqrstuvwxyz"
POSITIONS = [(l, i + 1) for i, l in enumerate(ALPHABET)]
POSITIONS_UPPERCASE = [(l, i + 1) for i, l in enumerate(ALPHABET.upper())]


@pytest.mark.parametrize("letter,pos", POSITIONS)
def test_get_alphabetic_position(letter, pos):
    assert get_alphabetic_position(letter) == pos


@pytest.mark.parametrize("letter,pos", POSITIONS_UPPERCASE)
def test_get_alphabetic_position_uppercase(letter, pos):
    assert get_alphabetic_position(letter) == pos


@pytest.mark.parametrize("letter,priority", [("p", 16), ("L", 38)])
def test_priority(letter, priority):
    assert get_priority(letter) == priority


@pytest.mark.parametrize(
    "l,groups",
    [
        (["1", "2", "3", "4"], [["1", "2", "3"], ["4"]]),
        (["1", "2", "3", "4", "5", "6"], [["1", "2", "3"], ["4", "5", "6"]]),
        (["1", "2", "3"], [["1", "2", "3"]]),
        (["1"], [["1"]]),
        ([], [[]]),
    ],
)
def test_group_into_3(l, groups):
    assert group_into_three(l) == groups


def test_group_into_3_with_testfile(rucksacks):
    g = group_into_three(rucksacks)
    assert g[0] == [
        "vJrwpWtwJgWrhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg",
    ]
    assert g[1] == [
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
        "ttgJtRGJQctTZtZT",
        "CrZsJsPPZsGzwwsLwLmpwMDw",
    ]
