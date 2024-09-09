from day_12 import CaveMap
import pytest


@pytest.fixture
def cave_map():
    cave_map = CaveMap()
    cave_map.add_edge("start", "A")
    cave_map.add_edge("start", "b")
    cave_map.add_edge("A", "c")
    return cave_map


def test_small_caves_found(cave_map: CaveMap):
    assert cave_map.visit_once_max == {"b", "c", "start"}


def test_add_edge():
    caves = CaveMap()
    caves.add_edge("start", "A")
    assert dict(caves.connections) == {"start": {"A"}, "A": {"start"}}


def test_add_multiple_edges():
    caves = CaveMap()
    caves.add_edge("start", "A")
    caves.add_edge("start", "b")
    caves.add_edge("start", "b")
    assert dict(caves.connections) == {
        "start": {"A", "b"}, "A": {"start"}, "b": {"start"}}
