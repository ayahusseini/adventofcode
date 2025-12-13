"""Solution to advent of code day 1 2015
INPUT = key (string)
OUTPUT = number
hash(key + number) starts with 5 zeros"""

import hashlib

TEST_INPUT = 'abcdef'
INPUT = 'bgvyzdsv'


def find_lowest_number(key: str, num_zeros: int = 5) -> int:
	"""Return the lowest number that gives a hash ending with 5 zeros"""
	start = 1
	while True:
		if does_hash_start_with_zeros(f'{key}{start}', num_zeros):
			break
		start += 1
	return start


def does_hash_start_with_zeros(string: str, num_zeros: int = 5) -> bool:
	"""Return True if it's hash starts with num_zeros zeros"""
	return hashlib.md5(string.encode()).hexdigest()[:num_zeros] == '0' * num_zeros


def two_star(filename: str):
	"""Returns the one star solution"""

	return


if __name__ == '__main__':
	print(find_lowest_number(INPUT, 6))
