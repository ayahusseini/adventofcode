'''Solution to advent of code day 11 2021

Puzzle input = 10 x 10 grid with 100 numbers, representing octopuses energy level (0-9)

Over time, 
- Each energy level increases by 1
- If an energy level is > 1, it increases all adjacent points by 1 (includes diagonals.)
- If any of the adjacent points are also increased to > 9, they will also flash. 
- An octopus can only flash once per step.
- Any octopus that flashes has its energy level set to 1. 


One star:
find the total number of flashes after 100 steps 
'''

INPUT_FILE = "inputs/day_11_input.txt"
TEST_FILE = "inputs/day_11_test_input.txt"


def load_file(filename: str) -> list[list[int]]:
    '''Loads the file as a grid of integers'''

    with open(filename, "r") as f:
        lines = f.readlines()

    lines = [l.replace("\n", "").replace(" ", "") for l in lines]
    arr = []
    for line in lines:
        arr.append([int(i) for i in line])
    return arr


def get_adjacent(x, y, dim: int) -> list[tuple]:
    '''Returns a list of tuples containing all the adjacent points to the position (x,y). This includes the points itself.'''
    pos = [(x+i, y+j) for i in range(-1, 2)
           for j in range(-1, 2) if x+i in range(dim) and y+j in range(dim)]
    return pos


def get_all_idcs(dim: int) -> list[tuple]:
    return [(i, j) for i in range(dim) for j in range(dim)]


def get_item(idx, arr):
    '''Returns the item at index idx'''
    i, j = idx
    return arr[i][j]


def get_flashed(arr, to_exclude: list = []) -> list[tuple]:
    '''Return a list of indeces that have flashed. Excludes those in the to_exclude list'''

    all_idcs = get_all_idcs(len(arr))
    return [idx for idx in all_idcs if get_item(idx, arr) > 9 and idx not in to_exclude]


def increment_arr(increment: int, arr: list) -> list:
    '''Increment an array by some fixed amount'''
    dim = len(arr)
    for i in range(dim):
        for j in range(dim):
            arr[i][j] += increment
    return arr


def update_state(arr: list[list]) -> list[list]:
    '''Perform one update step.'''
    dim = len(arr)
    print(arr)
    all_idcs = get_all_idcs(dim)

    # increase all points by 1
    arr = increment_arr(1, arr)

    flashed = get_flashed(arr)  # queue of flashed points to consider

    already_considered = []

    while flashed:

        flashed_idx = flashed.pop(0)

        already_considered.append(flashed_idx)

        neighbourhood = get_adjacent(flashed_idx)
        for idx in neighbourhood:

            if idx != flashed_idx:
                i, j = idx
                arr[i][j] += 1
                if arr[i][j] == 10:
                    # it's just had a flash triggered
                    flashed.append((i, j))
            else:
                arr[i][j] = 0

    return arr


def one_star(filename: str):
    '''Returns the one star solution'''
    lines = load_file(filename)

    return update_state(lines)


def two_star(filename: str):
    '''Returns the two star solution'''

    return


if __name__ == "__main__":
    print(f"One star solution is {one_star(TEST_FILE)}")
    print(f"Two star solution is {two_star(TEST_FILE)}")
    print(f"One star solution is {one_star(INPUT_FILE)}")
    print(f"Two star solution is {two_star(INPUT_FILE)}")
