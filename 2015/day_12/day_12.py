"""Solution to advent of code day 12 2015"""

import json

INPUT_FILE = "inputs/day_12_input.json"


def load_json_dict(filename: str) -> list[dict]:
    """Return a list of dictionaries containing the json file contents"""
    with open(filename, "r") as f:
        d = json.load(f)
    return d


def one_star(filename: str):
    """Returns the one star solution"""

    s = json.dumps(load_json_dict(filename))
    return sum_numbers_in_string(s)


def sum_numbers_in_string(s: str):
    num = 0
    i = 0

    while i < len(s):
        if s[i] == "-":
            multiplier = -1
            i += 1
            continue
        elif not s[i].isnumeric():
            multiplier = 1
            i += 1
            continue

        j = i
        while s[i : j + 1].isnumeric():
            j += 1

        num += int(s[i:j]) * multiplier
        i = j + 1
        multiplier = 1
    return num


def filter_red_from_list(l: list):
    """Remove all dictionaries with the value "red" from a list.
    Replace them with empty dictionaries."""

    for pos, i in enumerate(l):
        if isinstance(i, dict):
            if "red" in i.values():
                l[pos] = dict()
                continue
            for k, v in i.items():
                if isinstance(v, list):
                    l[pos][k] = filter_red_from_list(v)
                elif isinstance(v, dict):
                    l[pos][k] = filter_red_from_list([v])[0]
        elif isinstance(i, list):
            l[pos] = filter_red_from_list(i)
    return l


def two_star(filename: str):
    """Returns the two star solution"""
    s = json.dumps(filter_red_from_list(load_json_dict(filename)))
    return sum_numbers_in_string(s)


if __name__ == "__main__":
    print(f"One star solution is {one_star(INPUT_FILE)}")
    print(f"Two star solution is {two_star(INPUT_FILE)}")
