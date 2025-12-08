"""Solution to day 4 2021"""

TEST_FILENAME = "inputs/day_4_test.txt"
REAL_FILENAME = "inputs/day_4_input.txt"
DIM = 5


def load_data(filename: str) -> tuple[list[int], list[str]]:
    """Loads the data and returns the draw order and the list of board strings."""
    with open(filename, "r") as f:
        lines = f.readlines()

    order = convert_string_to_list_of_ints(lines.pop(0).replace("\n", ""), ",")

    board_lines = list(filter(lambda x: x != "\n", lines))

    board_lines = [l.replace("\n", "").strip() for l in board_lines]

    boards = [board_lines[i : i + 5] for i in range(len(board_lines)) if i % 5 == 0]

    return order, boards


def convert_string_to_list_of_ints(text: str, sep: str):
    """Converts a string to a list of ints"""
    l = text.strip().split(sep)

    return [int(i) for i in l if i.isnumeric()]


def convert_board_string_to_array(board: str) -> list[list[int]]:
    """Converts a board string into an array of integers"""
    return [convert_string_to_list_of_ints(row, " ") for row in board]


def create_new_board_status(dim: int) -> dict:
    """Return a dictionary with a new board's status
    with the number of marks in each row and column."""

    return {"rows": {i: 0 for i in range(dim)}, "cols": {i: 0 for i in range(dim)}}


def find_matching_index(
    board: list[list], target: int, matches: list = []
) -> list[tuple]:
    """Return an updated list of row,col index tuples where there's a match given a new draw."""

    for row_index, row in enumerate(board):
        for col_index, number in enumerate(row):
            if number == target:
                matches.append((row_index, col_index))
    return matches


def get_board_status(matching_indexes: list[tuple], dim: int) -> bool:
    """Given a list of marked indexes, return the board_status."""

    board_status = create_new_board_status(dim)
    for match in matching_indexes:
        r, c = match
        board_status["rows"][r] += 1
        board_status["cols"][c] += 1
    return board_status


def is_board_winner(board_status: dict):
    """Determines if a board_status is a winner."""
    return 5 in board_status["rows"].values() or 5 in board_status["cols"].values()


def sum_unmarked_matches(board: list, match_indexes: list):
    """Sums the unmarked matches"""
    tot = 0
    for i, row in enumerate(board):
        for j, n in enumerate(row):
            if (i, j) in match_indexes:
                pass
            else:
                tot += n
    return tot


def find_winning_score(board_list: list, numbers_to_draw: list[int]) -> int:
    """Find the score of the winning board"""
    board_matches = [[] for _ in range(len(board_list))]

    for num in numbers_to_draw:
        for i, board in enumerate(board_list):
            board_matches[i] = find_matching_index(board, num, board_matches[i])
            if is_board_winner(get_board_status(board_matches[i], DIM)):
                return sum_unmarked_matches(board, board_matches[i]) * num


def find_lowest_score(board_list: list, numbers_to_draw: list[int]) -> int:
    """Find the score of the last board to win."""
    board_matches = [[] for _ in range(len(board_list))]
    already_won = []
    nums_won_on = []
    for num in numbers_to_draw:
        for i, board in enumerate(board_list):
            if i in already_won:
                continue

            else:
                board_matches[i] = find_matching_index(board, num, board_matches[i])

            if is_board_winner(get_board_status(board_matches[i], DIM)):
                already_won.append(i)
                nums_won_on.append(num)
    return (
        sum_unmarked_matches(
            board_list[already_won[-1]], board_matches[already_won[-1]]
        )
        * nums_won_on[-1]
    )


def one_star(filename: str) -> int:
    numbers, board_strings = load_data(filename)
    boards = [convert_board_string_to_array(s) for s in board_strings]
    return find_winning_score(boards, numbers)


def two_star(filename: str) -> int:
    numbers, board_strings = load_data(filename)
    boards = [convert_board_string_to_array(s) for s in board_strings]
    return find_lowest_score(boards, numbers)


if __name__ == "__main__":
    print(one_star(REAL_FILENAME))
    print(two_star(REAL_FILENAME))
