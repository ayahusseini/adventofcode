'''Solution to advent of code day 5 2022
'''
import re
from collections import namedtuple, defaultdict

INPUT_FILE = "inputs/day_5_input.txt"
TEST_FILE = "inputs/day_5_test_input.txt"

Move = namedtuple("Move", ['amount', 'prev_stack', 'new_stack'])


class CrateStack:
    stack_pattern = r'\[(\w)\][ |\n]|(   )'

    def __init__(self, stacks_to_crates: dict):
        self.stacks = stacks_to_crates

    def update(self, move: Move):
        removed = self.stacks[move.prev_stack][-move.amount:]
        self.stacks[move.prev_stack] = self.stacks[move.prev_stack][:-move.amount]
        self.stacks[move.new_stack] += removed[::-1]

    @classmethod
    def from_lines(cls, lines: list[str]):
        """Instantiates a crate stack from lines"""
        stacks = defaultdict(lambda: [])
        for l in lines[::-1]:
            if '[' in l:
                level = re.findall(cls.stack_pattern, l)
                for i, entry in enumerate(level):
                    if entry[0]:
                        stacks[i].append(entry[0])
        return cls(stacks)


def one_star(filename: str):
    '''Returns the one star solution'''

    return


def two_star(filename: str):
    '''Returns the two star solution'''

    return


if __name__ == "__main__":
    print(f"One star test solution is {one_star(TEST_FILE)}")
    print(f"Two star test solution is {two_star(TEST_FILE)}")
    print(f"One star solution is {one_star(INPUT_FILE)}")
    print(f"Two star solution is {two_star(INPUT_FILE)}")
