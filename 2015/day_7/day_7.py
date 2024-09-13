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


def sort_lines(lines: list[dict]) -> list[dict]:
    '''Sort the lines'''
    sorted = []
    unhandled_sources = [l for l in lines if l["inputs"]
                         [0].isnumeric() and l["gate"] == "SET"]
    while unhandled_sources:
        source = unhandled_sources.pop(0)

        sorted.append(source)

        next_nodes = [
            l for l in lines if source["target"] in l["inputs"]]

        for c in next_nodes:
            defined_inputs = 0
            for incoming in c["inputs"]:
                if incoming.isnumeric() or incoming in set([s["target"] for s in sorted]):
                    defined_inputs += 1
            if defined_inputs == len(c["inputs"]):
                unhandled_sources.append(c)

    return sorted


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


def one_star(filename: str, target: str = "a"):
    '''Returns the one star solution'''
    lines = load_file(filename)
    print(list(filter(lambda x: "t" in x["inputs"], lines)))
    for i, l in enumerate(lines):
        if l['target'] == target:
            print(i)
    lines = sort_lines(lines)

    print(lines)
    wire_signal_values = dict()

    command_map = get_command_map()

    for i, command in enumerate(lines):

        for w in [*command["inputs"], command["target"]]:
            if w.isalpha():
                add_wire_to_dictionary(w, wire_signal_values)

        if execute_command(command, wire_signal_values, command_map):
            wire_signal_values = execute_command(
                command, wire_signal_values, command_map)

    return wire_signal_values[target]


def two_star(filename: str):
    '''Returns the two star solution'''

    return


if __name__ == "__main__":
    print(f"One star test solution is {one_star(TEST_FILE, target="x")}")
    print(f"Two star test solution is {two_star(TEST_FILE)}")
    print(f"One star solution is {one_star(INPUT_FILE, target="a")}")
    # print(f"Two star solution is {two_star(INPUT_FILE)}")
