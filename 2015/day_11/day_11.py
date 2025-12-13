"""Solution to advent of code day 11 2015"""

INPUT = 'hxbxwxba'
TEST = 'abcdefgh'


def get_alphabet() -> str:
	"""Return the alphabet"""
	return 'abcdefghijklmnopqrstuvwxyz'


def get_next_letter(s: str) -> str:
	"""Returns the next letter in the alphabet, or "a" if s == z"""

	s = s.lower()
	alphabet = get_alphabet()
	return alphabet[alphabet.find(s) + 1] if s != 'z' else 'a'


def increment_once(seq: str) -> str:
	"""Increment the last letter in the sequence.
	Increment the letter to it's left if it wraps around,
	continuing until one doesn't wrap."""

	for i, letter in enumerate(seq[::-1]):
		inc = get_next_letter(letter)
		if inc != 'a':
			return seq[: -i - 1] + inc + 'a' * i
	return 'a' * len(seq)


def count_subsequences(seq: str, length: int, overlapping: bool, rule) -> str:
	"""Return the number of subsequences of a given length
	within seq which satisfy some rule"""

	i = 0
	count = 0
	while i <= len(seq) - length:
		is_valid_subseq = rule(seq[i : i + length])
		if is_valid_subseq:
			count += 1
			if not overlapping:
				i += length
			else:
				i += 1
		else:
			i += 1

	return count


def is_increasing_alphabetically(text: str) -> bool:
	"""Returns True if letters in text are increasing alphabetically."""
	return text in get_alphabet()


def is_matching(text: str) -> bool:
	"""Returns True if all letters in the text are the same"""
	if not text:
		return True
	return text == text[0] * len(text)


def does_not_contain(text: str, cannot_contain: list[str] = ['i', 'o', 'l']) -> bool:
	"""Returns True if text doesn't contain cannot_contain"""
	return set(text) - set(cannot_contain) == set(text)


def is_valid_password(seq: str) -> bool:
	"""Returns True if a password is valid"""

	return (
		does_not_contain(seq, ['i', 'o', 'l'])
		and (count_subsequences(seq, 2, False, is_matching) > 1)
		and (count_subsequences(seq, 3, True, is_increasing_alphabetically) > 0)
	)


def one_star(input_sequence: str):
	"""Returns the one star solution"""
	while not is_valid_password(input_sequence):
		input_sequence = increment_once(input_sequence)
	return input_sequence


def two_star(input_sequence: str):
	"""Returns the two star solution"""
	input_sequence = increment_once(one_star(input_sequence))
	return one_star(input_sequence)


if __name__ == '__main__':
	print(f'One star test solution is {one_star(TEST)}')
	print(f'One star solution is {one_star(INPUT)}')
	print(f'Two star solution is {two_star(INPUT)}')
