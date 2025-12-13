"""Solution to advent of code day 5 2025"""

INPUT_FILE = 'inputs/day_5_input.txt'
TEST_FILE = 'inputs/day_5_test_input.txt'


def load_file(filename: str) -> tuple[list, list]:
	"""Load the puzzle input, yielding stripped lines."""
	rngs = []
	ids = []
	with open(filename, 'r') as f:
		for line in f:
			if '-' in line:
				rng_text = line.strip().split('-')
				rngs.append([int(rng_text[0]), int(rng_text[1])])
			elif not line.strip():
				continue
			else:
				ids.append(int(line.strip()))
	return rngs, ids


def merge_two_ranges(r1: list, r2: list, already_sorted=False) -> list[list]:
	"""Merge two inclusive ranges"""
	if not already_sorted:
		r1, r2 = sorted((r1, r2), key=lambda x: x[0])
	if r2[0] > r1[1] + 1:
		return [r1, r2]
	s = min(r1[0], r2[0])
	e = max(r1[1], r2[1])
	return [[s, e]]


def merge_all_ranges(ranges: list[list]) -> list[list]:
	"""Merge a list of inclusive ranges"""
	if len(ranges) < 2:
		return ranges

	ranges = sorted(ranges, key=lambda x: x[0])
	mutually_exclusive = [ranges[0]]
	for right in ranges[1:]:
		left = mutually_exclusive.pop()
		mutually_exclusive += merge_two_ranges(left, right, already_sorted=True)
	return mutually_exclusive


def one_star(filename: str):
	"""Solve part 1 for day 5."""
	ranges, ids = load_file(filename)
	merged = merge_all_ranges(ranges)
	return sum(1 for r in merged for i in ids if i in range(r[0], r[1] + 1))


def two_star(filename: str):
	"""Solve part 2 for day 5."""
	ranges, ids = load_file(filename)
	merged = merge_all_ranges(ranges)
	return sum(r[1] - r[0] + 1 for r in merged)


if __name__ == '__main__':
	print(f'One star test solution is {one_star(TEST_FILE)}')
	print(f'Two star test solution is {two_star(TEST_FILE)}')
	print(f'One star solution is {one_star(INPUT_FILE)}')
	print(f'Two star solution is {two_star(INPUT_FILE)}')
