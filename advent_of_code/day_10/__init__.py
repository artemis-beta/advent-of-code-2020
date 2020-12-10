#############################################################################################
#                                                                                           #
#                               ADVENT OF CODE 2020: Day 10                                 #
#                                                                                           #
#   @author :   K. Zarebski                                                                 #
#   @date   :   last modified 2020-12-10                                                    #
#                                                                                           #
#############################################################################################

import os
from typing import List, Tuple, Dict
from functools import reduce
from operator import mul


def get_adapter_ordering(
        joltage_list: List[int],
        start_joltage: int = 0,
        permitted_range_for_adaptor: List[int] = range(1, 4)) -> List[int]:

    _ordered_adapters = sorted(joltage_list)


def get_builtin_joltage(joltage_list: List[int]) -> int:
    return max(joltage_list) + 3


def get_prod_jolt_sums(data_input: List[str], device_joltage_diff = 3) -> int:
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


def process_file(data_input: str, device_joltage_diff: int) -> int:
    if not os.path.exists(data_input):
        raise FileNotFoundError(f"Could not find data file '{data_input}'")

    return get_prod_jolt_sums(
            open(data_input).readlines(),
            device_joltage_diff = device_joltage_diff
    )


if __name__ in "__main__":
    DATA_FILE = os.path.join(os.path.dirname(__file__), 'data.txt')
    DEVICE_DIFF = 3

    _distribution = process_file(DATA_FILE, DEVICE_DIFF)

    print(f'''
=================================================================

                    JOLTAGE ADAPTERS

    Input File                  :   {DATA_FILE}
    Device Joltage Difference   :   {DEVICE_DIFF}

=================================================================

The product of all differences is   :   {_distribution}

    ''')
