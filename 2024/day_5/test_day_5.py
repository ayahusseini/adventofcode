import pytest
from day_5 import load_file, RuleSet, TEST_FILE, INPUT_FILE


@pytest.fixture
def rs():
    rules = RuleSet()
    rules.add_rule(7, 5)
    rules.add_rule(7, 47)
    rules.add_rule(5, 47)
    return rules


@pytest.fixture
def example_rules_and_orders():
    return load_file(TEST_FILE)


@pytest.fixture
def example_rules_and_orders_large():
    return load_file(INPUT_FILE)


def test_correct_ordering(example_rules_and_orders_large):
    rules, orders = example_rules_and_orders_large
    correct_order = orders[0]
    assert rules[57] in rules[75].next
    assert rules[28] in rules[57].next
    assert rules[17] in rules[28].next
    assert rules[96] in rules[17].next
    assert rules.is_sorted(correct_order)


def test_correct_orders_found(example_rules_and_orders):
    rules, orders = example_rules_and_orders
    for i in (0, 1, 2):
        assert rules.is_sorted(orders[i])
    for i in (3, 4, 5):
        assert not rules.is_sorted(orders[i])


def test_pages_added(rs):
    assert rs.pages.keys() == {7, 5, 47}
    assert rs[47].next == set()
    assert rs[7].next == {rs[5], rs[47]}
    assert rs[5].next == {rs[47]}


def test_is_sorted(rs):
    rs.add_rule(43, 7)
    assert rs.is_sorted([43, 7, 5, 47])
    assert rs.is_sorted([43, 7, 5])
