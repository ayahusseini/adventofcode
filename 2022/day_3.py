'''
Each rucksack has 2 large compartments.
All items of a given type go into 1 compartment. This isn't true for exactly ONE compartment.

input = list of rucksacks
    - rucksack = line in the file consisting of items. Each rucksack has 2 compartments.
        - item = single uppercase or lowercase letters
    - Each compartment has the same number of items
'''
FILE = "inputs/day_3_input.txt"


def get_rucksacks(filename: str) -> list[str]:
    '''Return the rucksacks.'''
    r = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            r.append(line.replace("\n", "").strip())
    return r


def group_into_three(l: list[str]) -> list:
    '''Return a list of lists containing three items each.'''
    if len(l) < 3:
        return [l]
    return [l[i:i+3] for i in range(len(l)) if i % 3 == 0]


def get_compartments(line: str) -> list[str, str]:
    '''Get the rucksack split into compartments'''
    midpoint = len(line)//2
    return [line[:midpoint], line[midpoint:]]


def get_match(compartments: list) -> str:
    '''Find the matching item in a list of strings.
    A compartment is a string. Items are the letters.
    Raises an error if there is less than exactly one match'''
    matches = set(compartments[0])
    for c in compartments:
        matches = matches & set(c)

    if len(matches) != 1:
        raise ValueError(
            f"There should be exactly one match between the compartments.\n The matches found are {matches} for compartments {compartments}")
    match, = matches
    return match


def get_alphabetic_position(letter: str) -> int:
    '''Returns the position in the alphabet. Case insensitive.'''
    return ord(letter.lower()) - 96


def get_priority(item: str) -> int:
    """Returns the priority of an item"""
    if item.islower():
        return get_alphabetic_position(item)
    else:
        return get_alphabetic_position(item) + 26


def star_1(filename: str) -> int:
    '''Returns the solution to problem 1'''
    r = get_rucksacks(filename)
    c = [get_compartments(rucksack) for rucksack in r]

    priorities = [get_priority(get_match(compartment)) for compartment in c]
    return sum(priorities)


def star_2(filename: str) -> int:
    '''Returns the solution to problem 2'''
    r = get_rucksacks(filename)
    groups = group_into_three(r)

    priorities = [get_priority(get_match(group)) for group in groups]
    return sum(priorities)


if __name__ == "__main__":
    print(star_1(FILE))
    print(star_2(FILE))
