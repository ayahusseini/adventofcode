"""Solution to day 6 2021"""

from collections import defaultdict

TEST_FILE = 'inputs/day_6_test_input.txt'
INPUT_FILE = 'inputs/day_6_input.txt'
SEPARATOR = ','

ADULT_BIRTH_CYCLE = 7
CHILD_INITIAL_STATE = 8

NUM_DAYS_ONE_STAR = 80

NUM_DAYS_TWO_STAR = 256


def load_file(filename: str) -> list[int]:
	"""Loads the file as a list of integers"""

	with open(filename, 'r') as f:
		line = f.readline()
		as_strings = line.replace('\n', '').replace(' ', '').split(SEPARATOR)
	return [int(s) for s in as_strings if s]


def update_state_one_day(curr_state: dict) -> dict:
	"""Updates the state"""

	new_state = defaultdict(lambda: 0)

	for state, count in curr_state.items():
		if state == 0:
			new_state[CHILD_INITIAL_STATE] += count
			new_state[ADULT_BIRTH_CYCLE - 1] += count
		else:
			new_state[state - 1] += count

	return new_state


def update_state_n_days(initial_state: dict, num_days) -> dict:
	"""Updates the state dictionary after num_days have passed"""

	for _ in range(num_days):
		initial_state = update_state_one_day(initial_state)
	return initial_state


def find_total_population_after_n_days(initial_state_list: list, days: int) -> int:
	"""Given a list of initial states, return the total population after n days"""
	state = {i: initial_state_list.count(i) for i in initial_state_list}
	return sum([v for v in update_state_n_days(state, days).values()])


def one_star(filename: str):
	"""Returns the one star solution"""
	state = load_file(filename)
	return find_total_population_after_n_days(state, NUM_DAYS_ONE_STAR)


def two_star(filename: str):
	"""Returns the one star solution"""
	state = load_file(filename)
	return find_total_population_after_n_days(state, NUM_DAYS_TWO_STAR)


if __name__ == '__main__':
	print(f'One star solution is {one_star(INPUT_FILE)}')
	print(f'Two star solution is {two_star(INPUT_FILE)}')
