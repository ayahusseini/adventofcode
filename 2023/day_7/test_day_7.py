import pytest
from day_7 import sort_hands_by_strength, rank_hands


@pytest.fixture
def hands():
    return ["32T3K", "T55J5", "KK677", "KTJJT", "QQQJA"]


def test_sort_hands_by_strength():
    assert sort_hands_by_strength(["KK677", "KTJJT"]) == [
        "KK677", "KTJJT"][::-1]


def test_sort_hands_by_strength():
    assert sort_hands_by_strength(["QQQJA", "T55J5"]) == [
        "T55J5", "QQQJA"]


def test_rank_hands(hands):
    assert rank_hands(hands) == ["32T3K", "KTJJT", "KK677", "T55J5", "QQQJA"]
