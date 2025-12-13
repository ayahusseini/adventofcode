"""Solution to day 14 2021"""

from collections import Counter, defaultdict

INPUT_FILE = 'inputs/day_14_input.txt'
TEST_FILE = 'inputs/day_14_test_input.txt'


def load_file(filename: str) -> tuple:
	"""Loads the file as a template and a list of rules"""

	with open(filename, 'r') as f:
		lines = f.readlines()

	template = lines.pop(0).replace('\n', '')
	rules = {}

	for l in lines[1:]:
		pair, insertion = l.replace('\n', '').split(' -> ')
		rules[pair] = insertion

	return template, rules


def get_pair_counter(template: str) -> Counter:
	"""Splits the template into a list of overlapping pairs"""
	return Counter([template[i : i + 2] for i in range(len(template) - 1)])


def implement_step(pair_counts: Counter, rules: dict) -> Counter:
	"""Implements a single step of pair insertion.
	Returns the new pair counts dictionary"""
	new_pair_counts = Counter()
	for pair, count in pair_counts.items():
		to_insert = rules[pair]
		for new_pair in (pair[0] + to_insert, to_insert + pair[1]):
			new_pair_counts[new_pair] += count
	return new_pair_counts


def polymerise_n_times(n: int, pair_counter: Counter, rules: dict) -> Counter:
	"""Performs n steps of polymerisation"""
	for _ in range(n):
		pair_counter = implement_step(pair_counter, rules)
	return pair_counter


def get_polymer_counter(initial_template: str, pair_counts: Counter) -> Counter:
	"""Counts the polymers given a pair counter"""
	polymer_counter = defaultdict(int)
	polymer_counter[initial_template[-1]] = 1
	for pair, count in pair_counts.items():
		polymer_counter[pair[0]] += count
	return Counter(polymer_counter)


def get_max_min_occurances(template: str, rule: dict, num_steps: int) -> int:
	"""Returns the difference between the max and min occurances of a polymer"""
	pairs = get_pair_counter(template)
	final_pair_counter = polymerise_n_times(num_steps, pairs, rule)
	polymer_counter = get_polymer_counter(template, final_pair_counter).most_common()
	return polymer_counter[0][1] - polymer_counter[-1][1]


def one_star(filename: str):
	"""Returns the one star solution"""
	curr_template, rule_dict = load_file(filename)

	return get_max_min_occurances(curr_template, rule_dict, 10)


def two_star(filename: str):
	"""Returns the two star solution"""
	curr_template, rule_dict = load_file(filename)

	return get_max_min_occurances(curr_template, rule_dict, 40)


if __name__ == '__main__':
	print(f'One star test solution is {one_star(TEST_FILE)}')
	print(f'Two star test solution is {two_star(TEST_FILE)}')
	print(f'One star solution is {one_star(INPUT_FILE)}')
	print(f'Two star solution is {two_star(INPUT_FILE)}')
