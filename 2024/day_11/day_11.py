"""Solution to advent of code day 11 2024"""

from collections import defaultdict

INPUT_FILE = 'inputs/day_11_input.txt'
TEST_FILE = 'inputs/day_11_test_input.txt'


def count_digits(num: int) -> int:
	"""Return the number of digits"""
	return len(str(num))


def is_num_digits_even(num: int) -> bool:
	"""Return True if the number of digits is even"""
	return count_digits(num) % 2 == 0


def split_num(num: int) -> tuple[int, int]:
	"""Splits the digits in half, ignoring trailing zeros."""

	num = str(num)
	digits = len(num)
	return int(num[: digits // 2]), int(num[digits // 2 :])


def blink(num: int) -> tuple:
	"""Return a tuple containing the transformed number."""
	if num == 0:
		sol = (1,)
	elif is_num_digits_even(num):
		sol = split_num(num)
	else:
		sol = (num * 2024,)
	return sol


def precompute(blinks: int = 100) -> dict[tuple, tuple]:
	"""Precomputes a path memo for ease of use"""
	memo = dict()
	blink_n_times((0,), blinks, path_memo=memo)
	print('precompute_done')
	return memo


def blink_n_times(nums: tuple[int], blinks: int, path_memo: dict = dict()) -> tuple:
	"""Return the length of the new containing the transformed number after blinking n times"""

	counts = {n: nums.count(n) for n in nums}

	if isinstance(nums, int):
		nums = (nums,)
	else:
		nums = tuple(nums)

	for _ in range(blinks):
		new_nums = defaultdict(lambda: 0)
		for num, freq in counts.items():
			if num not in path_memo:
				path_memo[num] = blink(num)

			for p in path_memo[num]:
				new_nums[p] += freq

		counts = new_nums

	return sum(counts.values())


def load_file(filename: str) -> list[int]:
	"""Loads the file as a list of integers"""
	with open(filename, 'r') as f:
		line = f.readline().strip()
	return [int(n.strip()) for n in line.split(' ') if n.strip()]


def one_star(filename: str, num_blinks: int = 25, cache: dict = dict()):
	"""Returns the one star solution"""
	stones = load_file(filename)
	return blink_n_times(stones, num_blinks, path_memo=cache)


def two_star(filename: str, cache: dict = dict()):
	"""Returns the two star solution"""
	return one_star(filename, num_blinks=75, cache=cache)


if __name__ == '__main__':
	cache = precompute(75)
	print(f'One star test solution is {one_star(TEST_FILE, cache=cache)}')
	print(f'Two star test solution is {two_star(TEST_FILE, cache=cache)}')
	print(f'One star solution is {one_star(INPUT_FILE, cache=cache)}')
	print(f'Two star solution is {two_star(INPUT_FILE, cache=cache)}')
