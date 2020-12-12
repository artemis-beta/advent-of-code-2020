#############################################################################################
#                                                                                           #
#                               ADVENT OF CODE 2020: Day 10                                 #
#                                                                                           #
#   @author :   K. Zarebski                                                                 #
#   @date   :   last modified 2020-12-10                                                    #
#                                                                                           #
#############################################################################################

import os
import re
from typing import List, Tuple, Dict
from functools import reduce
from scipy.stats import binom
from operator import mul


def get_prod_jolt_sums(data_input: List[str], device_joltage_diff = 3) -> int:
    '''
    Get the product of all the sums of joltages

    Arguments
    ---------

    data_input              list of adapter joltages as file lines
    (device_joltage_diff)   joltage difference between device and highest
                            adapter rating

    Returns
    -------

    Calculates the product of the number of 1-3 joltage differences
    between adapter ratings

    '''

    _data = [int(i.strip()) for i in data_input]
    _ordered = sorted(_data)

    _count_dict: Dict[int, int] = {}

    for i in range(len(_ordered)-1):
        _diff = _ordered[i+1]-_ordered[i]
        if _diff not in _count_dict:
            _count_dict[_diff] = 0
        _count_dict[_diff] += 1

    _count_dict[device_joltage_diff] += 1
    _count_dict[_ordered[0]] += 1

    return reduce(mul, _count_dict.values(), 1)


def tribonacci(n: int) -> int:
    '''
    Returns the nth term of the tribonacci sequence: 0, 0, 1, 1, 2, 4, ...
    '''
    if n in [0, 1]:
        return 0
    elif n == 2:
        return 1
    else:
        return tribonacci(n-1)+tribonacci(n-2)+tribonacci(n-3)

def get_consecutives_n_possibilities(nums: List[int]) -> int:
    '''
    Find the number of possible paths for the given number list

    Arguments
    ---------

    nums        list of numbers with max separation of 3

    Returns
    -------

    Total number of possible paths

    '''

    # Get all intervals between numbers
    _intervals = [j-i for i, j in list(zip(nums[:-1], nums[1:]))]

    # If there are any intervals of 2, then there are two possible routes
    # between groups so x2 on product, e.g.:
    # 
    #   [1, 2, 3, 5, 6]
    #
    #   3 -> 5, 3 -> 6 are both permitted
    #
    _fac_n2_interv = 2*_intervals.count(2) if _intervals.count(2) > 0 else 1
    
    # Split the interval list into groups of interval=1 by splitting by
    # any appearance of 3 or 2
    _group_sizes: List[str] = re.split('3|2', ''.join(map(str, _intervals)))

    # Get the number of integers in each group, remembering that
    # size_group = interval_size + 1
    _group_sizes_int: List[int] = [len(i)+1 for i in _group_sizes if i]

    # Take the produce of the Tribonacci sequence terms remembering that
    # the sequence is offset by 1 in this case (starts at 1 not 0)
    _product = reduce(mul, [tribonacci(i+1) for i in _group_sizes_int], 1)

    # Return produce applying count of interval 2 factor
    return _product*_fac_n2_interv

def get_n_distinct(data_input: List[str], permitted_intervals=[1,2,3]) -> int:
    '''
    Find the number of possible paths for the numbers in a given data file

    Arguments
    ---------

    data_input              data file containing list of adapters as integers

    (permitted_intervals)   allowed joltage differences between consecutive
                            adapter ratings

    Returns
    -------

    Total number of possible paths

    '''
    _data = sorted(int(i.strip()) for i in data_input)
    _con = 0

    # Start adapter can be any value within permitted intervals if available
    # so need to add all of these cases
    for i in permitted_intervals:
        if i in _data:
            _index_i = _data.index(i)
            _con += get_consecutives_n_possibilities(_data[_index_i:])
    return _con


def process_file(data_input: str, device_joltage_diff: int) -> int:
    '''
    Arguments
    ---------

    data_input              file containing list of adapter joltage ratings
    (device_joltage_diff)   joltage difference between device and highest
                            adapter rating

    Returns
    -------

    Calculates the product of the number of 1-3 joltage differences
    between adapter ratings

    '''
    if not os.path.exists(data_input):
        raise FileNotFoundError(f"Could not find data file '{data_input}'")

    return get_prod_jolt_sums(
            open(data_input).readlines(),
            device_joltage_diff = device_joltage_diff
    )


if __name__ in "__main__":
    DATA_FILE = os.path.join(os.path.dirname(__file__), 'data.txt')
    DEVICE_DIFF = 3
    PERMITTED_INTERVALS=[1,2,3]

    _distribution = process_file(DATA_FILE, DEVICE_DIFF)
    _n_combos = get_n_distinct(
        open(DATA_FILE).readlines(),
        PERMITTED_INTERVALS
    )

    print(f'''
=================================================================

                    JOLTAGE ADAPTERS

    Input File                  :   {DATA_FILE}
    Device Joltage Difference   :   {DEVICE_DIFF}
    Permitted Joltage Intervals :   {PERMITTED_INTERVALS}

=================================================================

The product of all differences is   :   {_distribution}

Number of combinations for device   :   {_n_combos}

    ''')
