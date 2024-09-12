'''Solution to advent of code day 7 2015

Each WIRE
- Has an identifier (lowercase str)
- Carries a 16 bit SIGNAL (number from 0 to 65535)
- Can give its signal to multiple WIREs 

SIGNAL is given to each WIRE via one of three sources:
- GATE
- Another WIRE
- Some specific value 

GATE 
- Can give a signal after all of its imputs have a signal
'''

INPUT_FILE = "inputs/day_7_input.txt"
TEST_FILE = "inputs/day_7_test_input.txt"

GATES = ["AND", "OR", "LSHIFT", "RSHIFT", "NOT"]


def load_file(filename: str, possible_gates: list[str] = GATES) -> list[int]:
    '''Loads the file as a list of integers'''

    with open(filename, "r") as f:
        lines = f.readlines()

    return [process_line(l.replace("\n", "").strip(), possible_gates) for l in lines]


def filter_lines(lines: list[dict], target: str = "a") -> list[dict]:
    '''Filter the lines, such that only the components needed to find the target
    are included"'''
    to_define = []
    defined = []

    set_target = list(filter(lambda x: x["target"] == target, lines))[0]
    ordered_lines = [set_target]

    for wire in set_target["inputs"]:
        if wire.isalpha():
            to_define.append(wire)

    while to_define:

        for i in to_define:

            set_target = list(filter(lambda x: x["target"] == i, lines))[0]

            ordered_lines.append(set_target)

            for wire in set_target["inputs"]:
                if wire.isalpha() and wire not in defined:
                    to_define.append(wire)
            to_define.pop(0)
            defined.append(i)

    return ordered_lines[::-1]


def get_gate_from_line(line: str,
                       possible_gates: list[str]) -> str:
    '''Extract the gate from a line. Return "SET" if no gate.'''
    for gate in possible_gates:
        if gate in line:
            return gate
    return "SET"


def get_wires_from_line(line: str, to_exclude: list[str]) -> list[str]:
    '''Return the wires in a line of text.'''
    for word in to_exclude:
        line = line.replace(word, "").strip()
    wires = [word.strip() for word in line.split(" ") if word.strip()]
    return wires


def process_line(line: str, possible_gates: list[str]) -> dict:
    '''Get a dictionary containing 
    - a list of sources being fed into the wires
    - the target 
    - The gate ("SET" is used to represent a signal being sent into a wire without a gate)
    '''
    gate = get_gate_from_line(line, possible_gates)
    inputs, output = tuple(line.split(" -> "))

    input_wires = get_wires_from_line(inputs, possible_gates)

    return {
        "inputs": input_wires,
        "target": output.strip(),
        "gate": gate
    }


def get_numeric_inputs(curr_values: dict, inputs: list[str]) -> list[int]:
    '''Return a list of numeric values representing the signals.'''
    vals = []
    for val in inputs:
        if val.isalpha():
            vals.append(curr_values[val])
        else:
            vals.append(int(val))
    return vals


def add_wire_to_dictionary(wire: str, wire_to_signal: dict):
    '''Adds a wire to the wire_to_signal dictionary if not already there.'''
    if wire not in wire_to_signal.keys():
        wire_to_signal[wire] = 0
    return wire_to_signal


def get_command_map() -> dict:
    return {
        "AND": get_and,
        "OR": get_or,
        "NOT": get_complement,
        "LSHIFT": get_left_shift,
        "RSHIFT": get_right_shift
    }


def execute_command(command: dict, wire_to_signal: dict, command_map: dict) -> dict:
    '''Executes a command and returns a new wire_to_signal dictionary'''
    inputs = command["inputs"]
    output = command["target"]

    input_signals = get_numeric_inputs(wire_to_signal, inputs)

    if 0 in input_signals:
        return None

    if command["gate"] == "SET":
        output_val = input_signals[0]
    else:
        output_val = command_map[command["gate"]](*input_signals)

    wire_to_signal[output] = output_val
    return wire_to_signal


def get_and(signal1: int, signal2: int) -> int:
    '''Return the bitwise and'''
    return signal1 & signal2


def get_left_shift(signal1: int, signal2: int) -> int:
    '''Left shift signal 1 by signal 2'''
    return signal1 << signal2


def get_complement(signal1: int) -> int:
    '''Return the bitwise complement'''
    return 65536 + ~ signal1


def get_right_shift(signal1: int, signal2: int) -> int:
    '''Return signal1 shifted to the right by signal 2'''
    return signal1 >> signal2


def get_or(signal1: int, signal2: int) -> int:
    '''Return the bitwise or of signal1 and signal2'''
    return signal1 | signal2


def one_star(filename: str):
    '''Returns the one star solution'''
    lines = load_file(filename)
    wire_signal_values = {"a": 0}
    evaluated = [False]*len(lines)
    command_map = get_command_map()

    lines = sorted(
        lines, key=lambda x: x["gate"] == "SET" and x["inputs"][0].isnumeric())
    while wire_signal_values["a"] == 0:

        for i, command in enumerate(lines):
            if evaluated[i]:
                continue
            for w in [*command["inputs"], command["target"]]:
                if w.isalpha():
                    add_wire_to_dictionary(w, wire_signal_values)

            if execute_command(command, wire_signal_values, command_map):
                wire_signal_values = execute_command(
                    command, wire_signal_values, command_map)
                evaluated[i] = True
        print(sum(evaluated))

    return wire_signal_values


def two_star(filename: str):
    '''Returns the two star solution'''

    return


if __name__ == "__main__":
    # print(f"One star solution is {one_star(TEST_FILE)}")
    print(f"Two star solution is {two_star(TEST_FILE)}")
    print(f"One star solution is {one_star(INPUT_FILE)}")
    print(f"Two star solution is {two_star(INPUT_FILE)}")
