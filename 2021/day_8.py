'''Solution to day 8 2021.

The message is decoded by noticing that each segment belongs to a unique set of digits. This is what is distinguishes each segment, and is used to map a letter to the corresponding segment.'''

from collections import defaultdict

TEST_FILE = "inputs/day_8_test_input.txt"
INPUT_FILE = "inputs/day_8_input.txt"
SEPARATOR = "|"


SEGMENTS_USED = {
    0: {'T', 'B', 'TL', 'TR', 'BL', 'BR'},
    1: {'TR', 'BR'},
    2: {'T', 'M', 'B', 'TR', 'BL'},
    3: {'T', 'B', 'M', 'TR', 'BR'},
    4: {'TL', 'TR', 'M', 'BR'},
    5: {'T', 'B', 'M', 'TL', 'BR'},
    6: {'T', 'B', 'M', 'TL', 'BR', 'BL'},
    7: {'T', 'TR', 'BR'},
    8: {'T', 'B', 'M', 'TL', 'TR', 'BL', 'BR'},
    9: {'T', 'B', 'M', 'TL', 'TR', 'BR'}
}

SEGMENT_TO_DIGITS = {
    'T': [0, 2, 3, 5, 6, 7, 8, 9],
    'TL': [0, 4, 5, 6, 8, 9],
    'TR': [0, 1, 2, 3, 4, 7, 8, 9],
    'M': [2, 3, 4, 5, 6, 8, 9],
    'BL': [0, 2, 6, 8],
    'BR': [0, 1, 3, 4, 5, 6, 7, 8, 9],
    'B': [0, 2, 3, 5, 6, 8, 9]
}

UNIQUE = [1, 4, 7, 8]


def map_wire_to_word_lengths(words: list) -> dict:
    '''Return a dictionary containing letters, and the length of words they appear in.'''
    wires = {i: [] for i in "abcdefg"}
    for word in words:
        for i in word:
            wires[i].append(len(word))
    return wires


def map_segment_to_word_lengths() -> dict:
    '''Return a dictionary mapping segments to the length of words they appear in'''
    segments = {}
    for k, v in SEGMENT_TO_DIGITS.items():
        segments[k] = []
        for digit in v:
            num_segments = len(SEGMENTS_USED[digit])
            segments[k].append(num_segments)
    return segments


def match_wire_to_segment(wires_map: dict, segments_map: dict) -> dict:
    '''Return a dictionary mapping wire keys to segment keys where they have matching values.'''
    matches = {}
    for w, lw in wires_map.items():
        for s, ls in segments_map.items():
            if sorted(lw) == sorted(ls):
                matches[w] = s
    return matches


def decode_messages(wires_to_segments: dict, words: list) -> str:
    '''Return the corresponding digits to a list of words.'''
    digits = []
    for wires in words:
        segments_used = set([wires_to_segments[l] for l in wires])
        for k, v in SEGMENTS_USED.items():
            if segments_used == v:
                digits.append(str(k))
                break
    return int("".join(digits))


def load_file(filename: str) -> list[str]:
    '''Loads the file as a list of messages split into output and input.'''
    messages = []
    with open(filename, "r") as f:
        lines = f.readlines()
        for line in lines:
            message = line.replace(
                "\n", "").split(SEPARATOR)
            messages.append([m.strip().split(" ") for m in message])

    return messages


def count_unique_num(digits_list: list[str]):
    '''Return the number of digits which use a unique number of segments.'''
    counter = 0
    num_segment_to_unique_digit = {
        len(SEGMENTS_USED[digit]): digit for digit in UNIQUE}

    for digit in digits_list:
        num_segments_used = len(set(digit))
        if num_segments_used in num_segment_to_unique_digit.keys():
            counter += 1
    return counter


def one_star(filename: str):
    '''Returns the one star solution'''
    messages = load_file(filename)
    total = 0
    for message in messages:
        total += count_unique_num(message[1])
    return total


def two_star(filename: str):
    '''Returns the one star solution'''
    messages = load_file(filename)
    segment_map = map_segment_to_word_lengths()
    digits = []
    for message in messages:
        wire_map = map_wire_to_word_lengths(message[0])
        matches = match_wire_to_segment(wire_map, segment_map)
        digits.append(decode_messages(matches, message[1]))
    return sum(digits)


if __name__ == "__main__":
    print(f"One star test solution is {one_star(TEST_FILE)}")
    print(f"Two star test solution is {two_star(TEST_FILE)}")
    print(f"One star solution is {one_star(INPUT_FILE)}")
    print(f"Two star solution is {two_star(INPUT_FILE)}")
