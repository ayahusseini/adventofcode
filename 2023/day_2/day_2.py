"""Solution to advent of code day 2 2023"""

INPUT_FILE = "inputs/day_2_input.txt"
TEST_FILE = "inputs/day_2_test_input.txt"


class Game:
    def __init__(self, gameid: int, subsets: list[dict]):
        """Instantiate a game object"""
        self.id = gameid
        self.subsets = subsets

    @classmethod
    def from_line(cls, line: str):
        """Instantiate a game object from a line"""
        game_id = get_id(line)
        subset_lines = line.split(":")[-1].strip().split(";")
        subsets = [get_subresult(l) for l in subset_lines]
        return cls(game_id, subsets)

    def get_max(self) -> dict:
        """Returns the max number of red, green, blue across all subsets"""
        maxima = {"red": 0, "green": 0, "blue": 0}
        for c in ["red", "green", "blue"]:
            maxima[c] = max(self.subsets, key=lambda x: x[c])[c]
        return maxima

    def is_possible(self, max_r: int, max_g: int, max_b: int):
        """Returns True if a game is possible had a bag been loaded with a certain configuration."""
        total = self.get_max()
        return (
            total["red"] <= max_r and total["green"] <= max_g and total["blue"] <= max_b
        )

    def get_power(self) -> int:
        """Returns the power of the minimum set"""
        min_set = self.get_max()
        product = 1
        for v in min_set.values():
            product *= v
        return product


def load_file(filename: str) -> list[str]:
    """Loads the file as a list of integers"""

    with open(filename, "r") as f:
        lines = f.readlines()

    return [l.replace("\n", "") for l in lines]


def get_id(line: str) -> int:
    """Returns the game id as an integer"""
    return int(line.split(":")[0].split(" ")[-1])


def get_subresult(subresult_line: str) -> dict:
    """Given a subset of results, return a count of each colour"""
    counts = {"red": 0, "green": 0, "blue": 0}
    for r in subresult_line.split(","):
        count_colour = r.strip().split(" ")
        counts[count_colour[-1]] = int(count_colour[0])
    return counts


def one_star(filename: str):
    """Returns the one star solution"""

    lines = load_file(filename)
    games = [Game.from_line(l) for l in lines]
    return sum([g.id for g in games if g.is_possible(12, 13, 14)])


def two_star(filename: str):
    """Returns the two star solution"""
    lines = load_file(filename)
    games = [Game.from_line(l) for l in lines]
    return sum([g.get_power() for g in games])


if __name__ == "__main__":
    print(f"One star test solution is {one_star(TEST_FILE)}")
    print(f"Two star test solution is {two_star(TEST_FILE)}")
    print(f"One star solution is {one_star(INPUT_FILE)}")
    print(f"Two star solution is {two_star(INPUT_FILE)}")
