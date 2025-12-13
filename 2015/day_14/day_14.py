"""Solution to advent of code day 14 2015"""

INPUT_FILE = 'inputs/day_14_input.txt'
TEST_FILE = 'inputs/day_14_test_input.txt'
TEST_TIME = 1000
INPUT_TIME = 2503


def load_file(filename: str) -> list[int]:
	"""Loads the file as a list of integers"""

	with open(filename, 'r') as f:
		lines = f.readlines()

	return [l.replace('\n', '') for l in lines]


def get_moving_time(move_time: int, rest_time: int, tot_time: int):
	if tot_time <= move_time:
		return tot_time

	elif tot_time <= move_time + rest_time:
		return move_time

	return (tot_time // (move_time + rest_time)) * move_time + get_moving_time(
		move_time, rest_time, tot_time % (move_time + rest_time)
	)


def get_tot_distance(speed: int, move_time: int, rest_time: int, tot_time: int) -> int:
	"""Return the total distance given a move time and a rest time."""
	return speed * get_moving_time(move_time, rest_time, tot_time)


def one_star(filename: str, tot_time: int):
	"""Returns the one star solution"""
	lines = load_file(filename)
	distances = []
	for l in lines:
		words = l.split(' ')
		distances.append(get_tot_distance(int(words[3]), int(words[6]), int(words[-2]), tot_time))
	return max(distances)


def get_scores_after_n_sec(lines: list, scores=[], n: int = 1):
	distances = []

	for i, l in enumerate(lines):
		words = l.split(' ')
		distances.append(get_tot_distance(int(words[3]), int(words[6]), int(words[-2]), n))

	return [s + 1 if distances[i] == max(distances) else s for i, s in enumerate(scores)]


def two_star(filename: str, tot_time: int):
	"""Returns the two star solution"""
	lines = load_file(filename)
	scores = [0] * len(lines)
	for t in range(1, tot_time + 1):
		scores = get_scores_after_n_sec(lines, scores, t)
	return max(scores)


if __name__ == '__main__':
	print(f'One star test solution is {one_star(TEST_FILE, TEST_TIME)}')
	print(f'Two star solution is {two_star(TEST_FILE, TEST_TIME)}')
	print(f'One star solution is {one_star(INPUT_FILE, INPUT_TIME)}')
	print(f'Two star solution is {two_star(INPUT_FILE, INPUT_TIME)}')
