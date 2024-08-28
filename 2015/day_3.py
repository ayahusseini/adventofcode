'''
Each rucksack has 2 large compartments.
All items of a given type go into 1 compartment. This isn't true for exactly ONE compartment. 

input = list of rucksacks
    - rucksack = line in the file consisting of items. Each rucksack has 2 compartments.
        - item = single uppercase or lowercase letters
    - Each compartment has the same number of items
'''
TEST_FILE = "inputs/day_3_test.txt"


def get_rucksacks(filename: str) -> list[str]:
    '''Return the rucksacks.'''
    r = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            r.append(line.replace("\n", "").strip())
    return r


def get_compartments(line: str) -> list[str, str]:
    '''Get the rucksack split into compartments'''
    midpoint = len(line)//2
    return [line[:midpoint], line[midpoint:]]


def get_match(compartments: list[str, str]) -> str:
    '''Find the matching item in the compartments. 
    Raises an error if there is less than exactly one match'''
    matches = set(compartments[0]).intersection(compartments[1])
    if len(matches) != 1:
        raise ValueError(
            "There should be exactly one match between the compartments")
    match, = matches
    return match


def get_alphabetic_position(letter: str) -> int:
    '''Returns the position in the alphabet. Case insensitive.'''
    return ord(letter.lower()) - 96


def get_priority(item: str) -> int:
    """Returns the priority of an item"""


if __name__ == "__main__":
    get_rucksacks(TEST_FILE)
