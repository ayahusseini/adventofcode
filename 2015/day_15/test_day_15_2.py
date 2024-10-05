import pytest 
from day_15_2 import shuffle_proportions

@pytest.fixture 
def example_proportions():
    return [50,50]

def test_shuffle_proportions(example_proportions):
    '''Tests shuffle proportions'''
    assert shuffle_proportions(1,0,example_proportions) == [[49,51]]
    assert shuffle_proportions(1,1,example_proportions) == [[51,49]]

def test_shuffle_proportions_multiple_units(example_proportions):
    '''Tests shuffle proportions'''
    assert shuffle_proportions(10,0,example_proportions) == [[40,60]]

def test_shuffle_proportions_with_max_condition_met(example_proportions):
    '''Tests shuffle proportions'''
    assert shuffle_proportions(50,0,example_proportions) == [[0,100]]

def test_shuffle_proportions_with_max_condition_exceeded(example_proportions):
    '''Tests shuffle proportions'''
    assert shuffle_proportions(52,0,example_proportions) == []
