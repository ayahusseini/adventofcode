"""Solution to advent of code day 4 2023"""

INPUT_FILE = 'inputs/day_4_input.txt'
TEST_FILE = 'inputs/day_4_test_input.txt'


class Card:
	def __init__(self, card_num: int, winning_nums: list[int], nums: list[int]):
		self.card_num = card_num
		self.winning = winning_nums
		self.nums = nums

	def get_wins(self) -> int:
		"""Return a list of nums that are winning"""
		return list(set(self.nums) - (set(self.nums) - set(self.winning)))

	def get_points(self) -> int:
		num_wins = len(self.get_wins())
		if not num_wins:
			return 0
		return 2 ** (num_wins - 1)

	@classmethod
	def from_line(cls, line: str):
		"""Instantiate a card from a line"""

		card = int(line.split(':')[0].split(' ')[-1])

		winning, actual = line.split(':')[1].strip().split('|')

		winning = [int(w.strip()) for w in winning.strip().split(' ') if w]

		actual = [int(a.strip()) for a in actual.strip().split(' ') if a]
		return cls(card, winning, actual)


class Pile:
	def __init__(self, cards: list[Card]):
		"""Instantiates a pile of scratchcards"""
		self.cards = cards
		self.copies = {c.card_num: 1 for c in cards}

	def process_card(self, card: Card):
		num_wins = len(card.get_wins())
		num_copies = self.copies[card.card_num]
		for i in range(1, num_wins + 1):
			self.copies[card.card_num + i] += num_copies

	def process_cards(self):
		for c in self.cards:
			self.process_card(c)

	def count_scratchcards(self):
		return sum(self.copies.values())


def load_file(filename: str) -> list[str]:
	"""Loads the file as a list of integers"""

	with open(filename, 'r') as f:
		lines = f.readlines()

	return [l.replace('\n', '') for l in lines]


def one_star(filename: str):
	"""Returns the one star solution"""

	lines = load_file(filename)
	cards = [Card.from_line(l) for l in lines]
	return sum([c.get_points() for c in cards])


def two_star(filename: str):
	"""Returns the two star solution"""
	lines = load_file(filename)
	original_cards = [Card.from_line(l) for l in lines]
	pile = Pile(original_cards)
	pile.process_cards()
	return pile.count_scratchcards()


if __name__ == '__main__':
	print(f'One star test solution is {one_star(TEST_FILE)}')
	print(f'Two star test solution is {two_star(TEST_FILE)}')
	print(f'One star solution is {one_star(INPUT_FILE)}')
	print(f'Two star solution is {two_star(INPUT_FILE)}')
