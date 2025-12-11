"""Solution to advent of code day 1 2025"""

INPUT_FILE = "inputs/day_2_input.txt"
TEST_FILE = "inputs/day_2_test_input.txt"


def parse_range(range_str: str) -> tuple[int, int]:
    """Returnt the first and last IDs in a range"""
    nums = range_str.split("-")
    return int(nums[0]), int(nums[1])


def load_file(filename: str) -> list[str]:
    """Loads the file"""
    with open(filename, "r") as f:
        ranges = f.readline().replace("\n", "").replace(" ", "").split(",")
    for r in ranges:
        yield parse_range(r)


def get_upper_half_pattern_bound(maximum: int, numrepeats: int) -> int | None:
    """get the maximum pattern X that can be repeated X * numrepeats such that it is
    still <= maximum"""
    ndigits = len(str(maximum))

    if ndigits % numrepeats != 0:
        maximum = 10 ** (ndigits - 1) - 1
        ndigits -= 1
        if ndigits <= 0:
            return None

    maxpattern = str(maximum)[: ndigits // numrepeats]

    if int(maxpattern * numrepeats) > maximum:
        return int(maxpattern) - 1

    return int(maxpattern)


def get_lower_half_pattern_bound(minimum: int, numrepeats: int) -> int | None:
    """get the maximum pattern X that can be repeated X * numrepeats such that it is
    still <= maximum"""
    ndigits = len(str(minimum))

    if ndigits % numrepeats != 0:
        minimum = 10 ** (ndigits)
        ndigits += 1

    minpattern = str(minimum)[: ndigits // numrepeats]

    if int(minpattern * numrepeats) < minimum:
        return int(minpattern) + 1

    return int(minpattern)


def get_all_possible_invalid_ids(start: int, end: int, num_repeats: int = 2):
    """Get all invalid IDs
    in a range [start, end] that have num_repeats"""
    uh = get_upper_half_pattern_bound(end, num_repeats)
    lh = get_lower_half_pattern_bound(start, num_repeats)
    if lh <= uh:
        return [int(str(p) * num_repeats) for p in range(lh, uh + 1)]
    return []


def get_all_multiples(num: int) -> list:
    """Return all multiples of num"""
    multiples = []
    for lower in range(1, int(num ** (0.5) // 1) + 2):
        if num % lower == 0:
            higher = num // lower
            multiples += [lower, higher]
    return multiples


def one_star(filename: str):
    """Returns the one star solution"""
    total = 0
    for rng in load_file(filename):
        total += sum(get_all_possible_invalid_ids(rng[0], rng[1], 2))
    return total


def two_star(filename: str):
    """Returns the two star solution"""
    total = 0
    for rng in load_file(filename):
        ndigits = (len(str(rng[0])), len(str(rng[1])))
        invalid_ids = set()
        if ndigits[0] == ndigits[1]:
            possible_reps = get_all_multiples(ndigits[0])
        else:
            possible_reps = get_all_multiples(ndigits[0]) + get_all_multiples(
                ndigits[1]
            )

        for nreps in set(possible_reps):
            if nreps == 1:
                continue
            invalid_ids.update(get_all_possible_invalid_ids(rng[0], rng[1], nreps))
        total += sum(invalid_ids)
    return total


if __name__ == "__main__":
    print(f"One star test solution is {one_star(TEST_FILE)}")
    print(f"Two star test solution is {two_star(TEST_FILE)}")
    print(f"One star solution is {one_star(INPUT_FILE)}")
    print(f"Two star solution is {two_star(INPUT_FILE)}")
