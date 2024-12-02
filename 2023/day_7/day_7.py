'''Solution to advent of code day 7 2023
'''
from collections import defaultdict

INPUT_FILE = "inputs/day_7_input.txt"
TEST_FILE = "inputs/day_7_test_input.txt"


class Card:
    """A card within a hand"""
    symbols = ['A', 'K', 'Q', 'J', '9', '8', '7', '6', '5', '4', '3', '2']
    strengths = {s: i for i, s in enumerate(symbols[::-1])}

    def __init__(self, symbol: str):
        """Instantiate a card"""
        if not symbol in Card.symbols:
            raise ValueError("Invalid symbol")
        self.symbol = symbol
        self.strength = Card.strengths[self.symbol]

    def __gt__(self, card2):
        return self.strength > card2.strength

    def __lt__(self, card2):
        return self.strength < card2.strength

    def __eq__(self, card2):
        return self.strength == card2.strength


class Hand:
    """A collection of cards"""
    frequency_id = {
        (1, 1, 1, 1, 1): 0,
        (2, 1, 1, 1): 1,
        (2, 2, 1): 2,
        (3, 1, 1): 3,
        (3, 2): 4,
        (4, 1): 5,
        (5,): 6
    }

    def __init__(self, cards: list[Card], bid: int):
        """Instantiates a hand"""
        self.cards = cards
        self.bid = bid
        self.hand_type = Hand.frequency_id[self.frequency_pattern(cards)]

    def are_cards_stronger(self, hand2) -> bool:
        """Compares the card-by-card strength of two hands"""

    @staticmethod
    def frequency_pattern(cards) -> tuple:
        """Returns the sorted frequency pattern of a set of cards"""
        frequencies = defaultdict(lambda: 0)
        for c in cards:
            frequencies[c.symbol] += 1
        return tuple(sorted(frequencies.values(), reverse=True))

    @classmethod
    def from_line(cls, line: str):
        """Instantiates a hand from an input line"""
        hand, bid = line.split(' ')
        cards = [Card(l) for l in hand]
        return cls(cards, int(bid))


def load_file(filename: str) -> list:
    '''Loads the file as '''

    with open(filename, "r") as f:
        lines = f.readlines()


def one_star(filename: str) -> int:
    '''Returns the one star solution'''


def two_star(filename: str):
    '''Returns the two star solution'''


if __name__ == "__main__":
    print(f"One star test solution is {one_star(TEST_FILE)}")
    print(f"Two star test solution is {two_star(TEST_FILE)}")
    print(f"One star solution is {one_star(INPUT_FILE)}")
    print(f"Two star solution is {two_star(INPUT_FILE)}")
