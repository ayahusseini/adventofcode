'''Solution to day_5 2021'''


TEST_FILE = "inputs/day_5_test.txt"
INPUT_FILE = "inputs/day_5_input.txt"


def load_endpoints(filename: str) -> list[list[tuple]]:
    '''Return a list of endpoints. item contains [(x1,y1),(x2,y2)]'''
    endpoints = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.replace("\n", "")
            start_string, end_string = line.replace(" ", "").split("->")
            start_coord = convert_coordinate_string(start_string)
            end_coord = convert_coordinate_string(end_string)
            endpoints.append([start_coord, end_coord])
    return endpoints


def convert_coordinate_string(coord: str) -> tuple:
    return tuple([int(i) for i in coord.split(",")])


def is_straight(start, end):
    x1, y1 = start
    x2, y2 = end
    return x1 == x2 or y1 == y2


def find_coverage_of_straight_line(start, end):
    '''Return the list of points that a straight line would cover with start and endpoints'''
    x1, y1 = start
    x2, y2 = end
    is_horizontal = y1 == y2
    is_vertical = x1 == x2
    coverage = []
    if is_horizontal:
        x = [x1, x2]
        x.sort()
        for x_coord in range(x[0], x[1]+1):
            coverage.append((x_coord, y1))
    elif is_vertical:
        y = [y1, y2]
        y.sort()
        for y_coord in range(y[0], y[1]+1):
            coverage.append((x1, y_coord))
    return coverage


def create_coverage_counter(points_covered: list) -> dict:
    counter = {f"{point}": points_covered.count(
        point) for point in points_covered}
    return counter


def one_star(filename):
    endpoints = load_endpoints(filename)
    non_diag = list(filter(lambda x: is_straight(x[0], x[1]), endpoints))
    coverage = []
    counter = 0
    for i, endpoints in enumerate(non_diag):
        print(f"handling line {i}")
        s, e = endpoints

        new_coverage = find_coverage_of_straight_line(s, e)
        print("found_new_cov")
        coverage += new_coverage

    counter = create_coverage_counter(coverage)

    more_than_2 = list(filter(lambda x: x[1] > 1, counter.items()))
    return len(more_than_2)


if __name__ == "__main__":

    print(one_star(INPUT_FILE))
