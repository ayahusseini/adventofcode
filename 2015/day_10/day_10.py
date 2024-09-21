'''Solution to advent of code day 10 2021
'''

NUM_TRANSFORMS_1 = 40
NUM_TRANSFORMS_2 = 50
INPUT = "1113222113"


def transform_string(seq: str):
    final_string = ""
    i = 0
    while i < len(seq):

        s = seq[i]

        j = i
        while seq[i:j+1] == s * (j-i + 1) and j < len(seq):
            j += 1

        final_string += f"{j-i}{s}"

        i = j

    return final_string


def apply_n_transforms(input_seq: str, n: int):
    '''Apply n transforms and return the final string.'''
    curr_string = input_seq
    for i in range(n):
        curr_string = transform_string(curr_string)
    return curr_string


def one_star(input_sequence: str):
    '''Returns the one star solution'''

    return len(apply_n_transforms(input_sequence, NUM_TRANSFORMS_1))


def two_star(input_sequence: str):
    '''Returns the two star solution'''

    return len(apply_n_transforms(input_sequence, NUM_TRANSFORMS_2))


if __name__ == "__main__":

    print(f"One star solution is {one_star(INPUT)}")
    print(f"Two star solution is {two_star(INPUT)}")
