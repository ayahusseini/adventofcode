'''Solution to advent of code day 7 2024
'''

INPUT_FILE = "inputs/day_7_input.txt"
TEST_FILE = "inputs/day_7_test_input.txt"


def load_file(filename: str):
    '''Loads the file as a target and a list of integers'''

    with open(filename, "r") as f:
        lines = f.readlines()

    for l in lines:
        l = l.replace('\n', '').strip()
        target, nums_text = l.split(':')
        yield int(target), [int(n) for n in nums_text.split(' ') if n]


def search(nums, target_total) -> bool:
    """Searches for a target"""
    stack = [(nums[0], 0)]

    while stack:
        current_total, current_index = stack.pop()

        next_idx = current_index + 1

        if next_idx >= len(nums):
            continue

        next_sum = nums[next_idx] + current_total
        next_prod = nums[next_idx] * current_total

        for n in (next_sum, next_prod):
            if n < target_total:
                stack.append((n, next_idx))
            elif n == target_total:
                return True
    return False


def one_star(filename: str):
    '''Returns the one star solution'''
    tot = 0
    for target, expression in load_file(filename):
        if search(expression, target):
            tot += target

    return tot


def two_star(filename: str):
    '''Returns the two star solution'''

    return


if __name__ == "__main__":
    print(f"One star solution is {one_star(TEST_FILE)}")
    print(f"Two star solution is {two_star(TEST_FILE)}")
    print(f"One star solution is {one_star(INPUT_FILE)}")
    print(f"Two star solution is {two_star(INPUT_FILE)}")
