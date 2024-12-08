"""Solution to advent of code day 8 2023"""

INPUT_FILE = "inputs/day_8_input.txt"
TEST_FILE = "inputs/day_8_test_input.txt"


class Node:
    """Binary Tree Node."""

    def __init__(self, name: str,  left=None, right=None):
        """Instantiates the node."""
        self.name = name
        self.left = left
        self.right = right


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

    nodes = {'AAA': Node(name='AAA')}
    for l in lines:
        l = l.replace("\n", "").strip()
        if not l:
            continue
        elif '=' in l:
            curr, children = l.split(' = ')
            left, right = children[1:-1].split(', ')
            for name in (curr, left, right):
                if not name in nodes.keys():
                    nodes[name] = Node(name)

            nodes[curr].left = nodes[left]
            nodes[curr].right = nodes[right]
        else:
            instructions = l
    return instructions, nodes


def follow_instructions(instructions: str, root: Node, target: Node):
    count = 0
    for i in get_next_step(instructions):
        count += 1
        if i == 'L':
            root = root.left
        elif i == 'R':
            root = root.right
        if root == target:
            return count


def one_star(filename: str):
    """Returns the one star solution"""
    seq, nodes = load_file(filename)
    root = nodes['AAA']
    target = nodes['ZZZ']
    return follow_instructions(seq, root, target)


def two_star(filename: str):
    """Returns the two star solution"""

    return


if __name__ == "__main__":
    print(f"One star test solution is {one_star(TEST_FILE)}")
    print(f"Two star test solution is {two_star(TEST_FILE)}")
    print(f"One star solution is {one_star(INPUT_FILE)}")
    print(f"Two star solution is {two_star(INPUT_FILE)}")
