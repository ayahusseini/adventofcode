"""Solution to advent of code day 9 2024"""
INPUT_FILE = "inputs/day_9_input.txt"
TEST_FILE = "inputs/day_9_test_input.txt"


class Files:
    def __init__(self, disk_space: str):
        """Instantiates a file."""
        self.disk_space = disk_space

    @classmethod
    def from_line(cls, line: str):
        """Instantiates the files from a line of text"""
        disk = ""
        for num, i in enumerate(range(0, len(line), 2)):
            batch = line[i:i+2]
            disk += f"{str(num) * int(batch[0])}"

            if len(batch) == 2:
                disk += "." * int(batch[1])
        return cls(disk)

    def checksum(self):
        """Returns the checksum."""
        return sum([idx * int(id) for idx, id in enumerate(self.disk_space) if id.isdigit()])

    def __repr__(self):
        return self.disk_space


def load_file(filename: str) -> str:
    """Loads the file as a string"""
    with open(filename, "r") as f:
        line = f.readline().strip()
    return line


def one_star(filename: str):
    """Returns the one star solition"""
    files = Files.from_line(load_file(filename))

    files.move_rightmost_blocks()

    return files.checksum()


def two_star(filename: str):
    '''Returns the two star solution'''
    files = Files.from_line(load_file(filename))

    files.move_rightmost_files()

    return files.checksum()


if __name__ == "__main__":
    print(f"One star test solution is {one_star(TEST_FILE)}")
    print(f"Two star test solution is {two_star(TEST_FILE)}")
    print(f"One star solution is {one_star(INPUT_FILE)}")
    # print(f"Two star solution is {two_star(INPUT_FILE)}")
