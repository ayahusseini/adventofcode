"""Solution to advent of code day 1 2025"""

from numpy import full


INPUT_FILE = 'inputs/day_1_input.txt'
TEST_FILE = 'inputs/day_1_test_input.txt'

STARTING_POSITION = 50


def load_file(filename: str) -> list[str]:
	"""Loads the file as a list of strings"""
	with open(filename, 'r') as f:
		lines = f.readlines()

	for line in lines:
		yield parse_instruction(line)


def parse_instruction(instruction: str) -> int:
	"""Parses the instruction and returns the displacement"""
	instruction = instruction.replace('\n', '').replace(' ', '')
	multiplier = -1 if instruction.startswith('L') else 1
	return multiplier * int(instruction[1:])


def get_new_position(position: int, displacement: int) -> int:
	"""Returns the new position"""
	tot = position + displacement
	return tot % 100


def get_full_rotations(displacement: int) -> int:
	"""Returns the number of full rotations a displacement is equivalent to"""
	return abs(displacement) // 100


def passes_through_zero(position: int, displacement: int) -> bool:
	"""Returns 1 if rotating a dial from position by displacement will
	cause it to pass through zero"""
	position = position % 100
	if position == 0 and displacement <= 0 and abs(displacement) < 100:
		return False
	return (position + displacement) // 100 != 0 or (position + displacement) == 0


def one_star(filename: str):
	"""Returns the number of times the dial points at zero"""
	count = 0
	pos = STARTING_POSITION
	for instruction in load_file(filename):
		pos = get_new_position(pos, instruction)
		if pos == 0:
			count += 1

	return count


def two_star(filename: str):
	"""Returns the two star solution"""
	count = 0
	pos = STARTING_POSITION
	for instruction in load_file(filename):
		direction = -1 if instruction < 0 else 1
		full_rotations = get_full_rotations(instruction)
		count += full_rotations
		instruction = instruction - 100 * full_rotations * direction
		newpos = get_new_position(pos, instruction)
		if passes_through_zero(pos, instruction):
			count += 1
		pos = newpos
	return count


if __name__ == '__main__':
	print(f'One star test solution is {one_star(TEST_FILE)}')
	print(f'Two star test solution is {two_star(TEST_FILE)}')
	print(f'One star solution is {one_star(INPUT_FILE)}')
	print(f'Two star solution is {two_star(INPUT_FILE)}')
