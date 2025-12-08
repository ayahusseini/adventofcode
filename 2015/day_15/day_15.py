"""Solution to advent of code day 15 2015"""

from collections import defaultdict

INPUT_FILE = "inputs/day_15_input.txt"
TEST_FILE = "inputs/day_15_test_input.txt"


class Item(object):
    def __init__(self, name, capacity, durability, flavour, texture, calories) -> None:
        """Instantiate an item."""
        self.name = name
        self.stats = {
            "capacity": capacity,
            "durability": durability,
            "flavour": flavour,
            "texture": texture,
            "calories": calories,
        }


class ItemsList(object):
    def __init__(self, items_list: list[Item], is_constrained: bool):
        """Instantiate a list of items."""
        self.items = items_list
        num_items = len(items_list)
        self.constrained = is_constrained

        constraint = self.constraint
        initial = [100 // num_items for _ in range(num_items)]
        r = 100 % num_items
        i = 0

        while r > 0:
            initial[i] += 1
            r -= 1
            i += 1

        self.initial = initial

    def get_score(self, property: str, amounts: list[int]):
        """Returns the score for a given property"""
        total = sum(
            [i.stats[property] * amounts[idx] for idx, i in enumerate(self.items)]
        )
        return total if total > 0 else 0

    def constraint(self, proportions: list[int]) -> bool:
        """Return True/False if the proportions and items satisfy
        a constraint."""
        if self.constrained:
            return self.get_score("calories", proportions) == 500
        return True

    def get_total_score(self, amounts: list[int]):
        """Returns the total score"""
        tot = 1
        for p in ["capacity", "durability", "flavour", "texture"]:
            tot *= self.get_score(p, amounts)
            if tot == 0:
                return 0
        return tot

    def get_max_score(self):
        """Returns the maximum possible score"""
        curr = self.initial
        queue = []
        considered = set()

        score = self.get_total_score(curr) if self.constraint(curr) else 0

        while True:
            next_step = step_up_params_with_constraint(
                curr, self.get_total_score, score, self.constraint
            )
            if not next_step:
                return score
            queue += [p for p in next_step if tuple(p) not in considered]
            queue.sort(key=self.get_total_score, reverse=True)

            curr = queue.pop(0)

            considered.add(tuple(curr))

            score = max(self.get_total_score(curr), score)


def shuffle_proportions(units: int, from_idx: int, proportions: list[int]):
    """Given a list of proportions, transfer units from from_idx to all others. Return a list of the new proportions"""

    if proportions[from_idx] - units < 0:
        return []
    new = proportions.copy()
    new[from_idx] -= units

    return [
        new[:i] + [new[i] + units] + new[i + 1 :]
        for i in range(len(proportions))
        if new[i] + units <= 100 and i != from_idx
    ]


def shuffle_all(nunits: int, props: list[int]):
    """Given a list of proportions, transfer nunits from one index to another.
    Repeat for all pairs of indeces."""

    res = []
    for i in range(len(props)):
        res += shuffle_proportions(nunits, i, props)
    return res


def step_up_params(params: list[int], scorer, curr_score: int, step: int = 1):
    """Given a scorer, find the next valid set of parameters, such that the score
    increases"""

    new = []
    shuffled = shuffle_all(step, params)
    for p in shuffled:
        if scorer(p) >= curr_score:
            new.append(p)
    return new


def step_up_params_with_constraint(
    params: list[int], scorer, curr_score: int, constraint
):
    """Given a scorer, find the next valid set of parameters, such that the score
    increases.
    The step increases if the constraint prevents new parameters from being found."""
    step = 1
    while step <= 100 // len(params):
        found = step_up_params(params, scorer, curr_score, step)
        if not found:
            return []
        found = list(filter(constraint, found))
        if found:
            return found
        step += 1


def load_file(filename: str) -> list[int]:
    """Loads the file as a list of integers"""

    with open(filename, "r") as f:
        lines = f.readlines()

    return [l.replace("\n", "") for l in lines]


def get_items(lines: list[str], constraint: bool) -> ItemsList:
    """Returns a dict of ingredients"""
    items = []

    for l in lines:
        w = l.replace(",", "").replace(":", "").split(" ")
        items.append(Item(w[0], int(w[2]), int(w[4]), int(w[6]), int(w[8]), int(w[10])))

    return ItemsList(items, is_constrained=constraint)


def one_star(filename: str):
    """Returns the one star solution"""
    lines = load_file(filename)
    items = get_items(lines, constraint=False)

    return items.get_max_score()


def two_star(filename: str):
    """Returns the two star solution"""
    lines = load_file(filename)
    items = get_items(lines, constraint=True)

    return items.get_max_score()


if __name__ == "__main__":
    print(f"One star test solution is {one_star(TEST_FILE)}")
    print(f"Two star test solution is {two_star(TEST_FILE)}")
    print(f"One star solution is {one_star(INPUT_FILE)}")
    print(f"Two star solution is {two_star(INPUT_FILE)}")
