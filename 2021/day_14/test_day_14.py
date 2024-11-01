import pytest
from day_14 import load_file, TEST_FILE


def test_load_file():
    template, rules = load_file(TEST_FILE)
    assert template == "NNCB"
    assert rules[0] == ["CH", "B"]
