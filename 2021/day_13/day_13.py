"""Solution to advent of code day 13 2021"""

import numpy as np

INPUT_FILE = 'inputs/day_13_input.txt'
TEST_FILE = 'inputs/day_13_test_input.txt'


class Grid:
	def __init__(self, nrows: int, ncols: int, coords_filled: list[tuple]):
		self.grid = np.zeros(shape=(ncols, nrows))
		for coord in coords_filled:
			self.grid[*coord[::-1]] = 1

	@classmethod
	def from_lines(cls, lines: list[str]):
		"""Load a grid from file lines"""

		coords_filled = []
		nrows = 0
		ncols = 0

		for l in lines:
			coords = l.split(',')
			coords = [int(c.strip()) for c in coords]
			if coords[0] + 1 > nrows:
				nrows = coords[0] + 1
			if coords[1] + 1 > ncols:
				ncols = coords[1] + 1
			coords_filled.append(tuple(coords))

		return cls(nrows, ncols, coords_filled)

	def __str__(self):
		string_grid = self.grid.copy()
		string_grid = np.where(string_grid == 0, '.', '#')

		return '\n'.join(''.join(row) for row in string_grid.astype(str))

	def count_marks(self):
		"""Return the number of marks"""
		return np.count_nonzero(self.grid)

	def split_grid(self, along_y: bool, axis_num: int):
		"""split the grid"""
		to_split = self.grid.copy()
		if along_y:
			return to_split[:axis_num, :], to_split[axis_num + 1 :, :]
		return to_split[:, :axis_num], to_split[:, axis_num + 1 :]

	def fold_grid(self, along_y: bool, axis_num: int):
		"""fold the grid"""
		upper, lower = self.split_grid(along_y, axis_num)
		if along_y:
			lower = lower[::-1, :]
		else:
			lower = lower[:, ::-1]
		self.grid = upper + lower


def load_file(filename: str) -> tuple[list[tuple], list[str]]:
	"""Loads the file as a list of coordinates and instructions"""
	coords = []
	fold_instructions = []
	with open(filename, 'r') as f:
		lines = f.readlines()
		for l in lines:
			l.replace('\n', '')
			if ',' in l:
				coords.append(l)
			elif 'fold along' in l:
				fold_instructions.append(l)
	return coords, fold_instructions


def implement_instruction(grid: Grid, instruction: str):
	along = instruction.split('fold along ')[-1]
	along_axis, along_coord = along.split('=')
	along_y = along_axis == 'y'
	along_coord = int(along_coord)
	grid.fold_grid(along_y, along_coord)


def one_star(filename: str):
	"""Returns the one star solution"""
	coords, folds = load_file(filename)
	grid = Grid.from_lines(coords)
	implement_instruction(grid, folds[0])
	return grid.count_marks()


def two_star(filename: str):
	"""Returns the two star solution"""
	coords, folds = load_file(filename)
	grid = Grid.from_lines(coords)
	for fold in folds:
		implement_instruction(grid, fold)

	return str(grid)


if __name__ == '__main__':
	print(f'One star solution is {one_star(TEST_FILE)}')
	print(f'Two star solution is\n{two_star(TEST_FILE)}')
	print(f'One star solution is {one_star(INPUT_FILE)}')
	print(f'Two star solution is\n{two_star(INPUT_FILE)}')
