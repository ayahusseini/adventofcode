'''Solution to advent of code day 15 2015
'''
INPUT_FILE = "inputs/day_15_input.txt"
TEST_FILE = "inputs/day_15_test_input.txt"


class Item(object):
    def __init__(self, name, capacity, durability, flavour, texture, calories) -> None:
        '''Instantiate an item.'''
        self.name = name
        self.stats = {
            "capacity": capacity,
            "durability": durability,
            "flavour": flavour,
            "texture": texture,
            "calories": calories
        }


class ItemsList(object):
    def __init__(self, items_list: list[Item], is_constrained: bool):
        '''Instantiate a list of items.'''
        self.items = items_list
        self.constrained = is_constrained

    def get_score(self, property: str, amounts: list[int]):
        '''Returns the score for a given property'''
        total = sum([i.stats[property]*amounts[idx]
                     for idx, i in enumerate(self.items)])
        return total if total > 0 else 0

    def constraint(self, proportions: list[int]) -> bool:
        '''Return True/False if the proportions and items satisfy
        a constraint.'''
        if self.constrained:
            return self.get_score("calories", proportions) == 500
        return True

    def get_total_score(self, amounts: list[int]):
        '''Returns the total score'''
        tot = 1
        for p in ["capacity", "durability", "flavour", "texture"]:
            tot *= self.get_score(p, amounts)
            if tot == 0:
                return 0
        return tot


def shuffle_proportions(units: int, from_idx: int, proportions: list[int]):
    '''Given a list of proportions, transfer units from from_idx to all others. Return a list of the new proportions'''

    if proportions[from_idx] - units < 0:
        return []
    new = proportions.copy()
    new[from_idx] -= units

    return [new[:i] + [new[i]+units] + new[i+1:] for i in range(len(proportions)) if new[i]+units <= 100 and i != from_idx]


def load_file(filename: str) -> list[int]:
    '''Loads the file as a list of integers'''

    with open(filename, "r") as f:
        lines = f.readlines()

    return [l.replace("\n", "") for l in lines]
