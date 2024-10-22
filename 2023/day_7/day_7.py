'''Solution to advent of code day 7 2023
'''
INPUT_FILE = "inputs/day_7_input.txt"
TEST_FILE = "inputs/day_7_test_input.txt"


def get_first_differring_letter(hand1: str, hand2: str) -> list[str]:
    """Returns the first differing letter"""
    for i, l in enumerate(hand1):
        if l != hand2[i]:
            return [l, hand2[i]]


def sort_two_hands_by_strength(hands: list[str]) -> dict:
    '''Return a dictionary of relative strengths'''
    labels = ''.join(['A', 'K', 'Q', 'J', 'T', '9',
                      '8', '7', '6', '5', '4', '3', '2'])


def sort_hands_by_strength(hands: list[str]) -> list[str]:
    '''sorts hands by strength in increasing order'''
    return


def get_num_repeats(hand: str) -> list[int]:
    """Return a list containing the number of cards of each letter in the hand"""
    counts = [hand.count(i) for i in list(set(hand))]
    return sorted(counts, reverse=True)


def score_num_repeats(repeats: list[int]) -> int:
    """Return a score for a particular pattern of repeats"""
    pos_repeats = [[5], [4, 1], [3, 2], [3, 1, 1],
                   [2, 2, 1], [2, 1, 1, 1], [1, 1, 1, 1, 1]][::-1]
    for i, pattern in enumerate(pos_repeats):
        if repeats == pattern:
            return i


def group_hands_by_type(hands: list[str]) -> list[str]:
    groups = {i: [] for i in range(7)}
    for h in hands:
        score = score_num_repeats(get_num_repeats(h))
        groups[score].append(h)
    print(groups)
    return groups


def rank_hands(hands: list[str]) -> list[str]:
    """Rank hands from highest to lowest"""
    sorted_hands = []
    groups = group_hands_by_type(hands)

    for _, g in groups.items():
        sorted_hands += sort_hands_by_strength(g)

    return sorted_hands


def one_star(filename):
    """Returns the one star solution"""


def two_star(filename):
    """Returns the two star solution"""


if __name__ == "__main__":
    print(f"One star solution is {one_star(TEST_FILE)}")
    print(f"Two star solution is {two_star(TEST_FILE)}")
    print(f"One star solution is {one_star(INPUT_FILE)}")
    print(f"Two star solution is {two_star(INPUT_FILE)}")
