from day_12 import sum_numbers_in_string, filter_red_from_list
import json


def test_sum1():
    assert sum_numbers_in_string("""[{"e": [[{"e": 86, """) == 86


def test_sum2():
    assert sum_numbers_in_string("""{"a":2,"b":4}""") == 6


def test_sum3():
    assert sum_numbers_in_string("""{"a":[-1,2]}""") == 1


def test_filter1():
    assert filter_red_from_list([1, {"c": "red", "b": 2}, 3]) == [1, dict(), 3]


def test_filter_nested():
    assert filter_red_from_list([[1, {"c": "red", "b": 2}, 3]]) == [[1, dict(), 3]]


def test_filter_nested_dicts():
    assert filter_red_from_list([1, {2: 3, 4: {5: "red"}}]) == [1, {2: 3, 4: dict()}]


def test_filter_nested_dicts_and_lists():
    assert filter_red_from_list(
        [1, {2: 3, 4: {5: "red"}}, {6: [1, 2, 3]}, {7: [1, "red"], 8: {1: "red"}}]
    ) == [1, {2: 3, 4: dict()}, {6: [1, 2, 3]}, {7: [1, "red"], 8: dict()}]


def test_get_correct_filtered_sum():
    s = json.dumps(filter_red_from_list([{"d": "red", "e": [1, 2, 3, 4], "f": 5}]))
    print(s)
    print(filter_red_from_list([{"d": "red", "e": [1, 2, 3, 4], "f": 5}]))
    assert sum_numbers_in_string(s) == 0


def test_get_correct_filtered_sum2():
    s = json.dumps(
        filter_red_from_list(
            [{"d": "red", "e": [1, 2, 3, 4], "f": 5}, [1, {"c": "red", "b": 2}, 3]]
        )
    )
    assert sum_numbers_in_string(s) == 4
