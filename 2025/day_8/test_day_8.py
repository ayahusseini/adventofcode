import pytest

from day_8 import load_file, DisjointSets


@pytest.fixture
def mock_ds() -> DisjointSets:
    """Mock disjoint set object"""
    return DisjointSets(['a', 'b', 'c'])


@pytest.fixture
def mock_ds_joined_sets() -> DisjointSets:
    """Mock disjoint set object with grouped components [0,2,3], [1,10,7,6] and all else separate"""
    ds = DisjointSets([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    ds.union(0, 2)
    ds.union(2, 3)
    ds.union(1, 10)
    ds.union(1, 7)
    ds.union(1, 6)
    return ds


def test_union_in_correct_direction(mock_ds_joined_sets):
    mock_ds_joined_sets.union(0, 1)
    assert mock_ds_joined_sets.find(0) == 1


def test_union_in_correct_direction_with_inputs_reversed(mock_ds_joined_sets):
    mock_ds_joined_sets.union(1, 0)
    assert mock_ds_joined_sets.find(0) == 1


def test_ds_find_self_root(mock_ds):
    assert mock_ds.find(1) == 1
    assert mock_ds.find(2) == 2
    assert mock_ds.find(0) == 0


def test_ds_union_works_once(mock_ds):
    mock_ds.union(1, 2)
    assert mock_ds.find(1) == mock_ds.find(2)


def test_ds_union_works_twice(mock_ds):
    mock_ds.union(1, 2)
    mock_ds.union(0, 2)
    assert mock_ds.find(1) == mock_ds.find(2)
    assert mock_ds.find(1) == mock_ds.find(0)
    assert mock_ds.find(0) == mock_ds.find(2)
