import pytest
from day_11 import increment_once, is_increasing_alphabetically, count_subsequences, is_matching, does_not_contain, is_valid_password


@pytest.mark.parametrize(
    "seq,exp",
    [("hijklmmn", False),
     ("abbceffg", False),
     ("abbcegjk", False),
     ("abcdffaa", True)])
def test_valid_pw(seq, exp):
    assert is_valid_password(seq) == exp


def test_does_not_contain():
    assert does_not_contain("abbceffg")


def test_does_not_contain_again():
    assert does_not_contain("abcdffaa")


def test_does_not_contain_empty():
    assert does_not_contain("")


def test_does_contain():
    assert not does_not_contain("abbceffgi")


def test_does_contain2():
    assert not does_not_contain("hijklmmn")


def test_matching():
    assert is_matching("aa")


def test_matching_empty():
    assert is_matching("")


def test_not_matching():
    assert not is_matching("aabc")


def test_alphabetic_increase():
    assert is_increasing_alphabetically("abc")


def test_alphabetic_increase2():
    assert is_increasing_alphabetically("xyz")


def test_not_alphabetic_increase1():
    assert not is_increasing_alphabetically("bdf")


def test_not_alphabetic_increase2():
    assert not is_increasing_alphabetically("yza")


def test_increment_once():
    assert increment_once("xx") == "xy"


def test_increment_once2():
    assert increment_once("xy") == "xz"


def test_increment_once3():
    assert increment_once("xz") == "ya"


def test_increment_once4():
    assert increment_once("ya") == "yb"


def test_increment_once_long_string():
    assert increment_once("zzzzz") == "a"*5


def test_increment_once_long_string2():
    assert increment_once("azzzzz") == "b"+"a"*5


def test_basic_count_subsequences_not_overlapping():
    assert count_subsequences(
        "aabbcc", 2, False, lambda x: x.count(x[0]) == len(x)) == 3


def test_basic_count_subsequences_not_overlapping2():
    assert count_subsequences(
        "aaabbcc", 2, False, lambda x: x.count(x[0]) == len(x)) == 3


def test_basic_count_subsequences_overlapping():
    assert count_subsequences(
        "aaa", 2, True, lambda x: x.count(x[0]) == len(x)) == 2


def test_basic_count_subsequences_overlapping2():
    assert count_subsequences(
        "aaa", 1, True, lambda x: True) == 3


def test_basic_count_subsequences_not_overlapping3():
    assert count_subsequences(
        "aaa", 1, True, lambda x: True) == 3


def test_basic_count_subsequences_overlapping3():
    assert count_subsequences(
        "aaabbcc", 2, True, lambda x: x.count(x[0]) == len(x)) == 4
