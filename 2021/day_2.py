'''Solution to day 2'''

FILE = "inputs/day_2_input.txt"
DIRECTIONS = {
    "forward": [1, 0],
    "up": [0, -1],
    "down": [0, 1]
}


def get_net_directions_count(filename: str) -> list[str]:
    net_directions = {"forward": 0, "up": 0, "down": 0}
    with open(filename, "r") as f:
        while True:
            line = f.readline()
            if not line:
                break
            key, val = line.replace("\n", "").strip().split()

            if net_directions.get(key.strip()) is not False:
                net_directions[key.strip()] += int(val)
    return net_directions


def add_vectors(v1, v2):
    if len(v1) == len(v2):
        return [v1[i] + v2[i] for i in range(len(v1))]


def multiply_scalar(s, v):
    return [s*v_i for v_i in v]


def find_net_direction(counts: dict):
    net = [0, 0]

    for direction, count in counts.items():
        orientation = DIRECTIONS[direction]
        net = add_vectors(net, multiply_scalar(count, orientation))

    return net

# TODO sep load, process and get answer functions


def find_net_direction_with_aim(filename: str) -> list[int, int]:

    increments = {
        "forward": lambda curr: [1, curr[2], 0],
        "up": lambda curr: [0, 0, -1],
        "down": lambda curr: [0, 0, 1]
    }

    net = [0, 0, 0]  # horizontal,depth, aim
    with open(filename, "r") as f:
        for line in f.readlines():

            key, val = line.replace("\n", "").strip().split()

            next_increment = multiply_scalar(int(val), increments[key](net))

            print(next_increment)

            net = add_vectors(net, next_increment)
            print(f"net = {net}")
        return net


def find_net_dir_with_aim_2(filename: str):
    net = {"horizontal": 0, "depth": 0, "aim": 0}
    with open(filename, "r") as f:
        for line in f.readlines():
            key, val = line.replace("\n", "").strip().split()
            val = int(val)
            if key == "forward":
                net["horizontal"] += val
                net["depth"] += net["aim"] * val
            elif key == "up":
                net["aim"] -= val
            else:
                net["aim"] += val
    return net


if __name__ == "__main__":
    c = get_net_directions_count(FILE)

    print(find_net_direction_with_aim(FILE))
    net2 = find_net_dir_with_aim_2(FILE)
    print(net2)
