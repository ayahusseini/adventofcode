import pytest
from day_14 import load_file, TEST_FILE, get_pairs


def test_load_file():
    template, rules = load_file(TEST_FILE)
    assert template == "NNCB"
    assert rules["CH"] == "B"


def test_get_pairs():
    assert get_pairs("NNCB") == ["NN", "NC", "CB"]
