"""Solution to day 14 2021"""
from collections import Counter
INPUT_FILE = "inputs/day_14_input.txt"
TEST_FILE = "inputs/day_14_test_input.txt"


def load_file(filename: str) -> tuple:
    '''Loads the file as a template and a list of rules'''

    with open(filename, "r") as f:
        lines = f.readlines()

    template = lines.pop(0).replace("\n", "")
    rules = {}

    for l in lines[1:]:
        pair, insertion = l.replace("\n", "").split(' -> ')
        rules[pair] = insertion

    return template, rules


def get_pair_counter(template: str) -> Counter:
    """Splits the template into a list of overlapping pairs"""
    return Counter([template[i:i+2] for i in range(len(template)-1)])


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


def one_star(filename: str):
    '''Returns the one star solution'''
    curr_template, rule_dict = load_file(filename)

    return


def two_star(filename: str):
    '''Returns the two star solution'''

    return


if __name__ == "__main__":
    print(f"One star test solution is {one_star(TEST_FILE)}")
    print(f"Two star test solution is {two_star(TEST_FILE)}")
    print(f"One star solution is {one_star(INPUT_FILE)}")
    print(f"Two star solution is {two_star(INPUT_FILE)}")
