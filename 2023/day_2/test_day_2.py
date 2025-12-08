import pytest
from day_2 import get_id, get_subresult, Game


@pytest.mark.parametrize(
    "line, id",
    [
        ("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", 1),
        ("Game 11: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", 11),
    ],
)
def test_get_id(line, id):
    assert get_id(line) == id


@pytest.mark.parametrize(
    "line, subres",
    [
        ("3 blue, 4 red", {"blue": 3, "red": 4, "green": 0}),
        ("1 red, 2 green, 6 blue", {"red": 1, "green": 2, "blue": 6}),
    ],
)
def test_get_subresult(line, subres):
    assert get_subresult(line) == subres


def test_is_not_possible_from_line():
    g = Game.from_line(
        """Game 10: 16 green, 10 red; 13 green, 7 red; 8 red, 1 blue, 8 green"""
    )
    assert not g.is_possible(6, 100, 100)


def test_get_maxima():
    g = Game.from_line("""Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green""")
    assert g.get_max() == {"red": 4, "green": 2, "blue": 6}


def test_get_power():
    g = Game.from_line("""Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green""")
    assert g.get_power() == 48


def test_get_maxima2():
    g = Game.from_line(
        """Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue"""
    )
    assert g.get_max() == {"red": 1, "green": 3, "blue": 4}


def test_get_game_from_line():
    g = Game.from_line("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")
    assert g.id == 1
    assert g.subsets == [
        {"blue": 3, "red": 4, "green": 0},
        {"red": 1, "green": 2, "blue": 6},
        {"green": 2, "blue": 0, "red": 0},
    ]


def test_get_game_from_line_three_digit_id():
    g = Game.from_line("Game 111: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")
    assert g.id == 111
    assert g.subsets == [
        {"blue": 3, "red": 4, "green": 0},
        {"red": 1, "green": 2, "blue": 6},
        {"green": 2, "blue": 0, "red": 0},
    ]
