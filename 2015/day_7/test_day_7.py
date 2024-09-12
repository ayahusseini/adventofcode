import pytest

from day_7 import get_numeric_inputs, get_gate_from_line, get_wires_from_line, process_line, add_wire_to_dictionary, execute_command, get_and, get_left_shift, get_complement, get_or, filter_lines


def test_filter_two_lines():
    lines = [
        {"inputs": ["x"],
         "target": "y",
         "gate": "OR"},
        {"inputs": ["123"],
         "target": "x",
         "gate": "SET"}]
    assert all(l in filter_lines(lines, target="y") for l in lines)


def test_filter_two_lines_filters_out():
    lines = [
        {"inputs": ["x"],
         "target": "y",
         "gate": "OR"},
        {"inputs": ["123"],
         "target": "x",
         "gate": "SET"}]
    assert lines[1] in filter_lines(lines, target="x")


def test_filter_two_lines_filters_out_2():
    lines = [
        {"inputs": ["x"],
         "target": "y",
         "gate": "OR"},
        {"inputs": ["123"],
         "target": "x",
         "gate": "SET"}]
    assert len(filter_lines(lines, target="x")) == 1


def test_filter_three_lines():
    lines = [
        {"inputs": ["x", "y"],
         "target": "z",
         "gate": "AND"},
        {"inputs": ["123"],
         "target": "x",
         "gate": "SET"},
        {"inputs": ["x"],
         "target": "y",
         "gate": "SET"}]
    assert all(l in filter_lines(lines, target="z")
               for l in [lines[1], lines[2], lines[0]])


def test_filter_three_lines_2():
    lines = [
        {"inputs": ["x", "y"],
         "target": "z",
         "gate": "AND"},
        {"inputs": ["123"],
         "target": "x",
         "gate": "SET"},
        {"inputs": ["x"],
         "target": "y",
         "gate": "SET"}]
    assert len(filter_lines(lines, target="z")) == 3


def test_filter_three_lines_3():
    lines = [
        {"inputs": ["x", "y"],
         "target": "z",
         "gate": "AND"},
        {"inputs": ["123"],
         "target": "x",
         "gate": "SET"},
        {"inputs": ["x"],
         "target": "y",
         "gate": "SET"}]
    assert len(filter_lines(lines, target="y")) == 2


def test_execute_command():
    command_map = {}
    command = {
        "inputs": ["123"],
        "target": "x",
        "gate": "SET"
    }
    assert execute_command(command, {}, command_map) == {"x": 123}


def test_execute_command_and():
    command_map = {"AND": get_and}
    wire_vals = {"x": 123, "y": 456}
    command = {
        "inputs": ["x", "y"],
        "target": "d",
        "gate": "AND"
    }
    assert execute_command(command, wire_vals, command_map) == {
        "x": 123, "y": 456, "d": 72}


def test_execute_command_lshift():
    command_map = {"LSHIFT": get_left_shift}
    wire_vals = {"x": 123, "y": 456}
    command = {
        "inputs": ["x", "2"],
        "target": "f",
        "gate": "LSHIFT"
    }
    assert execute_command(command, wire_vals, command_map) == {
        "x": 123, "y": 456, "f": 492}


def test_execute_command_not():
    command_map = {"NOT": get_complement}
    wire_vals = {"x": 123}
    command = {
        "inputs": ["x"],
        "target": "h",
        "gate": "NOT"
    }
    assert execute_command(command, wire_vals, command_map) == {
        "x": 123, "h": 65412}


def test_execute_command_gate_not_supplied_with_signals():
    command_map = {"OR": get_or}
    wire_vals = {"x": 1000, "y": 0}
    command = {
        "inputs": ["x", "y"],
        "target": "d",
        "gate": "OR"
    }
    assert execute_command(command, wire_vals, command_map) == {
        "x": 1000, "y": 0, "d": 0}


def test_add_wire():
    assert add_wire_to_dictionary("a", {"b": 2}) == {"a": 0, "b": 2}


def test_add_wire_if_already_there():
    assert add_wire_to_dictionary("a", {"a": 1}) == {"a": 1}


@pytest.mark.parametrize(
    "line,expected",
    [
        ("123 -> x", "SET"),
        ("x OR y -> e", "OR"),
        ("x LSHIFT 2 -> f", "LSHIFT"),
        ("NOT lk -> ll", "NOT"),
        ("", "SET")

    ]
)
def test_get_gate(line, expected):
    assert get_gate_from_line(
        line, ["AND", "OR", "LSHIFT", "RSHIFT", "NOT"]) == expected


@pytest.mark.parametrize(
    "line,expected",
    [
        ("123 ", ["123"]),
        ("x OR y", ["x", "y"]),
        ("x LSHIFT 2", ["x", "2"]),
        ("NOT lk", ["lk"]),
        ("", [])

    ]
)
def test_get_wires_input(line, expected):
    assert get_wires_from_line(
        line, ["AND", "OR", "LSHIFT", "RSHIFT", "NOT"]) == expected


@pytest.mark.parametrize(
    "curr_wires,inputs,expected",
    [
        ({"a": 1}, ["a"], [1]),
        ({"b": 1, "a": -1}, ["a", "b"], [-1, 1]),
        ({}, ["123", "456"], [123, 456]),
        ({"a": 0, "b": 1}, ["123", "456"], [123, 456]),
        ({"a": 1, "b": 2}, ["123", "b"], [123, 2])

    ]
)
def test_get_numeric_inputs(curr_wires, inputs, expected):
    assert get_numeric_inputs(curr_wires, inputs) == expected


def test_process_line():
    assert process_line("p LSHIFT 2 -> q", ["AND", "OR", "LSHIFT", "RSHIFT", "NOT"]) == {"inputs": ["p", "2"],
                                                                                         "target": "q",
                                                                                         "gate": "LSHIFT"}


def test_process_line_2():
    assert process_line("123 -> x", ["AND", "OR", "LSHIFT", "RSHIFT", "NOT"]) == {"inputs": ["123"],
                                                                                  "target": "x",
                                                                                  "gate": "SET"}
