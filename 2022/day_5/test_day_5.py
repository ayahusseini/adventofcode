import pytest
from day_5 import CrateStack, TEST_FILE, load_file, Move


def test_load_crate():
    cratestack, moves = load_file(TEST_FILE)
    assert cratestack.stacks[1] == ["Z", "N"]
    assert cratestack.stacks[2] == ["M", "C", "D"]
    assert cratestack.stacks[3] == ["P"]
    assert moves[0].amount == 1
    assert moves[0].prev_stack == 2
    assert moves[0].new_stack == 1


@pytest.fixture
def cratestack():
    return load_file(TEST_FILE)[0]


def test_update(cratestack):
    move = Move(1, 2, 1)
    cratestack.update(move)
    assert cratestack.stacks[1] == ["Z", "N", "D"]
    assert cratestack.stacks[2] == ["M", "C"]
    assert cratestack.stacks[3] == ["P"]


def test_update_with_multiple_crates(cratestack):
    move1 = Move(1, 2, 1)
    cratestack.update(move1)
    move2 = Move(3, 1, 3)
    cratestack.update(move2)
    assert cratestack.stacks[1] == []
    assert cratestack.stacks[2] == ["M", "C"]
    assert cratestack.stacks[3] == ["P", "D", "N", "Z"]
