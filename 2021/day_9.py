'''Solution to advent of code day 9 2021

Input:
List of strings of numbers.
Each number corresponds to the height of a particular location, ranging from 0 (min) to 9 (max)

One star:
Find the sum of the low points (lower than adjacent locations) + number of low points
Note: if a point is a minimum, then none of it's adjacent points are minima.

Two star:
Find the product of the size of each basin. A basin is the region around a minimum point, 
bordered by 9's 
'''

INPUT_FILE = "inputs/day_9_input.txt"


def load_file(filename: str) -> list[int]:
    '''Loads the file as a list of integers'''

    with open(filename, "r") as f:
        lines = f.readlines()

    return [l.replace("\n", "") for l in lines]


def get_array(strings: list) -> list:
    '''Get an array representing the heightmap'''
    arr = []
    for i in strings:
        arr.append([int(l) for l in i])
    return arr


def get_adjacent_indeces(row: int, col: int, arr: list) -> list:
    '''Return a list of tuples containing the indeces of adjacent points'''
    max_row = len(arr) - 1
    max_col = len(arr[0]) - 1

    adjacent = []
    for i in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col-1)]:
        x, y = i
        if x in range(0, max_row+1) and y in range(0, max_col+1):
            adjacent.append(i)

    return adjacent


def is_point_min(row: int, col: int, arr: list) -> bool:
    '''Returns True/False if a point is or isn't an integer'''
    adjacent = get_adjacent_indeces(row, col, arr)
    point = arr[row][col]

    if point < min(arr[r][c] for r, c in adjacent):

        return True
    return False


def find_minima(arr: list) -> tuple[list, list]:
    '''Return a list of minimum points height'''
    minima_heights = []
    minima_idxs = []
    idxs = [(i, j) for i in range(len(arr)) for j in range(len(arr))]
    not_min = []  # contains points determined not to be minima
    for idx in idxs:
        if idx not in not_min:
            row, col = idx

            if is_point_min(row, col, arr):

                minima_heights.append(arr[row][col])
                minima_idxs.append((row, col))
                not_min += get_adjacent_indeces(row, col, arr)

    return minima_heights, minima_idxs


def find_size_of_basin_around_min_point(min_r: int, min_c: int, arr: list[list]) -> int:
    '''Given a point assumed to be a minimum, find the size of the basin around it.'''
    edges = set(get_adjacent_indeces(min_r, min_c, arr))
    already_considered = set()
    size = 0
    while len(edges) > 0:
        already_considered.update(edges)
        for edge in list(edges).copy():

            i, j = edge
            val = arr[i][j]

            if val != 9:
                size += 1

                edges.update(get_adjacent_indeces(i, j, arr))
            edges = edges - already_considered

    return size


def one_star(filename: str):
    '''Returns the one star solution'''
    map = load_file(filename)
    arr = get_array(map)
    minima = find_minima(arr)[0]
    return sum(minima) + len(minima)


def two_star(filename: str):
    '''Returns the one star solution'''
    map = load_file(filename)
    arr = get_array(map)
    minima = find_minima(arr)[1]
    sizes = []
    for x, y in minima:
        sizes.append(find_size_of_basin_around_min_point(x, y, arr))
    sizes.sort(reverse=True)
    return sizes[0] * sizes[1] * sizes[2]


if __name__ == "__main__":
    print(f"One star solution is {one_star(INPUT_FILE)}")
    print(f"Two star solution is {two_star(INPUT_FILE)}")
