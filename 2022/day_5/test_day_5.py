import pytest
from day_5 import CrateStack, TEST_FILE, load_file, Move


def test_load_crate():
    cratestack, moves = load_file(TEST_FILE)
    assert cratestack.stacks[1] == ['Z', 'N']
    assert cratestack.stacks[2] == ['M', 'C', 'D']
    assert cratestack.stacks[3] == ['P']
    assert moves[0].amount == 1
    assert moves[0].prev_stack == 2
    assert moves[0].new_stack == 1
