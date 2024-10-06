from day_1 import first_text_digit


def test_first_text_digit():
    assert (first_text_digit("two1nine"))[0] == "2"


def test_first_text_digit2():
    assert (first_text_digit("eightwothree"))[0] == "8"


def test_first_text_digit3():
    assert (first_text_digit("4nineeightseven2"))[0] == "9"


def test_first_text_digit4():
    assert (first_text_digit("abcone2threexyz"))[0] == "1"
