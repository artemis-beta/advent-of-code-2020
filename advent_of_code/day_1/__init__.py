from itertools import combinations
from typing import List, Tuple
from functools import reduce
from operator import mul
import os


def get_numbers_totalling_N(numbers: List[int], total_N: int, n_numbers: int) -> Tuple[int]:
    '''
    Find the subset of numbers in a list which sum to the given total


    Arguments
    ---------

    numbers     list of numbers to search
    total_N     total to be met by summing subset
    n_numbers   size of the subset


    Returns
    -------

    A tuple containing the subset of integers which sum to the total

    '''

    for combo in combinations(numbers, n_numbers):
        if sum(combo) == total_N:
            return tuple(combo)
    
    raise ValueError(f"Could not find subset which summates to {total_N}")


def tidy_data(input_file: str):
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"File '{input_file}' not found")

    with open(input_file) as f:
        _lines = f.readlines()

    if not _lines:
        raise AssertionError(f"Failed to read data from input file.")

    _lines = [i.strip().replace('\\', '') for i in _lines]
    _lines = [i for i in _lines if i]
    _lines = [int(i) for i in _lines]

    return _lines


if __name__ in "__main__":
    DATA_INPUT = os.path.join(os.path.dirname(__file__), 'data.txt')

    data = tidy_data(DATA_INPUT)
    candidates_2 = get_numbers_totalling_N(data, 2020, 2)
    candidates_3 = get_numbers_totalling_N(data, 2020, 3)
    prod_2 = reduce(mul, candidates_2, 1)
    prod_3 = reduce(mul, candidates_3, 1)

    _out_str=f'''

Out of the values contained within: '{DATA_INPUT}' 
for the two cases of which subsets of 2 and 3 total 2020:

    - Values {candidates_2} total 2020, and give the product: {prod_2}
    - Values {candidates_3} total 2020, and give the prodict: {prod_3}

    '''

    print(_out_str)
