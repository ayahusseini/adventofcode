import pytest

from day_3 import get_rucksacks, get_compartments, get_match

TEST_FILE = "inputs/day_3_test.txt"


def test_file_load():
    assert get_rucksacks(TEST_FILE) == ["vJrwpWtwJgWrhcsFMMfFFhFp",
                                        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
                                        "PmmdzqPrVvPwwTWBwg", "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", "ttgJtRGJQctTZtZT", "CrZsJsPPZsGzwwsLwLmpwMDw"]


@pytest.mark.parametrize("l,expected", [
    ("vJrwpWtwJgWrhcsFMMfFFhFp", [
     "vJrwpWtwJgWr", "hcsFMMfFFhFp"]), ("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", ["jqHRNqRjqzjGDLGL", "rsFMfFZSrLrFZsSL"]), ("1234", ["12", "34"])
])
def test_get_rucksack_compartments(l, expected):
    assert get_compartments(l) == expected


@pytest.mark.parametrize("l,expected", [
    ([
     "vJrwpWtwJgWr", "hcsFMMfFFhFp"], "p"),
    (["jqHRNqRjqzjGDLGL", "rsFMfFZSrLrFZsSL"], "L"),
    (["123", "1"], "1")
])
def test_matches(l, expected):
    assert get_match(l) == expected


@pytest.mark.parametrize("l", [
    ([
     "vJrwpWtwJgWrph", "hcsFMMfFFhFp"]),
    (["jqHRNqRjqzjGDLGLr", "rsFMfFZSrLrFZsSL"]),
    (["23", "1"])
])
def test_matches_raises_error_if_more_than_1(l):
    with pytest.raises(ValueError):

        get_match(l)
