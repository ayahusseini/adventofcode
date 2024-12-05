import pytest
from day_5 import Page, RuleSet, TEST_FILE


def test_overlapping_rules():
    rs = RuleSet()
    p75 = Page('75')
    p47 = Page('47')
    p9 = Page('9')
    rs.add_rule(p75, p47)
    rs.add_rule(p75, p9)
    assert rs.pages['75'].next == {p47, p9}
