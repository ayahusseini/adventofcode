from day_13 import map_relations, load_file, TEST_FILE, get_relation, get_all_cycles
import pytest


@pytest.fixture
def test_file():
    return load_file(TEST_FILE)


def test_mapping(test_file):
    map, _ = map_relations(test_file)
    assert map[("Alice", "David")] == 44


def test_get_relation(test_file):
    map, _ = map_relations(test_file)
    assert get_relation("Bob", "Alice", map) == 83 + 54


def test_get_all_cycles():
    assert get_all_cycles(["A", "B"]) == [["A", "B", "A"]]


def test_get_all_cycles2():
    assert get_all_cycles(["A", "B", "C"]) == [
        ["A", "B", "C", "A"],
        ["A", "C", "B", "A"],
    ]
