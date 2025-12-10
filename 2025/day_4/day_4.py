"""Solution to advent of code day 4 2025"""
import numpy as np
INPUT_FILE = "inputs/day_4_input.txt"
TEST_FILE = "inputs/day_4_test_input.txt"


def load_file(filename: str):
    """Load the puzzle input, yielding stripped lines."""
    with open(filename, "r") as f:
        lines = [list(l.strip()) for l in f]
    arr = np.array(lines)
    return (arr == "@").astype(int)


def get_neighbourhood(rows: int, cols: int, r: int, c: int) -> tuple:
    """Get the neighbourhood around (r,c) in an array of shape (rows, cols)
    Return the neighbourhood as the slice parameters rstart, rend, cstart, cend """
    rstart, rend = max(0, r - 1), min(rows, r + 1)
    cstart, cend = max(0, c - 1), min(cols, c + 1)
    return rstart, rend, cstart, cend


def get_true_neighbour_count(arr: np.ndarray) -> np.ndarray:
    """Given arr, a 2D boolean array, return an array 
    where the entry at (r,c) shows how many '1' neighbours it has
    in arr.
    """

    padded = np.pad(arr, 1, mode='constant', constant_values=0)
    neighbours = np.zeros_like(padded)
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if dr == dc and dc == 0:
                continue
            neighbours += np.roll(np.roll(padded, dr, axis=0), dc, axis=1)
    return neighbours[1:-1, 1:-1]


def meets_condition(is_roll: np.ndarray, neighbours: np.ndarray) -> np.ndarray:
    """Return whether or not a position meets the conditions is_roll and neighbours < 4"""
    return (neighbours < 4) & (is_roll != 0)


def remove_rolls(remove_roll: np.ndarray, is_roll: np.ndarray, neighbours: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """updates is_roll and neighbours by removing all removable rolls"""
    removable_neighbourhood = get_true_neighbour_count(remove_roll.astype(int))
    is_roll[remove_roll] = 0  # boolean mask; clears removable rolls
    neighbours -= removable_neighbourhood
    return is_roll, neighbours


def one_star(filename: str):
    """Solve part 1 for day 4."""
    arr = load_file(filename)
    n = get_true_neighbour_count(arr)
    return meets_condition(arr, n).sum()


def two_star(filename: str):
    """Solve part 2 for day 4."""
    arr = load_file(filename)
    n = get_true_neighbour_count(arr)
    total = 0
    accessible = meets_condition(arr, n).sum()
    while accessible > 0:
        remove_roll = meets_condition(arr, n)
        arr, n = remove_rolls(remove_roll, arr, n)
        accessible = remove_roll.astype(int).sum()
        total += accessible

    return total


if __name__ == "__main__":
    print(f"One star test solution is {one_star(TEST_FILE)}")
    print(f"Two star test solution is {two_star(TEST_FILE)}")
    print(f"One star solution is {one_star(INPUT_FILE)}")
    print(f"Two star solution is {two_star(INPUT_FILE)}")
