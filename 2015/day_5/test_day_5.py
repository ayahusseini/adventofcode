import pytest
from day_5 import is_three_vowels, one_letter_twice, doesnt_contain_invalid


def test_invalid_string():
	assert doesnt_contain_invalid('haegwjzuvuyypxyu') == False


def test_one_letter_twice():
	assert one_letter_twice('aa') == True


def test_one_letter_twice_gives_false():
	assert one_letter_twice('abcabc') == False


def test_at_least_three_vowels():
	assert is_three_vowels('ugknbfddgicrmopn') == True


def test_at_least_three_vowels_if_invalid():
	assert is_three_vowels('aa') == False
