'''Solution for day 3 of the advent of code.

input = The diagnostic report, list of binary numbers.'''

FILENAME = "inputs/day_3_input.txt"


def extract_report(filename: str) -> list[str]:
    '''Return the diagnostic data'''

    r = []
    with open(filename, 'r') as f:
        for line in f.readlines():

            r.append(line.replace("\n", "").strip())
    return r


def convert_binary_to_decimal(binary: str) -> int:
    '''Return the decimal version of a binary number'''
    return int(binary, 2)


def get_counts(strings: list[str], n: int) -> dict:
    '''Return the count of each letter at the nth position of a string.'''
    counts = {"0": 0, "1": 1}
    for s in strings:
        counts[s[n]] += 1
    return counts


def get_most_freq_nth_letter(strings: list[str], n: int, opposite: bool = False) -> str:
    '''Return the most frequent nth letter in all the strings.
    Return the least frequent if opposite'''
    counts = get_counts(strings, n)
    min_or_max = max if not opposite else min
    return min_or_max(counts.items(), key=lambda x: x[1])[0]


def most_freq_at_each_pos(d: list[str], opposite: bool = False) -> list[str]:
    '''Given a list of equally sized strings, return a list containing the most frequent letter at each position.
    If opposite, return the least frequent.'''
    item_length = len(d[0])

    if not any(len(i) == item_length for i in d):
        raise ValueError("The items must be of equal length.")

    return [get_most_freq_nth_letter(d, i, opposite) for i in range(item_length)]


def get_gamma_rate(diagnostic_report: list[str]) -> int:
    '''Return the gamma rate as a decimal'''
    binary = "".join(most_freq_at_each_pos(diagnostic_report, opposite=False))
    return convert_binary_to_decimal(binary)


def get_epsilon_rate(diagnostic_report: list[str]) -> int:
    '''Return the gamma rate as a decimal'''
    binary = "".join(most_freq_at_each_pos(diagnostic_report, opposite=True))
    return convert_binary_to_decimal(binary)


def one_star_solution(filename: str) -> int:
    '''Return the power rate from the diagnostic report'''
    diag = extract_report(filename)
    return get_epsilon_rate(diag) * get_gamma_rate(diag)


if __name__ == "__main__":
    print(one_star_solution(FILENAME))
