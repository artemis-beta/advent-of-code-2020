#############################################################################################
#                                                                                           #
#                               ADVENT OF CODE 2020: Day 9                                  #
#                                                                                           #
#   @author :   K. Zarebski                                                                 #
#   @date   :   last modified 2020-12-09                                                    #
#                                                                                           #
#############################################################################################

import os
from typing import List
from itertools import combinations


def check_any_subset_totals(total: int, subset: List[int], n_sum: int) -> bool:
    for combination in combinations(subset, n_sum):
        if sum(combination) == total:
            return True
    return False


def XMAS_decoder(preamble_size: int, n_sum: int, data_lines: List[int]) -> int:
    for i, _ in enumerate(data_lines):
        total = data_lines[i+preamble_size]
        _check = check_any_subset_totals(
                total,
                data_lines[i:i+preamble_size],
                n_sum
        )

        if not _check:
            print(f"Invalid entry '{total}', aborting...")
            return total
    return -1


def find_data_vulnerability(preamble_size: int, n_sum: int, data_lines: List[str]) -> int:
    _int_lines = [int(i.strip()) for i in data_lines]

    _invalid_entry = XMAS_decoder(preamble_size, n_sum, _int_lines)

    if _invalid_entry == -1:
        print(f"No vulnerabilities found.")
        return _invalid_entry

    return _invalid_entry


def scan_file(data_input: str, preamble_size: int, n_sum: int) -> int:
    if not os.path.exists(data_input):
        raise FileNotFoundError(f"Could not find file '{data_input}'")

    return find_data_vulnerability(preamble_size, n_sum, open(data_input).readlines())


if __name__ in "__main__":
    DATA_INPUT = os.path.join(os.path.dirname(__file__), 'data.txt')
    PREAMBLE_SIZE = 25
    N_SUM = 2

    print(f'''
===============================================================

             XMAS Decoder and Vulnerability Finder

    Preamble Size   :       {PREAMBLE_SIZE}
    Input File      :       {DATA_INPUT}
    Values per Sum  :       {N_SUM}

===============================================================
    ''')

    scan_file(DATA_INPUT, PREAMBLE_SIZE, N_SUM)
