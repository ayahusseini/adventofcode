import pytest
from day_14 import load_file, TEST_FILE, get_pair_counter, implement_step


@pytest.fixture
def template():
	return 'NNCB'


@pytest.fixture
def rules():
	return {
		'CH': 'B',
		'HH': 'N',
		'CB': 'H',
		'NH': 'C',
		'HB': 'C',
		'HC': 'B',
		'HN': 'C',
		'NN': 'C',
		'BH': 'H',
		'NC': 'B',
		'NB': 'B',
		'BN': 'B',
		'BB': 'N',
		'BC': 'B',
		'CC': 'N',
		'CN': 'C',
	}


def test_load_file():
	template, rules = load_file(TEST_FILE)
	assert template == 'NNCB'
	assert rules['CH'] == 'B'


def test_get_pairs(template):
	assert get_pair_counter(template) == {'NN': 1, 'NC': 1, 'CB': 1}


def test_step(template, rules):
	counter = get_pair_counter(template)
	final_counter = get_pair_counter('NCNBCHB')
	assert implement_step(counter, rules) == final_counter
