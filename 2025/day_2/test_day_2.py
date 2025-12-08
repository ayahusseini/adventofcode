import pytest

from day_2 import is_repeated_twice


@pytest.mark.parametrize("id, ans", [
    (55, True), (6464, True), (123123, True),
    (95, False), (11, True), (111, False),
    (1010, True), (1188511885, True), (222222, True),
    (2223, False), (0, False)
])
def test_is_repeated_twice(id, ans):
    assert is_repeated_twice(id) == ans
