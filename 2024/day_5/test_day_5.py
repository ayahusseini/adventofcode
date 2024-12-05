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
    assert set(7, 5, 47) in rs.pages
    assert rs[47].next == set()
