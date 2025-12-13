"""Solution to advent of code day 6 2023

dist = speed * time moving
time moving = t_tot - t_stopped
speed = a * t_stopped

dist = t_stopped * a * (t_tot - t_stopped)

dist == r_dist (record distance) at the solutions to the quadratic

since this is a negative quadratic, dist >= r_dist between the solutions
"""

from math import floor, ceil

INPUT_FILE = 'inputs/day_6_input.txt'
TEST_FILE = 'inputs/day_6_test_input.txt'

START_SPEED = 0
ACCELERATION = 1


def get_det(a: int, t_tot: int, dist: int) -> int:
	"""Returns determinant"""
	return (a * t_tot) ** 2 - 4 * dist


def solve_quadratic(a: int, t_tot: int, dist: int) -> int:
	"""
	Returns the solution to the quadratic
	x**2 - a * t_tot * x + dist == 0
	"""
	det = get_det(a, t_tot, dist)
	if get_det(a, t_tot, dist) < 0:
		raise ValueError('There is no solution')
	return (a * t_tot + det**0.5) / 2, (a * t_tot - det**0.5) / 2


def get_num_solutions(accel: int, race_time: int, record: int):
	"""Returns the number of ways that the record time can be beaten, given a total race time, and a record distance.
	accel is the acceleration when the button is pressed"""
	max_stop_time, min_stop_time = solve_quadratic(accel, race_time, record)

	if floor(max_stop_time) == max_stop_time:
		max_stop_time -= 1
	if ceil(min_stop_time) == min_stop_time:
		min_stop_time += 1

	return floor(max_stop_time) - ceil(min_stop_time) + 1


def load_file(filename: str):
	"""Loads the file as two lists of integers"""

	with open(filename, 'r') as f:
		lines = f.readlines()

	lines = [l.replace('\n', '').strip() for l in lines]

	times = [int(i) for i in lines[0].split('Time:')[-1].split(' ') if i.strip()]
	records = [int(i.strip()) for i in lines[1].split('Distance:')[-1].split(' ') if i.strip()]
	return times, records


def one_star(filename: str):
	"""Returns the one star solution"""
	times, records = load_file(filename)
	ways = 1
	for t, r in zip(times, records):
		ways *= get_num_solutions(ACCELERATION, t, r)

	return ways


def two_star(filename: str):
	"""Returns the two star solution"""
	times, records = load_file(filename)
	time = int(''.join([str(t) for t in times]))

	record = int(''.join([str(t) for t in records]))

	return get_num_solutions(ACCELERATION, time, record)


if __name__ == '__main__':
	print(f'One star solution is {one_star(TEST_FILE)}')
	print(f'Two star solution is {two_star(TEST_FILE)}')
	print(f'One star solution is {one_star(INPUT_FILE)}')
	print(f'Two star solution is {two_star(INPUT_FILE)}')
