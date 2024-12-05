'''Solution to advent of code day 5 2024
'''

INPUT_FILE = "inputs/day_5_input.txt"
TEST_FILE = "inputs/day_5_test_input.txt"


class Page:
    def __init__(self, num: str):
        self.page_num = num
        self.prev = set()
        self.next = set()

    def __gt__(self, page2):
        return (page2 in self.prev) or not (page2 in self.next)

    def __str__(self):
        return str(self.page_num)

    def __repr__(self):
        return str(self.page_num)


class RuleSet:
    def __init__(self):
        self.pages = dict()

    def add_rule(self, before: Page, after: Page):
        """Adds a rule"""
        before.next.add(after)
        after.prev.add(before)

        if before in self.pages:
            for page in before.prev:
                page.next.add(after)
        else:
            self.pages[before.page_num] = before

        if after in self.pages:
            for page in after.next:
                page.prev.add(before)
        else:
            self.pages[after.page_num] = after

    def is_sorted(self, pages: list[int]):
        """Returns True if a list of page numbers is sorted in increasing order."""
        for i in range(0, len(pages) - 1):
            p1, p2 = pages[i:i+2]
            if self.pages[p1] > self.pages[p2]:
                return False


def load_file(filename: str):
    '''Loads the file'''

    with open(filename, "r") as f:
        lines = f.readlines()

    return lines


def one_star(filename: str):
    '''Returns the one star solution'''


def two_star(filename: str):
    '''Returns the two star solution'''


if __name__ == "__main__":

    print(f"One star test solution is {one_star(TEST_FILE)}")
    print(f"Two star test solution is {two_star(TEST_FILE)}")
    print(f"One star solution is {one_star(INPUT_FILE)}")
    print(f"Two star solution is {two_star(INPUT_FILE)}")
