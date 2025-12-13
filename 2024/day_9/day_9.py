"""Solution to advent of code day 9 2024"""

INPUT_FILE = 'inputs/day_9_input.txt'
TEST_FILE = 'inputs/day_9_test_input.txt'


class Files:
	def __init__(self, disk_space: dict):
		"""Instantiates a list of files."""

		self.disk = disk_space
		self.num_filled = len(disk_space)

	def get_file_quantities(self) -> dict:
		"""Maps a file id to the number of blocks it occupies."""

		return {f: list(self.disk.values()).count(f) for f in set(self.disk.values())}

	def get_first_index(self) -> dict:
		"""Maps a file id to the first index it appears in."""

		first_idx = dict()
		for idx, file_id in sorted(self.disk.items(), key=lambda x: x[0], reverse=False):
			if file_id in first_idx:
				continue
			first_idx[file_id] = idx
		return first_idx

	@classmethod
	def from_line(cls, line: str):
		"""Instantiates the files from a line of text."""

		disk = dict()

		write_to = 0

		for id, i in enumerate(range(0, len(line), 2)):
			batch = line[i : i + 2]
			batch = batch + '0' if len(batch) < 2 else batch

			num_blocks = int(batch[0])
			gap = int(batch[1])

			for pointer in range(write_to, write_to + num_blocks):
				disk[pointer] = id

			write_to += num_blocks + gap

		return cls(disk)

	def swap(self, l_idx: int, r_idx: int) -> None:
		"""Swaps two disk items."""

		if l_idx in self.disk.keys() and r_idx in self.disk.keys():
			self.disk[l_idx], self.disk[r_idx] = self.disk[r_idx], self.disk[l_idx]

		elif r_idx in self.disk.keys():
			self.disk[l_idx] = self.disk[r_idx]
			del self.disk[r_idx]

		elif l_idx in self.disk.keys():
			self.disk[r_idx] = self.disk[l_idx]
			del self.disk[l_idx]

	def count_gaps(self) -> int:
		"""Counts the number of gaps."""

		return max(self.disk.keys()) - self.num_filled + 1

	def fill_blocks(self) -> None:
		"""Moves the blocks from right to left such that there are no more gaps."""

		l = 0
		r = max(self.disk.keys())

		while l <= r:
			if l in self.disk.keys():
				l += 1
			elif r not in self.disk.keys():
				r -= 1
			else:
				self.swap(l, r)
				l += 1
				r -= 1

	def leftmost_gap(self, ridx: int, minsize: int):
		"""Finds consecutive gap indeces to the left of ridx"""

		g_start = 0
		g_end = 0

		while g_start < ridx:
			if g_start in self.disk.keys():
				g_start += 1
				g_end = g_start
				continue

			while g_end not in self.disk.keys() and g_end < ridx:
				if (g_end - g_start) + 1 >= minsize:
					yield range(g_start, g_end + 1)

				g_end += 1

			g_start += 1
			g_end = g_start

	def fill_files(self) -> None:
		"""Moves the files in batches from right to left in order of decreasing file id."""

		quantities = self.get_file_quantities()
		first_idx = self.get_first_index()

		file_id = max(self.disk.values())

		while file_id >= 0:
			filesize = quantities[file_id]
			fileidx = first_idx[file_id]
			gap = next(self.leftmost_gap(fileidx, filesize), None)

			if gap is None:
				file_id -= 1
				continue
			for gidx, fidx in zip(gap, range(fileidx, fileidx + filesize)):
				self.swap(gidx, fidx)

			file_id -= 1

	def checksum(self) -> int:
		"""Returns the checksum."""
		return sum([idx * int(id) for idx, id in self.disk.items()])

	def __str__(self) -> str:
		"""String representation."""
		text = ['.' for _ in range(max(self.disk.keys()) + 1)]
		for idx, file_id in self.disk.items():
			text[idx] = str(file_id)
		return ''.join(text)


def load_file(filename: str) -> str:
	"""Loads the file as a string"""
	with open(filename, 'r') as f:
		line = f.readline().strip()
	return line


def one_star(filename: str):
	"""Returns the one star solition"""
	files = Files.from_line(load_file(filename))

	files.fill_blocks()

	return files.checksum()


def two_star(filename: str):
	"""Returns the two star solution"""
	files = Files.from_line(load_file(filename))
	files.fill_files()

	return files.checksum()


if __name__ == '__main__':
	print(f'One star test solution is {one_star(TEST_FILE)}')
	print(f'Two star test solution is {two_star(TEST_FILE)}')
	print(f'One star solution is {one_star(INPUT_FILE)}')
	print(f'Two star solution is {two_star(INPUT_FILE)}')
