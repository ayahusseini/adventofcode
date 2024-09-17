from collections import defaultdict

INPUT_FILE = "inputs/day_7_input.txt"
TEST_FILE = "inputs/day_7_test_input.txt"


def load_file(filename: str) -> list[int]:
    '''Loads the file as a list of integers'''

    with open(filename, "r") as f:
        lines = f.readlines()

    return [l.replace("\n", "") for l in lines]


def get_components_from_text(component_text: str):
    ''' Component text is a text-representation
    of the component in the form inputs -> outputs'''

    gate_class = "NOGATE"
    for i in ["AND", "OR", "NOT", "LSHIFT", "RSHIFT"]:
        if i in component_text:
            gate_class = i
            break

    incoming_names = [i.strip() for i in component_text.split(
        " -> ")[0].split(" ") if i.islower() or i.isnumeric()]

    outgoing = component_text.split(" -> ")[1].strip()

    incoming = [i if i.isalpha() else int(i) for i in incoming_names]

    return {'in': incoming, 'out': outgoing, 'gate': gate_class}


def get_in_degrees(lines: list[dict]):
    '''Map each component id (position in the list) to the number of incoming wires'''
    return {i: len(
        list(filter(lambda x: not isinstance(x, int), l['in']))) for i, l in enumerate(lines)}


def sort_components(lines: list[dict]):
    in_degrees = get_in_degrees(lines)

    queue = [l for i, l in enumerate(lines) if in_degrees[i] == 0]
    sorted = []

    while queue:
        curr_component = queue[0]

        sorted.append(curr_component)
        next_wire = curr_component['out']

        next_component_ids = []
        for i, l in enumerate(lines):
            if next_wire in l['in']:
                next_component_ids += [i]

        # reduce the in degrees of the next component
        for i in next_component_ids:
            in_degrees[i] -= 1
            if in_degrees[i] == 0:
                queue.append(lines[i])

        queue.pop(0)

    return sorted


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


def get_command_map() -> dict:
    return {
        "AND": get_and,
        "OR": get_or,
        "NOT": get_complement,
        "LSHIFT": get_left_shift,
        "RSHIFT": get_right_shift
    }


def get_signal_value(lines: list[dict], wire_name: str):
    '''Get the value of the signal at a particular wire'''

    gate_command_map = get_command_map()
    lines = sort_components(lines)
    wire_values = dict()

    for l in lines:
        print(l)
        input_values = [i if isinstance(
            i, int) else wire_values.get(i) for i in l['in']]
        print(f"input {input_values}")
        gate = gate_command_map.get(l["gate"], False)

        if gate:
            wire_values[l['out']] = gate(*input_values)
        elif len(input_values) == 1:
            wire_values[l['out']] = input_values[0]
        print(f"wire values: {wire_values}")

        if wire_name in wire_values:
            return wire_values.get(wire_name)


def one_star(filename: str):
    lines = load_file(filename)
    nodes = [get_components_from_text(l) for l in lines]
    print(get_signal_value(nodes, 'a'))


if __name__ == "__main__":
    one_star(INPUT_FILE)
