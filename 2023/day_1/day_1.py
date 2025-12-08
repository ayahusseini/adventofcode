"""Solution to advent of code day 1 2023"""

INPUT_FILE = "inputs/day_1_input.txt"
TEST_FILE = "inputs/day_1_test_input.txt"
TEST_FILE_2 = "inputs/day_1_test_input_2.txt"


def load_file(filename: str) -> list[int]:
    """Loads the file as a list of integers"""

    with open(filename, "r") as f:
        lines = f.readlines()

    return [l.replace("\n", "").replace(" ", "") for l in lines]


def first_number(text: str) -> tuple[str, int]:
    """Returns the first number in the string, and its index."""
    for i, s in enumerate(text):
        if s.isnumeric():
            return s, i


def first_text_digit(text: str, digits: dict) -> tuple[str, int]:
    """Returns the first text digit in the string and its index"""

    i = 0
    while i < len(text):
        j = i + 1
        while j < len(text):
            substring = text[i : j + 1]
            if substring in digits:
                return digits[substring], i
            j += 1
        i += 1


def first_digit(string: str, digit_map: dict) -> tuple[str, int]:
    """Returns the first digit in the string and its index.
    Includes those represented as words."""

    num = first_number(string)
    word = first_text_digit(string, digit_map)

    if word is None and num is None:
        raise ValueError("No digits found")

    if word is None:
        return num

    if num is None:
        return word

    return min(num, word, key=lambda x: x[1])


def one_star(filename: str):
    """Returns the one star solution"""

    lines = load_file(filename)

    return sum([int(first_number(l)[0] + first_number(l[::-1])[0]) for l in lines])


def two_star(filename: str):
    """Returns the two star solution"""

    lines = load_file(filename)

    digits = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    digits_reversed = {k[::-1]: v for k, v in digits.items()}

    return sum(
        [
            int(first_digit(l, digits)[0] + first_digit(l[::-1], digits_reversed)[0])
            for l in lines
        ]
    )


if __name__ == "__main__":
    print(f"One star test solution is {one_star(TEST_FILE)}")
    print(f"Two star test solution is {two_star(TEST_FILE_2)}")
    print(f"One star solution is {one_star(INPUT_FILE)}")
    print(f"Two star solution is {two_star(INPUT_FILE)}")
