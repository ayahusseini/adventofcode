"""Solution to advent of code day 9 2024"""
INPUT_FILE = "inputs/day_9_input.txt"
TEST_FILE = "inputs/day_9_test_input.txt"


class Files:
    def __init__(self, disk_space: dict):
        """Instantiates a file."""
        self.disk = disk_space

    @classmethod
    def from_line(cls, line: str):
        """Instantiates the files from a line of text."""
        disk = dict()
        write_to = 0

        for id, i in enumerate(range(0, len(line), 2)):
            batch = line[i:i+2]
            batch = batch + "0" if len(batch) < 2 else batch

            num_blocks = int(batch[0])
            gap = int(batch[1])

            for pointer in range(write_to, write_to + num_blocks):
                disk[pointer] = id

            write_to += num_blocks + gap

        return cls(disk)

    def swap(self, l_idx: int, r_idx: int) -> None:
        """Swaps two characters."""
        self.disk[l_idx], self.disk[r_idx] = self.disk[r_idx], self.disk[l_idx]

    def checksum(self) -> int:
        """Returns the checksum."""
        return sum([idx * int(id) for idx, id in self.disk.items()])

    def __str__(self) -> str:
        """String representation."""
        text = ["." for _ in range(max(self.disk.keys()) + 1)]
        for idx, file_id in self.disk.items():
            text[idx] = str(file_id)
        return "".join(text)


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
