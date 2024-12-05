import pytest
from day_5 import Page, RuleSet, TEST_FILE


@pytest.fixture
def rs():
    rules = RuleSet()
    rules.add_rule(Page('75'), Page('47'))
    rules.add_rule(Page('75'), Page('9'))
    return rules


def test_overlapping_rules(rs):
    assert rs.pages['75'].next == {rs.pages['47'], rs.pages['9']}


def test_sorting(rs):
    assert rs.is_sorted(['75', '47', '9'])
