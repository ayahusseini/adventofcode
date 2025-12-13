"""Solution to day 7 2021.

Puzzle input = horizontal positions of each crap.
They want to move to meet at the same point
What is the lowest number of moves for this to happen?

Essentially we need to find the median of a sorted list of points.
In the second problem, we want to find the average.
"""

from math import floor, ceil

TEST_FILE = 'inputs/day_7_test_input.txt'
INPUT_FILE = 'inputs/day_7_input.txt'
SEPARATOR = ','


def load_file(filename: str) -> list[int]:
	"""Loads the file as a list of integers"""

	with open(filename, 'r') as f:
		line = f.readline()
		as_strings = line.replace('\n', '').replace(' ', '').split(SEPARATOR)
	return [int(s) for s in as_strings if s]


def find_median_positions(positions: str) -> list:
	"""Return a list of median positions (either 1 or 2)"""
	positions.sort()
	midpoint = len(positions) // 2 + 1
	if len(positions) % 2 == 0:
		return [positions[midpoint], positions[midpoint - 1]]
	return [positions[midpoint]]


def find_average_positions(positions: str) -> list:
	"""Return a list of discrete average positions (either 1 or 2)"""
	total = sum(positions)
	average = total / len(positions)
	if floor(average) == ceil(average):
		return floor(average)
	return [floor(average), ceil(average)]


def find_fuel_cost(positions: list, target: int) -> int:
	"""Return the fuel cost of everyone moving to a given target"""
	counts = {i: positions.count(i) for i in positions}
	total = 0
	for pos, factor in counts.items():
		total += abs(pos - target) * factor

	return total


def find_fuel_cost_two_star(positions: list, target: int) -> int:
	"""Return the fuel cost of everyone moving to a given target"""
	counts = {i: positions.count(i) for i in positions}
	total = 0
	for pos, factor in counts.items():
		num_terms = abs(pos - target)
		total += num_terms / 2 * (num_terms + 1) * factor
	return int(total)


def one_star(filename: str):
	"""Returns the one star solution"""
	pos = load_file(filename)
	medians = find_median_positions(pos)
	smallest = find_fuel_cost(pos, medians[0])
	pos_other = find_fuel_cost(pos, medians[1])
	if smallest < pos_other:
		return smallest
	return pos_other


def two_star(filename: str):
	"""Returns the one star solution"""
	pos = load_file(filename)
	medians = find_average_positions(pos)
	print(medians)

	smallest = find_fuel_cost_two_star(pos, medians[0])
	pos_other = find_fuel_cost_two_star(pos, medians[1])
	if smallest < pos_other:
		return smallest
	return pos_other


if __name__ == '__main__':
	print(f'One star test solution is {one_star(TEST_FILE)}')
	print(f'Two star test solution is {two_star(TEST_FILE)}')
	print(f'One star solution is {one_star(INPUT_FILE)}')
	print(f'Two star solution is {two_star(INPUT_FILE)}')
