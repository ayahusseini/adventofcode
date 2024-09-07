'''Solution to advent of code day 10 2021

Puzzle input = navigation subsystem: lines of strings
Each line has multiple chunks. Each chunk contains >= 0 other chunks
Each chunk must open and close with pairs of matching characters

Corrupted line: chunk closes with the wrong character

One star:
Find the first illegal character and use it's SCORE to find the score
for a corrupted line. Return the total syntax score.
Ignore incomplete lines.

Two star: 
No longer ignore incomplete lines.
'''

INPUT_FILE = "inputs/day_10_input.txt"
TEST_FILE = "inputs/day_10_test_input.txt"

BRACKETS = ["()", "[]", "<>", "{}"]
CLOSED_TO_OPENED = {b[1]: b[0] for b in BRACKETS}
OPENED_TO_CLOSED = {b[0]: b[1] for b in BRACKETS}

SCORE = {
    ")": 3, "]": 57, "}": 1197, ">": 25137
}
AUTOCOMPLETE_SCORE = {
    ")": 1, "]": 2, "}": 3, ">": 4
}


def load_file(filename: str) -> list[int]:
    '''Loads the file as a list of integers'''

    with open(filename, "r") as f:
        lines = f.readlines()

    return [l.replace("\n", "").replace(" ", "") for l in lines]


def find_incorrect_bracket(line: str, return_autocomplete: bool = False) -> str | list:
    '''Assuming a corrupted line, find the first incorrect bracket.
    This is the first closing bracket that closes an unopened bracket

    If return_autocomplete, return any brackets left to close, in the order that
    they should be closed in.'''

    to_close = []
    for b in line:
        if b in OPENED_TO_CLOSED.keys():
            to_close.append(OPENED_TO_CLOSED[b])
        else:
            if b != to_close.pop(-1):
                if not return_autocomplete:
                    return b
                else:
                    return []

    return to_close[::-1] if return_autocomplete else None


def get_autocomplete_score(to_close: list) -> int:
    '''Get the autocomplete score given a list of autocomplete brackets'''
    total = 0
    for c in to_close:
        total *= 5
        total += AUTOCOMPLETE_SCORE[c]
    return total


def find_middle(nums: list) -> int:
    '''Return the midpoint of a list of nums'''
    midpoint = len(nums)//2
    nums.sort()
    if not nums:
        return None
    return nums[midpoint]


def one_star(filename: str):
    '''Returns the one star solution'''
    lines = load_file(filename)

    tot = sum(SCORE.get(find_incorrect_bracket(l), 0) for l in lines)
    return tot


def two_star(filename: str):
    '''Returns the two star solution'''
    lines = load_file(filename)
    totals = [get_autocomplete_score(find_incorrect_bracket(
        line, return_autocomplete=True)) for line in lines if find_incorrect_bracket(
        line, return_autocomplete=True)]

    return find_middle(totals)


if __name__ == "__main__":
    print(f"One star solution is {one_star(TEST_FILE)}")
    print(f"Two star solution is {two_star(TEST_FILE)}")
    print(f"One star solution is {one_star(INPUT_FILE)}")
    print(f"Two star solution is {two_star(INPUT_FILE)}")
