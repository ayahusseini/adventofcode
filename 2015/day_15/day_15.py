'''Solution to advent of code day 14 2015
'''

import numpy as np
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
    def __init__(self, items_list: list[Item], constraint=lambda i, p: True):
        '''Instantiate a list of items'''
        self.items_list = items_list
        self.initial_proportions = [100//len(items_list) for _ in items_list]

        r = 100 % len(items_list)
        i = 0

        while r > 0:
            self.initial_proportions[i] += 1
            r -= 1
            i += 1

        while not constraint(self, self.initial_proportions):
            self.initial_proportions[0] -= 1
            self.initial_proportions[-1] += 1

        self.constraint = lambda p: constraint(self, p)

    def __len__(self):
        return len(self.items_list)

    def get_total_value_for_property(self, property: str, proportions: list[int]):
        '''Returns the total value for a given property'''
        total = sum([i.stats[property]*proportions[idx]
                    for idx, i in enumerate(self.items_list)])
        return total if total > 0 else 0

    def get_score(self, proportions: list[int], properties: list[str] = ["capacity", "durability", "flavour", "texture"]):
        '''Returns the total score given items in certain proportions'''
        score = 1
        for p in properties:
            score *= self.get_total_value_for_property(p, proportions)
        return score

    def get_increasing_directions(self, curr_proportions: list[int], curr_score: int, constraint=lambda p: True):
        '''Make a single unit change to curr_proportions that will lead to an increase.
        Return the new proportions and their scores, 
        as long as those proportions satisfy the constraint.'''
        increasing_directions = []

        for i, p_decrease in enumerate(curr_proportions):
            if p_decrease == 0:
                continue
            for j, p_increase in enumerate(curr_proportions):
                if i == j:
                    continue

                if p_increase == 100:
                    continue

                new_proportion = curr_proportions.copy()
                new_proportion[i] -= 1
                new_proportion[j] += 1
                if not constraint(new_proportion):
                    continue
                if self.get_score(new_proportion) >= curr_score:
                    increasing_directions.append(new_proportion)
        return increasing_directions

    def find_max_score(self, properties: list[str] = ["capacity", "durability", "flavour", "texture"]):
        '''Return the maximum possible score with respect to certain properties.
        The function constraint maps valid proportions to True.'''

        queue = [self.initial_proportions]
        print(queue)

        considered = []
        curr_max = 0

        while queue:

            considering = queue.pop(0)
            if tuple(considering) in considered:
                continue
            considered.append(tuple(considering))
            curr_max = max(curr_max, self.get_score(considering, properties))
            queue += self.get_increasing_directions(
                curr_proportions=considering, curr_score=curr_max, constraint=self.constraint)
        return curr_max


def load_file(filename: str) -> list[int]:
    '''Loads the file as a list of integers'''

    with open(filename, "r") as f:
        lines = f.readlines()

    return [l.replace("\n", "") for l in lines]


def get_items(lines: list[str], max_calories=None) -> dict:
    '''Returns a dict of ingredients'''
    items = []
    for l in lines:
        w = l.replace(",", "").replace(":", "").split(" ")
        items.append(Item(w[0], int(w[2]), int(w[4]),
                     int(w[6]), int(w[8]), int(w[10])))

    if max_calories is not None:
        def constraint(items_obj, prop): return items_obj.get_total_value_for_property(
            "calories", prop) == 500
        return ItemsList(items, constraint)
    return ItemsList(items)


def one_star(filename: str):
    '''Returns the one star solution'''
    lines = load_file(filename)
    items = get_items(lines)

    return items.find_max_score()


def two_star(filename: str):
    '''Returns the two star solution'''
    lines = load_file(filename)
    items = get_items(lines, max_calories=500)
    print(items.initial_proportions)
    return items.find_max_score()


if __name__ == "__main__":
    print(f"One star test solution is {one_star(TEST_FILE)}")

    print(f"Two star test solution is {two_star(TEST_FILE)}")
    print(f"One star solution is {one_star(INPUT_FILE)}")
    print(f"Two star solution is {two_star(INPUT_FILE)}")
