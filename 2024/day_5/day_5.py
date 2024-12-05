'''Solution to advent of code day 5 2024
'''

INPUT_FILE = "inputs/day_5_input.txt"
TEST_FILE = "inputs/day_5_test_input.txt"


class Page:
    def __init__(self, num: int):
        self.page_num = num
        self.next = set()

    def __gt__(self, page2):
        return not (page2 in self.next)

    def __str__(self):
        return str(self.page_num)

    def __repr__(self):
        return str(self.page_num)


class RuleSet:
    def __init__(self):
        """Instantiates a set of rules"""
        self.pages = dict()

    def __getitem__(self, val):
        """Returns the key associated with val"""
        return self.pages[val]

    def add_page(self, pagenum: int):
        """Adds a page to the Rule Set"""
        if not pagenum in self.pages:
            self.pages[pagenum] = Page(pagenum)

    def add_rule(self, beforenum: int, afternum: int):
        """Adds an ordering rule"""
        self.add_page(beforenum)
        self.add_page(afternum)

        for page in (self[afternum], *self[afternum].next):
            self[beforenum].next.add(page)

    def is_sorted(self, pages: list[int]):
        """Returns True if a list of page numbers is sorted in increasing order."""
        for i in range(0, len(pages) - 1):
            p1, p2 = pages[i:i+2]
            if p1 not in self.pages or p2 not in self.pages:
                raise ValueError(f"Not enough information about {p1,p2}")
            if self.pages[p1] > self.pages[p2]:
                return False
        return True


def load_file(filename: str) -> tuple[RuleSet, list[list]]:
    """Loads the file as a set of Rules and a list of page updates"""
    rs = RuleSet()
    page_orders = []

    with open(filename, "r") as f:
        lines = f.readlines()
        for l in lines:
            l = l.replace('\n', '').strip()
            if "|" in l:
                num1, num2 = l.split('|')
                rs.add_rule(int(num1), int(num2))
            elif ',' in l:
                page_orders.append([int(n) for n in l.split(',')])

    return rs, page_orders


def one_star(filename: str):
    '''Returns the one star solution'''
    rules, orders = load_file(filename)
    sum = 0
    for order in orders:
        if rules.is_sorted(order):
            sum += order[len(order)//2]
    return sum


def two_star(filename: str):
    '''Returns the two star solution'''


if __name__ == "__main__":

    print(f"One star test solution is {one_star(TEST_FILE)}")
    print(f"Two star test solution is {two_star(TEST_FILE)}")
    print(f"One star solution is {one_star(INPUT_FILE)}")
    print(f"Two star solution is {two_star(INPUT_FILE)}")
