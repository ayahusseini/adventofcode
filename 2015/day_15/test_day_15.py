import pytest 
from day_15 import shuffle_proportions, step_up_params, step_up_params_with_constraint

@pytest.fixture 
def example_proportions():
    return [50,50]

@pytest.fixture
def example_scorer():
    def product(p): 
        t = 1
        for i in p:
            t *= i 
        return t
    return product


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

def test_step_up_params(example_scorer, example_proportions):
    assert step_up_params(example_proportions, example_scorer, 500000) == []

def test_step_up_params_with_results(example_scorer, example_proportions):
    assert step_up_params(example_proportions, example_scorer, 0) == [[49,51],[51,49]]

def test_step_up_params_with_constraint(example_scorer, example_proportions):
    constraint = lambda p: all(x != 49 for x in p)
    assert step_up_params_with_constraint(example_proportions,example_scorer,0,constraint) == [[48,52],[52,48]]
