from day_4 import Card


def test_from_line():
    c = Card.from_line("Card 1: 41 48    83 86 17 | 83 86  6 31 17  9 48 53")
    assert c.card_num == 1
    assert c.winning == [41, 48, 83, 86, 17]
    assert c.nums == [83, 86,  6, 31, 17,  9, 48, 53]
