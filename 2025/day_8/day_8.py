"""Solution to advent of code day 8 2025"""
from ast import Tuple
from itertools import combinations
from turtle import distance

from _pytest.stash import T

INPUT_FILE = 'inputs/day_8_input.txt'
TEST_FILE = 'inputs/day_8_test_input.txt'


def load_file(filename: str) -> list[tuple[int]]:
    """Load the puzzle input, returning coordinates."""

    with open(filename, 'r') as f:
        return [tuple([int(num) for num in line.strip().split(',')]) for line in f if line.strip()]


class Box:
    def __init__(self, coord: tuple):
        self._validate_coordinate(coord)
        self.coord = coord

    def __repr__(self) -> str:
        return f'Box({self.coord})'

    def __str__(self) -> str:
        return f'{self.coord}'

    @staticmethod
    def _validate_coordinate(coord: tuple[int]):
        if not type(coord) == tuple:
            raise ValueError('Expecting a tuple')
        elif not all(type(t) == int for t in coord):
            raise ValueError('Expecting a tuple of integers')
        if len(coord) != 3:
            raise ValueError('Expecting coordinate')

    def __len__(self):
        return len(self.coord)


class DisjointSets:
    def __init__(self, nodes: list):
        """Initialises N separate components with integer labels 1, 2, ..., N."""
        self.reps = list(range(len(nodes)))
        self.nodes = nodes
        self.sizes = [1] * len(nodes)
        self.count = len(nodes)

    def union(self, p: int, q: int):
        """Merge components containing p and q.
        Add the smaller tree to the larger tree (to ensure they grow wider not taller)
        """

        p_parent = self.find(p)
        q_parent = self.find(q)

        # p belongs to the larger tree
        if self.sizes[p_parent] < self.sizes[q_parent]:
            p_parent, q_parent = q_parent, p_parent
            p, q = q, p

        if p_parent == q_parent:
            return

        self.reps[q_parent] = p_parent
        self.sizes[p_parent] += self.sizes[q_parent]
        self.count -= 1

    def find(self, query_node: int) -> int:
        """Find the ID of the representative component containing p.
        Roots are their own representatives."""
        if self.reps[query_node] == query_node:
            return query_node

        root = self.find(self.reps[query_node])
        self.reps[query_node] = root
        return root


def get_squared_distance(c1: tuple[int], c2: tuple[int]) -> int:
    """Return the squared distance between two coordinates."""
    return sum(((c1i - c2i)**2 for c1i, c2i in zip(c1, c2)))


def get_all_distances(all_boxes: list[Box]) -> list[int, int, int]:
    """Return all distances between boxes.
    Returned as a list of tuples (box_id_1, box_id_2, dist),
    The ID of a box is it's position in all_boxes (0,1,2,..., len(all_boxes) -1)
    """
    all_distances = []
    ids = list(range(0, len(all_boxes)))
    for b1, b2 in combinations(ids, 2):
        dist = get_squared_distance(all_boxes[b1].coord, all_boxes[b2].coord)
        all_distances.append((b1, b2, dist))
    return all_distances


def make_shortest_connections(boxes: list[Box], num_connections: int = 10) -> DisjointSets:
    """Create a DisjointSet object with num_connections of the shortest connections made.
    Return the last two boxes that will be connected """
    box_sets = DisjointSets(boxes)

    all_dists = sorted(get_all_distances(boxes),
                       key=lambda x: x[2], reverse=False)

    for _ in range(num_connections):
        b1, b2, _ = all_dists.pop(0)
        box_sets.union(b1, b2)
    return box_sets


def make_shortest_connections_until_one_set(boxes: list[Box]) -> Tuple:
    """Return a DisjointSet object with shortest connections made until there are only two components"""
    box_sets = DisjointSets(boxes)
    all_dists = sorted(get_all_distances(boxes),
                       key=lambda x: x[2], reverse=False)

    while box_sets.count > 1:
        b1, b2, _ = all_dists.pop(0)
        box_sets.union(b1, b2)
    return b1, b2


def get_n_largest(nums: list[int], n: int) -> list[int]:
    """Get the n largest sizes in a list"""
    return sorted(nums, reverse=True)[:n]


def multiply_all(nums: list[int]) -> int:
    """Multiply all numbers in a list"""
    prod = 1
    for n in nums:
        prod *= n
    return prod


def one_star(filename: str, nconnections: int):
    """Solve part 1 for day 8."""
    coords = load_file(filename)
    all_boxes = [Box(c) for c in coords]
    bs = make_shortest_connections(all_boxes, nconnections)
    largest_sizes = get_n_largest(bs.sizes, 3)
    return multiply_all(largest_sizes)


def two_star(filename: str):
    """Solve part 2 for day 8."""
    coords = load_file(filename)
    all_boxes = [Box(c) for c in coords]
    b1, b2 = make_shortest_connections_until_one_set(all_boxes)
    return (all_boxes[b1].coord[0] * all_boxes[b2].coord[0])


if __name__ == '__main__':

    print(f'One star test solution is {one_star(TEST_FILE, nconnections=10)}')
    print(f'Two star test solution is {two_star(TEST_FILE)}')
    print(f'One star solution is {one_star(INPUT_FILE, nconnections=1000)}')
    print(f'Two star solution is {two_star(INPUT_FILE)}')
