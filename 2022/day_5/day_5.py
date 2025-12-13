"""Solution to advent of code day 5 2022"""

import re
from collections import namedtuple, defaultdict

INPUT_FILE = 'inputs/day_5_input.txt'
TEST_FILE = 'inputs/day_5_test_input.txt'

MOVE_PATTERN = r'move (\w+) from (\w+) to (\w+)'
STACK_PATTERN = r'\[(\w)\][ |\n]|(   )'

Move = namedtuple('Move', ['amount', 'prev_stack', 'new_stack'])


class CrateStack:
	def __init__(self, stacks_to_crates: dict):
		self.stacks = stacks_to_crates

	def update_full_moves(self, moves: list[Move]):
		for m in moves:
			self.update(m)

	def update(self, move: Move):
		removed = self.stacks[move.prev_stack][-move.amount :]
		self.stacks[move.prev_stack] = self.stacks[move.prev_stack][: -move.amount]
		self.stacks[move.new_stack] += removed[::-1]

	@classmethod
	def from_lines(cls, lines: list[str]):
		"""Instantiates a crate stack from lines"""
		stacks = defaultdict(lambda: [])
		for l in lines[::-1]:
			if '[' in l:
				level = re.findall(STACK_PATTERN, l)
				for i, entry in enumerate(level):
					if entry[0]:
						stacks[i + 1].append(entry[0])
		return cls(stacks)


def load_file(filename: str) -> tuple[CrateStack, list[Move]]:
	"""Loads the file as an initial stack and a list of moves"""
	stacklines = []
	moves = []
	with open(filename, 'r') as f:
		lines = f.readlines()
	parsing_moves = False
	for l in lines:
		if 'move' in l:
			amount, prev, next = re.findall(MOVE_PATTERN, l)[0]
			moves.append(Move(int(amount), int(prev), int(next)))
		else:
			stacklines.append(l)
	return CrateStack.from_lines(stacklines), moves


def one_star(filename: str):
	"""Returns the one star solution"""
	cratestack, moves = load_file(filename)
	cratestack.update_full_moves(moves)
	print(cratestack.stacks)
	return ''.join([crates[-1] for stack, crates in cratestack.stacks.items()])


def two_star(filename: str):
	"""Returns the two star solution"""

	return


if __name__ == '__main__':
	print(f'One star test solution is {one_star(TEST_FILE)}')
	print(f'Two star test solution is {two_star(TEST_FILE)}')
	print(f'One star solution is {one_star(INPUT_FILE)}')
	print(f'Two star solution is {two_star(INPUT_FILE)}')
