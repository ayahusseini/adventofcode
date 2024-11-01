import pytest
from day_14 import load_file, TEST_FILE, get_pairs, generate_next_item


@pytest.fixture
def template():
    return "NNCB"


@pytest.fixture
def rules():
    return {'CH': 'B', 'HH': 'N', 'CB': 'H', 'NH': 'C', 'HB': 'C', 'HC': 'B', 'HN': 'C', 'NN': 'C', 'BH': 'H', 'NC': 'B', 'NB': 'B', 'BN': 'B', 'BB': 'N', 'BC': 'B', 'CC': 'N', 'CN': 'C'}


def test_load_file():
    template, rules = load_file(TEST_FILE)
    assert template == "NNCB"
    assert rules["CH"] == "B"


def test_get_pairs(template):
    assert get_pairs(template) == ["NN", "NC", "CB"]


def test_generate_next_item(template, rules):
    assert ''.join(generate_next_item(template, rules)) == "NCNBCHB"
