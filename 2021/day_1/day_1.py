"""Solve advent of code day_1"""

FILE = "inputs/day_1_input.txt"


def read_input(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return f.readlines()


def get_measurements(filename: str) -> list[int]:
    f = read_input(filename)
    return [int(i.replace("\n", "")) for i in f]


def get_window_sums(m: list[int]) -> list[int]:
    """Get a list containing the sum of each window
    of width 3."""
    sums = []
    for i in range(len(m) - 2):
        j = i + 2
        sums.append(sum(m[i : j + 1]))
    return sums


def num_measurements_bigger_than_prev(m: list) -> int:
    """Return the number of measurements in a list that
    are bigger than the previous one."""
    is_bigger = [0]
    for i in range(1, len(m)):
        if m[i] > m[i - 1]:
            is_bigger.append(1)
        else:
            is_bigger.append(0)
    return sum(is_bigger)


if __name__ == "__main__":
    measurements = get_measurements(FILE)
    # task 1
    print(num_measurements_bigger_than_prev(measurements))
    # task 2
    print(num_measurements_bigger_than_prev(get_window_sums(measurements)))
