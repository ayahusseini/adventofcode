import pytest
from day_8 import get_num_characters_of_string, load_file
TEST_INPUT = "inputs/day_8_test_input.txt"


@pytest.fixture
def test_input_lines():
    return load_file(TEST_INPUT)


def test_get_num_characters_of_string1(test_input_lines):
    assert get_num_characters_of_string(test_input_lines[0]) == 0


def test_get_num_characters_of_string2(test_input_lines):
    assert get_num_characters_of_string(test_input_lines[1]) == 3


def test_get_num_characters_of_string3(test_input_lines):
    assert get_num_characters_of_string(test_input_lines[2]) == 7


def test_get_num_characters_of_string4(test_input_lines):
    assert get_num_characters_of_string(test_input_lines[3]) == 1
