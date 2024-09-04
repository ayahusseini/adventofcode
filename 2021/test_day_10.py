import pytest

from day_10 import find_incorrect_bracket, get_autocomplete_score, find_middle


@pytest.fixture
def lines():
    return ['[({(<(())[]>[[{[]{<()<>>',
            '[(()[<>])]({[<{<<[]>>(',
            '{([(<{}[<>[]}>{[]{[(<()>',
            '(((({<>}<{<{<>}{[]{[]{}',
            '[[<[([]))<([[{}[[()]]]',
            '[{[{({}]{}}([{[{{{}}([]',
            '{<[[]]>}<{[{[{[]{()[[[]',
            '[<(<(<(<{}))><([]([]()',
            '<{([([[(<>()){}]>(<<{{',
            '<{([{{}}[<[[[<>{}]]]>[]]']


@pytest.mark.parametrize("line, res", [
    ("(]", ']'),
    ("{()()()>", '>'),
    ("(((()))}", '}'),
    ("<([]){()}[{}])", ')'),
    ("{([(<{}[<>[]}>{[]{[(<()>", "}"),
    ("[[<[([]))<([[{}[[()]]]", ")"),
    ("[{[{({}]{}}([{[{{{}}([]", "]"),
    ('[]', None)
])
def test_find_wrong_brack(line, res):
    assert find_incorrect_bracket(line) == res


@pytest.mark.parametrize("line, res", [
    ("[({(<(())[]>[[{[]{<()<>>", "}}]])})]"),
    ("[(()[<>])]({[<{<<[]>>(", ")}>]})"),
    ("(((({<>}<{<{<>}{[]{[]{}", "}}>}>))))"),
    ("", "")
])
def test_find_autocomplete(line, res):
    assert find_incorrect_bracket(line, return_autocomplete=True) == [
        r for r in res]


@pytest.mark.parametrize("line, res", [
    ("}}]])})]", 288957),
    (")}>]})", 5566),
    ("}}>}>))))", 1480781),
    ("", 0)
])
def test_find_autocomplete_score(line, res):
    assert get_autocomplete_score([l for l in line]) == res


def test_find_middle():
    assert find_middle([1, 2, 3]) == 2


def test_find_middle_empty():
    assert find_middle([]) == None


def test_find_middle_unsorted():
    assert find_middle([3, 1, 2]) == 2
