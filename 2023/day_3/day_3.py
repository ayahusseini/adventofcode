'''Solution to advent of code day 3 2023
'''

INPUT_FILE = "inputs/day_3_input.txt"
TEST_FILE = "inputs/day_3_test_input.txt"


class Grid:
    def __init__(self, rows: list[list[str]]):
        '''Instantiates a grid'''
        self.rows = rows
        self.nrows = len(rows)
        self.ncols = len(rows[0])

        self.marked = set()
        self.symbol_pos = Grid.get_symbol_idx(rows)

    def get_part_numbers(self) -> list[int]:
        '''Return a list of part numbers'''
        self.marked = set()
        part_numbers = []
        for s_idx in self.symbol_pos:
            part_numbers += self.get_part_number_for_idx(s_idx)
        return part_numbers

    def get_part_number_for_idx(self, idx: tuple):
        '''Return a list of part numbers next to a given index'''
        adjacent = [idx for idx in self.get_adjacent(
            idx) if self.rows[idx[0]][idx[1]].isnumeric()]
        return [self.extract_full_num(i, cache=True)
                for i in adjacent if i not in self.marked]

    def get_gear_ratios(self) -> list[int]:
        '''Return a list of gear ratios'''
        self.marked = set()
        gear_ratios = []
        for s in self.symbol_pos:
            part_numbers = self.get_part_number_for_idx(s)
            if len(part_numbers) == 2:
                gear_ratios.append(part_numbers[0]*part_numbers[1])
        return gear_ratios

    def get_adjacent(self, idx: tuple):
        '''Return a list of tuples adjacent to index'''
        return [
            (r, c) for r in range(idx[0]-1, idx[0]+2)
            if r >= 0 and r < self.nrows
            for c in range(idx[1]-1, idx[1]+2)
            if c >= 0 and c < self.ncols and (r, c) != idx]

    def traverse_row(self, row_num: int, start_col: int, step: int, condition):
        '''Traverses a row in a specific direction'''

        entries = []

        row = self.rows[row_num]

        col = start_col

        while 0 <= col < self.ncols and condition(row[col]):
            entries.append(row[col])
            col += step

        return entries

    def extract_full_num(self, idx: tuple, cache: bool = False) -> int:
        '''Extract the full number that idx is a part of'''
        if not self.rows[idx[0]][idx[1]].isnumeric():
            raise ValueError("The idx must point to a number")
        row = self.rows[idx[0]]

        behind = self.traverse_row(
            idx[0], idx[1]-1, -1, lambda x: x.isnumeric())[::-1]

        front = self.traverse_row(idx[0],
                                  idx[1]+1, +1, lambda x: x.isnumeric())

        number = int("".join(behind+[row[idx[1]]]+front))
        if cache:
            self.marked.update([(idx[0], idx[1]+n)
                                for n in range(-len(behind), len(front)+1)])
        return number

    @ staticmethod
    def is_symbol(string: str) -> bool:
        '''Returns True if a string is a symbol'''
        return not string.isalnum() and string != "."

    @ staticmethod
    def get_symbol_idx(grid: list[list]):
        '''Return the indeces of all symbols'''
        idxs = []
        for r, row in enumerate(grid):
            for c, col in enumerate(row):
                if Grid.is_symbol(col):
                    idxs.append((r, c))
        return idxs


def load_file(filename: str) -> list[str]:
    '''Loads the file as a list of integers'''

    with open(filename, "r") as f:
        lines = f.readlines()

    return [l.replace("\n", "") for l in lines]


def one_star(filename: str):
    '''Returns the one star solution'''

    lines = load_file(filename)
    grid = Grid([[s for s in l]for l in lines])
    return sum(grid.get_part_numbers())


def two_star(filename: str):
    '''Returns the two star solution'''
    lines = load_file(filename)
    grid = Grid([[s for s in l]for l in lines])
    return sum(grid.get_gear_ratios())


if __name__ == "__main__":

    print(f"One star test solution is {one_star(TEST_FILE)}")
    print(f"Two star test solution is {two_star(TEST_FILE)}")
    print(f"One star solution is {one_star(INPUT_FILE)}")
    print(f"Two star solution is {two_star(INPUT_FILE)}")
