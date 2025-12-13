import pytest

from day_4 import (
	load_data,
	convert_board_string_to_array,
	find_matching_index,
	create_new_board_status,
	is_board_winner,
)

TEST_FILE = 'inputs/day_4_test.txt'


@pytest.fixture
def order():
	return [
		7,
		4,
		9,
		5,
		11,
		17,
		23,
		2,
		0,
		14,
		21,
		24,
		10,
		16,
		13,
		6,
		15,
		25,
		12,
		22,
		18,
		20,
		8,
		19,
		3,
		26,
		1,
	]


@pytest.fixture
def board_strings():
	return [
		[
			'22 13 17 11  0',
			'8  2 23  4 24',
			'21  9 14 16  7',
			'6 10  3 18  5',
			'1 12 20 15 19',
		],
		[
			'3 15  0  2 22',
			'9 18 13 17  5',
			'19  8  7 25 23',
			'20 11 10 24  4',
			'14 21 16 12  6',
		],
		[
			'14 21 17 24  4',
			'10 16 15  9 19',
			'18  8 23 26 20',
			'22 11 13  6  5',
			'2  0 12  3  7',
		],
	]


@pytest.fixture
def new_board_status():
	return {
		'rows': {0: 0, 1: 0, 2: 0, 3: 0, 4: 0},
		'cols': {0: 0, 1: 0, 2: 0, 3: 0, 4: 0},
	}


@pytest.fixture
def board():
	return [
		[
			[22, 13, 17, 11, 0],
			[8, 2, 23, 4, 24],
			[21, 9, 14, 16, 7],
			[6, 10, 3, 18, 5],
			[1, 12, 20, 15, 19],
		],
		[
			[3, 15, 0, 2, 22],
			[9, 18, 13, 17, 5],
			[19, 8, 7, 25, 23],
			[20, 11, 10, 24, 4],
			[14, 21, 16, 12, 6],
		],
		[
			[14, 21, 17, 24, 4],
			[10, 16, 15, 9, 19],
			[18, 8, 23, 26, 20],
			[22, 11, 13, 6, 5],
			[2, 0, 12, 3, 7],
		],
	]


def test_load_gets_correct_order(order):
	assert load_data(TEST_FILE)[0] == order


def test_load_gets_correct_boards(board_strings):
	assert load_data(TEST_FILE)[1] == board_strings


def test_board_to_array(board_strings, board):
	for i in range(3):
		assert convert_board_string_to_array(board_strings[i]) == board[i]


@pytest.mark.parametrize(
	'board,target,matching_index',
	[
		([[1, 1], [1, 0]], 0, [(1, 1)]),
		([[1, 1], [1, 0]], 1, [(0, 0), (0, 1), (1, 0)]),
		([[1, 1], [2, 3]], 0, []),
	],
)
def test_find_matching_index(board, target, matching_index):
	assert find_matching_index(board, target, matches=[]) == matching_index


def test_new_board_status_1():
	assert create_new_board_status(1) == {'rows': {0: 0}, 'cols': {0: 0}}


def test_new_board_status_2():
	assert create_new_board_status(2) == {'rows': {0: 0, 1: 0}, 'cols': {0: 0, 1: 0}}


@pytest.mark.parametrize(
	'expected,status',
	[
		(
			False,
			{
				'rows': {0: 1, 1: 1, 2: 2, 3: 1, 4: 0},
				'cols': {0: 0, 1: 1, 2: 0, 3: 2, 4: 2},
			},
		),
		(
			False,
			{
				'rows': {0: 0, 1: 2, 2: 1, 3: 2, 4: 0},
				'cols': {0: 1, 1: 1, 2: 1, 3: 0, 4: 2},
			},
		),
		(
			True,
			{
				'rows': {0: 5, 1: 0, 2: 1, 3: 2, 4: 0},
				'cols': {0: 1, 1: 1, 2: 1, 3: 0, 4: 2},
			},
		),
		(
			True,
			{
				'rows': {0: 5, 1: 0, 2: 1, 3: 2, 4: 0},
				'cols': {0: 5, 1: 1, 2: 1, 3: 0, 4: 2},
			},
		),
	],
)
def test_is_board_winner(expected, status):
	assert is_board_winner(status) == expected
