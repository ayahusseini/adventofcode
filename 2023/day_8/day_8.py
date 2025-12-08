"""Solution to advent of code day 8 2023"""

from collections import defaultdict

INPUT_FILE = "inputs/day_8_input.txt"
TEST_FILE = "inputs/day_8_test_input.txt"
TEST_FILE_2 = "inputs/day_8_test_input_2.txt"


class Node:
    """Binary Tree Node."""

    def __init__(self, name: str, left=None, right=None):
        """Instantiates the node."""
        self.name = name
        self.left = left
        self.right = right
        self.cache = defaultdict(lambda: dict())

    def traverse(self, seq: str, stop_condition):
        count = 0
        root = self
        for step in get_next_step(seq):
            root = self.left if step == "L" else self.right
            self.cache[seq][count] = root
            count += 1
            yield stop_condition(root)


def get_next_step(steps: str):
    """Generates the next step in the sequence."""
    i = 0
    while True:
        yield steps[i]
        i += 1
        if i == len(steps):
            i = 0


def load_file(filename: str) -> tuple[str, dict]:
    """Loads the file as a sequence of instructions and a dictionary of nodes"""
    with open(filename, "r") as f:
        lines = f.readlines()
    nodes = defaultdict(lambda: Node(name=None))
    for l in lines:
        l = l.strip()
        if not l:
            continue
        elif "=" in l:
            curr, children = l.split(" = ")
            left, right = children[1:-1].split(", ")
            nodes[curr].name = curr
            nodes[left].name = left
            nodes[right].name = right
            nodes[curr].left = nodes[left]
            nodes[curr].right = nodes[right]
        else:
            instructions = l
    return instructions, nodes


def follow_instructions(instructions: str, root: list[Node], stop_condition):
    """Follow the instructions for a list of starting roots."""
    count = 0
    for i in get_next_step(instructions):
        count += 1
        root = [r.left if i == "L" else r.right for r in roots]
        if stop_condition(roots):
            return count


def one_star(filename: str):
    """Returns the one star solution"""
    seq, nodes = load_file(filename)
    root = nodes["AAA"]
    target = nodes["ZZZ"]
    return root.traverse(seq, stop_condition=lambda x: x == [target])


def all_nodes_end_on_z(nodes: list[Node], cache: dict = dict()) -> bool:
    """Returns True if all node names end with a 'Z'"""
    return all(n.name[-1] == "Z" for n in nodes)


def two_star(filename: str):
    """Returns the two star solution"""
    seq, nodes = load_file(filename)
    roots = [node for node in nodes.values() if node.name[-1] == "A"]
    return follow_instructions(seq, roots, stop_condition=all_nodes_end_on_z)


if __name__ == "__main__":
    print(f"One star test solution is {one_star(TEST_FILE)}")
    print(f"Two star test solution is {two_star(TEST_FILE_2)}")
    print(f"One star solution is {one_star(INPUT_FILE)}")
    print(f"Two star solution is {two_star(INPUT_FILE)}")
