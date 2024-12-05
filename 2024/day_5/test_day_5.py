import pytest
from day_5 import Page, RuleSet, TEST_FILE


@pytest.fixture
def rs():
    rules = RuleSet()
    rules.add_rule(7, 5)
    rules.add_rule(7, 47)
    rules.add_rule(5, 47)
    return rules


def test_pages_added(rs):
    assert rs.pages.keys() == {7, 5, 47}
    assert rs[47].next == set()
    assert rs[7].next == {rs[5], rs[47]}
    assert rs[5].next == {rs[47]}
