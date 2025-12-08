"""day 5"""


def load_file(filename: str) -> list[str]:
    with open(filename, "r") as f:
        lines = f.readlines()
    return lines


def is_three_vowels(string: str) -> bool:
    vowels = ["a", "e", "i", "o", "u"]
    count = 0
    for letter in string:
        if letter in vowels:
            count += 1
    return count >= 3


def one_letter_twice(string: str) -> bool:
    for i, l in enumerate(string[:-1]):
        if l == string[i + 1]:
            return True
    return False


def doesnt_contain_invalid(string: str) -> bool:
    disallowed = ["ab", "cd", "pq", "xy"]
    for s in disallowed:
        if s in string:
            return False
    return True


def one_letter_sandwiched(string: str) -> bool:
    for i, l in enumerate(string[:-2]):
        if l == string[i + 2]:
            return True
    return False


def non_overlapping_pair(string: str) -> bool:
    for i in range(len(string[:-1])):
        substring = string[i : i + 2]
        for j in range(i + 2, len(string[:-1])):
            if substring == string[j : j + 2]:
                return True
    return False


def all_conditions_one_star(string: str) -> bool:
    return (
        doesnt_contain_invalid(string)
        and one_letter_twice(string)
        and is_three_vowels(string)
    )


def all_conditions_two_star(string: str) -> bool:
    return non_overlapping_pair(string) and one_letter_sandwiched(string)


if __name__ == "__main__":
    all_words = load_file("input.txt")
    count = len(list(filter(all_conditions_one_star, all_words)))
    print("one star solution " + str(count))

    count = len(list(filter(all_conditions_two_star, all_words)))
    print("Two star solution " + str(count))
