'''Solution to day 6 2021'''

TEST_FILE = "inputs/day_6_test_input.txt"
INPUT_FILE = "inputs/day_6_input.txt"
SEPARATOR = ","
BIRTHSPAN = 7
NUM_DAYS = 80
NUM_DAYS_TWO_STAR = 256


def load_file(filename: str) -> list[int]:
    '''Loads the file as a list of integers'''

    with open(filename, "r") as f:
        line = f.readline()
        as_strings = line.replace("\n", "").replace(" ", "").split(SEPARATOR)
    return [int(s) for s in as_strings if s]


def simulate_day(current_state: list[int]):
    '''Returns the next_state'''
    new_state = [i-1 if i > 0 else 6 for i in current_state]
    just_birthed = new_state.count(
        BIRTHSPAN - 1) - current_state.count(BIRTHSPAN)

    return [*new_state, *[8]*just_birthed]


def simulate_n_days(n: int, initial_state: int):
    '''Returns the state after n days'''
    for _ in range(n):
        initial_state = simulate_day(initial_state)
    return initial_state


def one_star(filename: str) -> int:
    '''Count the number of fish after some days'''
    initial = load_file(filename)
    return len(simulate_n_days(NUM_DAYS, initial))


def two_star(filename: str) -> int:
    '''Count the number of fish after some days'''
    initial = load_file(filename)
    return len(simulate_n_days(NUM_DAYS_TWO_STAR, initial))


if __name__ == "__main__":
    print(f"One star solution in test is {
          one_star(TEST_FILE)}")
    print(f"Two star solution in test is {
        two_star(TEST_FILE)}")
    print(f"One star solution is {
          one_star(INPUT_FILE)}")
    print(f"Two star solution is {
        two_star(INPUT_FILE)}")
