"""Solution for day 3 of the advent of code.

input = The diagnostic report, list of binary numbers."""

FILENAME = 'inputs/day_3_input.txt'


def extract_report(filename: str) -> list[str]:
	"""Return the diagnostic data"""

	r = []
	with open(filename, 'r') as f:
		for line in f.readlines():
			r.append(line.replace('\n', '').strip())
	return r


def convert_binary_to_decimal(binary: str) -> int:
	"""Return the decimal version of a binary number"""
	return int(binary, 2)


def get_counts(strings: list[str], n: int) -> dict:
	"""Return the count of each letter at the nth position of a string."""

	counts = {'0': 0, '1': 0}
	for s in strings:
		counts[s[n]] += 1
	return counts


def get_most_freq_nth_letter(
	strings: list[str], n: int, opposite: bool = False, default_if_equal: str = '1'
) -> str:
	"""Return the most frequent nth letter in all the strings"""

	counts = get_counts(strings, n)

	if len(set(counts.values())) == 1:
		return default_if_equal

	min_or_max = max if not opposite else min
	return min_or_max(counts.items(), key=lambda x: x[1])[0]


def most_freq_at_each_pos(d: list[str], opposite: bool = False) -> list[str]:
	"""Return a list containing the most frequent letter at each position."""

	item_length = len(d[0])

	if not any(len(i) == item_length for i in d):
		raise ValueError('The items must be of equal length.')

	return [get_most_freq_nth_letter(d, i, opposite) for i in range(item_length)]


def get_gamma_rate(diagnostic_report: list[str]) -> int:
	"""Return the gamma rate as a decimal"""

	binary = ''.join(most_freq_at_each_pos(diagnostic_report, opposite=False))
	return convert_binary_to_decimal(binary)


def get_epsilon_rate(diagnostic_report: list[str]) -> int:
	"""Return the gamma rate as a decimal"""

	binary = ''.join(most_freq_at_each_pos(diagnostic_report, opposite=True))
	return convert_binary_to_decimal(binary)


def get_filtered_down(diagnostic_report: list[str], opposite: bool = False) -> int:
	"""Return the oxygen generator rating as a decimal."""

	num_letters = len(diagnostic_report[0])
	default = '1' if not opposite else '0'

	filtered = diagnostic_report.copy()

	for i in range(num_letters):
		ith_letter = get_most_freq_nth_letter(
			filtered, i, opposite=opposite, default_if_equal=default
		)
		filtered = list(filter(lambda x: x[i] == ith_letter, filtered))

		if len(filtered) == 1:
			return filtered[0]

	raise ValueError('Did not successfully filter down to one value.')


def one_star_solution(filename: str) -> int:
	"""Return the power rate from the diagnostic report"""
	diag = extract_report(filename)
	return get_epsilon_rate(diag) * get_gamma_rate(diag)


def two_star_solution(filename: str) -> int:
	"""Return the two star solution."""
	diag = extract_report(filename)
	oxygen_consumption = convert_binary_to_decimal(get_filtered_down(diag, opposite=False))
	co2_consumption = convert_binary_to_decimal(get_filtered_down(diag, opposite=True))
	return oxygen_consumption * co2_consumption


if __name__ == '__main__':
	print(one_star_solution(FILENAME))
	print(two_star_solution(FILENAME))
