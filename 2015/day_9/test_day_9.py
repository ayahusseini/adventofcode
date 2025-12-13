import pytest
from day_9 import UndirectedGraph, get_shortest_path_from_start


@pytest.fixture
def graph():
	graph = UndirectedGraph()
	graph.add_node('L')
	graph.add_node('D')
	graph.add_node('B')
	graph.add_edge('L', 'D', 464)
	graph.add_edge('L', 'B', 518)
	graph.add_edge('D', 'B', 141)
	return graph


def test_get_shortest_path_from_node(graph):
	assert get_shortest_path_from_start(graph, 'D', clear_visited=True) == 659


def test_get_longest_path_from_node(graph):
	assert get_shortest_path_from_start(graph, 'D', clear_visited=True, edge_multiplier=-1) == 982


def test_get_longest_path_from_node2(graph):
	assert get_shortest_path_from_start(graph, 'L', clear_visited=True, edge_multiplier=-1) == 659


def test_get_longest_path_from_node3(graph):
	assert get_shortest_path_from_start(graph, 'B', clear_visited=True, edge_multiplier=-1) == 982


def test_get_shortest_path_from_node2(graph):
	assert get_shortest_path_from_start(graph, 'L', clear_visited=True) == 605


def test_get_shortest_path_from_node3(graph):
	assert get_shortest_path_from_start(graph, 'B', clear_visited=True) == 605


def test_neighbours(graph):
	assert set(graph.get_node_neighbours('L')) == {'D', 'B'}


def test_valid_path(graph):
	assert graph.is_valid_path(['L', 'D'], visit_each_node_once=False)


def test_valid_path_complete(graph):
	assert graph.is_valid_path(['D', 'L', 'B'], visit_each_node_once=True)


def test_get_path_distance(graph):
	assert graph.get_path_length(['L', 'D']) == 464


def test_get_path_distance2(graph):
	assert graph.get_path_length(['L', 'D', 'L', 'B']) == 464 * 2 + 518
