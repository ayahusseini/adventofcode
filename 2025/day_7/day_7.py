"""Solution to advent of code day 7 2025"""

INPUT_FILE = 'inputs/day_7_input.txt'
TEST_FILE = 'inputs/day_7_test_input.txt'


def load_file(filename: str):
	"""
	Load the puzzle input, returning processed lines

	Returns:
	    is_beam : 2D array which is '1' at the source
	    is_splitted : 2D array which is '1' at any splitters
	"""

	with open(filename, 'r') as f:
		lines = [list(l.strip()) for l in f if l.strip()]

	is_beam = [[1 if char == 'S' else 0 for char in l] for l in lines]
	is_splitter = [[1 if char == '^' else 0 for char in l] for l in lines]
	return is_beam, is_splitter


def num_ways_to_reach(
	above_neighbourhood: list[int],
	splitter_neighbourhood: list[int],
	memo: dict = dict(),
) -> tuple[int, int]:
	"""Return the number of ways for a beam to reach an position, given its immediate surroundings.
	Also returns the number of 'split events'

	Given:
	    above_neigbourhood : list of 3 integers representing the solution for the above three positions.
	        - Note that if one of the 'neighbours' is out of bounds, it is just a '0'
	    splitter_neighbourhood : Boolean list of integers representing whether or not there is a splitter
	        at the index and its neighbouring two positions.
	    memo : Dictionary storing solutions
	Returns:
	    tot : the number of ways for a beam to reach the index
	    splits : the number of times a beam gets split
	"""
	tot = 0
	splits = 0

	if (tuple(above_neighbourhood), tuple(splitter_neighbourhood)) in memo.keys():
		return memo[(tuple(above_neighbourhood), tuple(splitter_neighbourhood))]

	if splitter_neighbourhood[1]:
		return 0, 0

	if above_neighbourhood[1] > 0:
		tot += above_neighbourhood[1]

	for dir in (0, 2):
		if splitter_neighbourhood[dir] and above_neighbourhood[dir]:
			tot += above_neighbourhood[dir]
			splits += 1

	memo[(tuple(above_neighbourhood), tuple(splitter_neighbourhood))] = (tot, splits)

	return tot, splits


def num_ways_to_reach_next_row(
	above_row: list[int], splitter_row: list[int], memo: dict = dict()
) -> tuple[list, int]:
	"""Return the number of ways for a beam to reach each position in a row, and the number of
	split events.
	Given:
	    above_row : list of integers representing the number of ways to reach each index in the above row
	    splitter_row : boolean list representing whether or not a position has a splitter
	Return:
	    next_row : list of integers representing the next row
	    tot_splits : The number of split events
	"""
	num_pos = len(above_row)
	tot_splits = 0
	above_row = [0] + above_row + [0]
	next_row = [0] * num_pos
	splitter_row = [0] + splitter_row + [0]

	for idx in range(1, num_pos + 1):
		neighbourhood = above_row[idx - 1 : idx + 2]
		splitters = splitter_row[idx - 1 : idx + 2]
		ways, splits = num_ways_to_reach(neighbourhood, splitters, memo)
		next_row[idx - 1] = ways
		tot_splits += splits

	return next_row, tot_splits // 2


def one_star(filename: str):
	"""
	Solve part 1 for day 7.
	Returns:
	    num_splits : The number of time the beam gets split
	"""
	is_beam, is_splitter = load_file(filename)
	row = is_beam[0]

	num_splits = 0
	for splitter in is_splitter[1:]:
		row, splits = num_ways_to_reach_next_row(row, splitter)
		num_splits += splits
	return num_splits


def two_star(filename: str):
	"""
	Solve part 2 for day 7.
	"""
	is_beam, is_splitter = load_file(filename)
	row = is_beam[0]
	all_ways = [row]
	for splitter in is_splitter[1:]:
		row, splits = num_ways_to_reach_next_row(row, splitter)
		all_ways += [row]

	return sum(all_ways[-1])


if __name__ == '__main__':
	print(f'One star test solution is {one_star(TEST_FILE)}')
	print(f'Two star test solution is {two_star(TEST_FILE)}')
	print(f'One star solution is {one_star(INPUT_FILE)}')
	print(f'Two star solution is {two_star(INPUT_FILE)}')
