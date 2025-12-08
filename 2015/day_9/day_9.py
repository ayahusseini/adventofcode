"""Solution to advent of code day 9 2015"""

from collections import defaultdict

INPUT_FILE = "inputs/day_9_input.txt"
TEST_FILE = "inputs/day_9_test_input.txt"


class UndirectedGraph:
    def __init__(self):
        """Instantiate an empty undirected graph, with weighted edges."""

        self._nodes = set()
        self._node_neighbours = defaultdict(lambda: dict())

    def __len__(self) -> int:
        """Return the number of nodes"""

        return len(self._nodes)

    def add_node(self, node: str):
        """Add a node to the graph if it isn't already there."""

        if node not in self._nodes:
            self._nodes.update([node])
            self._node_neighbours[node] = {}

    def get_nodes(self):
        """Returns node iterator."""
        return iter(self._nodes)

    def add_edge(self, n1: str, n2: str, distance: int):
        """Adds an edge to the graph connecting nodes n1 and n2."""

        if n1 not in self._nodes or n2 not in self._nodes:
            raise ValueError(
                f"{n1} and {n2} must be in the graph before a connecting edge is added."
            )

        self._node_neighbours[n1][n2] = distance
        self._node_neighbours[n2][n1] = distance

    def get_node_neighbours(self, node: str) -> list[str]:
        """Return the neighbours of a node in a graph"""

        return [n for n in self._node_neighbours[node].keys()]

    def is_valid_edge(self, start: str, end: str) -> bool:
        """Returns True if an edge is valid."""

        return end in self._node_neighbours.get(start, dict()).keys()

    def is_valid_path(self, path: list[str], visit_each_node_once: bool = True):
        """Return True if a path (list of nodes) is valid."""

        valid_edges = all(
            self.is_valid_edge(path[i], path[i + 1]) for i in range(len(path) - 1)
        )
        if visit_each_node_once:
            valid_edges = valid_edges and all(v in self._nodes for v in path)
        return valid_edges

    def get_path_length(self, path: list[str]) -> int:
        """Return the path length."""

        if not self.is_valid_path(path):
            raise ValueError("Path is invalid")
        return sum(
            self._node_neighbours[path[i]][path[i + 1]] for i in range(len(path) - 1)
        )


def load_file(filename: str) -> UndirectedGraph:
    """Loads the file as a list of integers"""

    with open(filename, "r") as f:
        lines = f.readlines()

    graph = UndirectedGraph()

    for l in lines:
        l = l.replace("\n", "")
        words = l.split(" ")
        graph.add_node(words[0])
        graph.add_node(words[2])
        graph.add_edge(words[0], words[2], int(words[-1]))

    return graph


def get_shortest_path_from_start(
    graph: UndirectedGraph,
    start: str,
    visited: list = [],
    clear_visited: bool = False,
    edge_multiplier: int = 1,
) -> int:
    """Return the shortest path length that visits all other nodes starting from start.
    Set edge_multiplier to -1 to get the maximum path length instead."""

    if clear_visited:
        visited = []
    visited.append(start)

    nn = graph.get_node_neighbours(start)

    nn_not_visited = [i for i in nn if i not in visited]

    if len(visited) == len(graph):
        return graph.get_path_length(visited)

    curr_min = None

    for n in nn_not_visited:
        prev_visited = visited.copy()

        length_via_n = get_shortest_path_from_start(
            graph, n, visited, edge_multiplier=edge_multiplier
        )

        if curr_min is None:
            curr_min = length_via_n
        elif curr_min * edge_multiplier > length_via_n * edge_multiplier:
            curr_min = length_via_n
        visited = prev_visited

    return curr_min


def one_star(filename: str):
    """Returns the one star solution"""
    graph = load_file(filename)

    return min(
        get_shortest_path_from_start(graph, node, clear_visited=True)
        for node in graph.get_nodes()
    )


def two_star(filename: str):
    """Returns the two star solution"""
    graph = load_file(filename)

    return max(
        get_shortest_path_from_start(
            graph, node, clear_visited=True, edge_multiplier=-1
        )
        for node in graph.get_nodes()
    )


if __name__ == "__main__":
    print(f"One star solution is {one_star(TEST_FILE)}")
    print(f"Two star solution is {two_star(TEST_FILE)}")
    print(f"One star solution is {one_star(INPUT_FILE)}")
    print(f"Two star solution is {two_star(INPUT_FILE)}")
