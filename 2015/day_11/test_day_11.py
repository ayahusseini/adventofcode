from day_10 import transform_string


def test_transform():
    assert transform_string("1") == "11"


def test_transform2():
    assert transform_string("11") == "21"


def test_transform3():
    assert transform_string("21") == "1211"


def test_transform4():
    assert transform_string("1211") == "111221"


def test_transform5():
    assert transform_string("111221") == "312211"
