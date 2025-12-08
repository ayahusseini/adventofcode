"""Solution to advent of code 2015 day 2"""

FILENAME = "inputs/day_2_input.txt"


def extract_data(filename: str) -> list[str]:
    """Return the data as a list of separate lines"""

    r = []
    with open(filename, "r") as f:
        for line in f.readlines():
            r.append(line.replace("\n", "").strip())
    return r


def get_dimensions_from_string(line: str) -> tuple[int, int, int]:
    """Return a tuple with the dimensions"""
    s = line.split("x")
    return tuple([int(i) for i in s])


def get_surface_area(l: int, w: int, h: int) -> int:
    """Return the surface area of a box."""
    return 2 * l * w + 2 * w * h + 2 * h * l


def get_smallest_side_area(l: int, w: int, h: int) -> int:
    """Return the area of the smallest side"""
    return min([l * w, w * h, h * l])


def get_smallest_side_perimeter(l: int, w: int, h: int) -> int:
    """Return the perimeter of the smallest side."""
    return min([2 * (l + w), 2 * (w + h), 2 * (h + l)])


def get_volume(l: int, w: int, h: int) -> int:
    """Return the present volume"""
    return l * w * h


def one_star_solution():
    """Get the feet of wrapping paper required."""
    data = extract_data(FILENAME)
    dimensions = []
    for line in data:
        dimensions.append(get_dimensions_from_string(line))
    return sum([get_surface_area(*d) + get_smallest_side_area(*d) for d in dimensions])


def two_star_solution():
    """Get the feet of ribbon required"""
    data = extract_data(FILENAME)
    dimensions = []
    for line in data:
        dimensions.append(get_dimensions_from_string(line))
    return sum([get_smallest_side_perimeter(*d) + get_volume(*d) for d in dimensions])


if __name__ == "__main__":
    print(one_star_solution())
    print(two_star_solution())
