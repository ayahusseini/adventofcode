"""Solution to advent of code day 7 2024"""

INPUT_FILE = 'inputs/day_7_input.txt'
TEST_FILE = 'inputs/day_7_test_input.txt'


def load_file(filename: str):
	"""Loads the file as a target and a list of integers"""

	with open(filename, 'r') as f:
		lines = f.readlines()

	for l in lines:
		l = l.replace('\n', '').strip()
		target, nums_text = l.split(':')
		yield int(target), [int(n) for n in nums_text.split(' ') if n]


def concatenate(num1: int, num2: int) -> int:
	"""Concatenates two numbers"""
	return int(f'{num1}{num2}')


def search(nums, target_total, include_concatenate: bool = False) -> bool:
	"""Searches for a target"""
	stack = [(nums[0], 0)]

	while stack:
		current_total, current_index = stack.pop()

		next_idx = current_index + 1

		if next_idx >= len(nums):
			continue

		next_sum = current_total + nums[next_idx]
		next_prod = current_total * nums[next_idx]
		possibilities = [next_sum, next_prod]

		if include_concatenate:
			possibilities.append(concatenate(current_total, nums[next_idx]))

		for n in possibilities:
			if (next_idx == len(nums) - 1) and n == target_total:
				return True
			elif n <= target_total:
				stack.append((n, next_idx))

	return False


def get_total_callibration_result(input_file: str, allow_concatenate: bool):
	tot = 0
	for target, expression in load_file(input_file):
		if search(expression, target, allow_concatenate):
			tot += target

	return tot


def one_star(filename: str):
	"""Returns the one star solution"""

	return get_total_callibration_result(filename, False)


def two_star(filename: str):
	"""Returns the two star solution"""

	return get_total_callibration_result(filename, True)


if __name__ == '__main__':
	print(f'One star test solution is {one_star(TEST_FILE)}')
	print(f'Two star test solution is {two_star(TEST_FILE)}')
	print(f'One star solution is {one_star(INPUT_FILE)}')
	print(f'Two star solution is {two_star(INPUT_FILE)}')
