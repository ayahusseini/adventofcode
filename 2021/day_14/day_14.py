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


def get_pairs(template: str) -> list[str]:
    """Splits the template into a list of overlapping pairs"""
    return [template[i:i+2] for i in range(len(template)-1)]


def generate_next_item(template: str, rules: dict):
    """Performs pair insertion according to the rules"""
    pairs = get_pairs(template)

    yield template[0]

    for pair in pairs:
        yield rules[pair]
        yield pair[1]


def one_star(filename: str):
    '''Returns the one star solution'''
    curr_template, rule_dict = load_file(filename)
    for _ in range(10):
        curr_template = ''.join(generate_next_item(curr_template, rule_dict))

    most_common = Counter(curr_template).most_common()

    return most_common[0][1] - most_common[-1][1]


def two_star(filename: str):
    '''Returns the two star solution'''

    return


if __name__ == "__main__":
    print(f"One star solution is {one_star(TEST_FILE)}")
    print(f"Two star solution is {two_star(TEST_FILE)}")
    print(f"One star solution is {one_star(INPUT_FILE)}")
    print(f"Two star solution is {two_star(INPUT_FILE)}")
