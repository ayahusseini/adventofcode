'''Solution to advent of code day 7 2023
'''

from collections import defaultdict

INPUT_FILE = "inputs/day_7_input.txt"
TEST_FILE = "inputs/day_7_test_input.txt"


class Card:
    """A card within a hand"""
    symbols = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
    strengths = {s: i for i, s in enumerate(symbols[::-1])}

    def __init__(self, symbol: str):
        """Instantiate a card"""
        if not symbol in set(Card.symbols):
            raise ValueError(f"Invalid symbol: {symbol}")
        self.symbol = symbol
        self.strength = self.strengths[self.symbol]

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

        if len(cards) != 5:
            raise ValueError("A hand must have 5 cards")

        self.cards = cards
        self.bid = bid
        self.hand_type = Hand.frequency_id[self.frequency_pattern(cards)]

    def __eq__(self, hand2) -> bool:
        """Returns True if two hands are equal"""
        return self.cards == hand2.cards

    def __gt__(self, hand2) -> bool:
        """Returns True if this hand is greater than hand2"""
        if self.hand_type != hand2.hand_type:
            return self.hand_type > hand2.hand_type
        return self.are_cards_stronger(hand2)

    def __lt__(self, hand2) -> bool:
        """Returns True if this hand is less than hand2"""
        if self.hand_type != hand2.hand_type:
            return self.hand_type < hand2.hand_type

        return self.are_cards_stronger(hand2) == False

    def __str__(self):
        return "".join([c.symbol for c in self.cards])

    def are_cards_stronger(self, hand2) -> bool:
        """Compares the card-by-card strength of two hands"""

        for c1, c2 in zip(self.cards, hand2.cards):
            if c1 != c2:

                return c1 > c2

        return False

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


def JokerHand(Hand):
    """A special case of the hand where the Joker rule is considered."""

    @staticmethod
    def frequency_pattern(cards) -> tuple:
        """Returns the sorted frequency pattern of a set of cards"""
        frequencies = defaultdict(lambda: 0)
        for c in cards:
            frequencies[c.symbol] += 1

        if 'J' in frequencies:
            joker_count = frequencies['J']
            del frequencies['J']

        frequency_pattern = tuple(sorted(frequencies.values(), reverse=True))
        frequency_pattern[0] += joker_count
        return frequency_pattern


def load_file(filename: str, hand_class=Hand) -> list[Hand]:
    '''Loads the file as a list of hands'''
    hands = []
    with open(filename, "r") as f:
        lines = f.readlines()
        for l in lines:
            hands.append(hand_class.from_line(l))
    return hands


def one_star(filename: str) -> int:
    '''Returns the one star solution'''
    hands = load_file(filename)
    hands.sort()
    return sum([(i+1)*h.bid for i, h in enumerate(hands)])


def two_star(filename: str):
    '''Returns the two star solution'''
    hands = load_file(filename, hand_class=JokerHand)
    hands.sort()
    return sum([(i+1)*h.bid for i, h in enumerate(hands)])


if __name__ == "__main__":
    print(f"One star test solution is {one_star(TEST_FILE)}")
    print(f"Two star test solution is {two_star(TEST_FILE)}")
    print(f"One star solution is {one_star(INPUT_FILE)}")
    print(f"Two star solution is {two_star(INPUT_FILE)}")
