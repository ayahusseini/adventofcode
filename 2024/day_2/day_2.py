'''Solution to advent of code day 2 2024
'''
from collections import defaultdict

INPUT_FILE = "inputs/day_2_input.txt"
TEST_FILE = "inputs/day_2_test_input.txt"


class Report:
    def __init__(self, numbers: list):
        """Instantiates a report object"""
        self.numbers = numbers

    @classmethod
    def from_line(cls, line: str):
        """Instantiates a report from a line"""
        return cls(list(map(lambda x: int(x), line.split(' '))))

    def is_safe(self, num_removals: int = 0) -> bool:
        """Returns True if a report is safe"""
        is_increasing = None
        invalid_count = 0

        for dif in self.get_differences():
            if is_increasing is None:
                is_increasing = dif > 0
            else:
                if is_increasing is not (dif > 0):
                    invalid_count += 1
            if abs(dif) not in range(1, 4):
                invalid_count += 1
            if invalid_count > num_removals:
                return False
        return True

    def get_differences(self):
        """Returns the differences between adjacent pairs"""
        differences = []
        for i in range(0, len(self.numbers)-1):
            yield self.numbers[i] - self.numbers[i+1]


def load_file(filename: str) -> list[Report]:
    '''Loads the file as two lists of integers'''
    reports = []
    with open(filename, "r") as f:
        lines = f.readlines()
        for line in lines:
            reports.append(Report.from_line(line))
    return reports


def one_star(filename: str) -> int:
    '''Returns the one star solution'''
    reports = load_file(filename)
    return sum([r.is_safe() for r in reports])


def two_star(filename: str):
    '''Returns the two star solution'''
    reports = load_file(filename)
    return sum([r.is_safe(num_removals=1) for r in reports])


if __name__ == "__main__":
    print(f"One star test solution is {one_star(TEST_FILE)}")
    print(f"Two star test solution is {two_star(TEST_FILE)}")
    print(f"One star solution is {one_star(INPUT_FILE)}")
    print(f"Two star solution is {two_star(INPUT_FILE)}")
