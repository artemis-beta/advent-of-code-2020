#############################################################################################
#                                                                                           #
#                               ADVENT OF CODE 2020: Day 9                                  #
#                                                                                           #
#   @author :   K. Zarebski                                                                 #
#   @date   :   last modified 2020-12-09                                                    #
#                                                                                           #
#############################################################################################

import os
from typing import List, Tuple
from itertools import combinations


def check_any_num_set_totals(total: int, num_set: List[int], n_sum: int) -> bool:
    '''
    For a given num_set of numbers, determine if the num_set summates to a total

    Arguments
    ---------

    total   total to try to find compatible sum for
    num_set  set of numbers to find sum from
    n_sum   size of the sample to summate

    Returns
    -------

    True if a subset of the given list summaets to the total

    '''
    for combination in combinations(num_set, n_sum):
        if sum(combination) == total:
            return True
    return False


def get_invalid_entry(preamble_size: int, n_sum: int, data_lines: List[int], quiet: bool = False) -> int:
    '''
    Get entry which is invalid from data lines

    Arguments
    ---------

    preamble_size   size of the starting set of numbers
    n_sum           number of values to summate at a time
    data_lines      lines of digits to examine

    (quiet)         do not print outputs

    Returns
    -------

    The value of the invalid entry, else -1

    '''
    for i, _ in enumerate(data_lines):
        total = data_lines[i+preamble_size]
        _check = check_any_num_set_totals(
                total,
                data_lines[i:i+preamble_size],
                n_sum
        )

        if not _check:
            if not quiet:
                print(f"Invalid entry '{total}', aborting...")
            return total
    return -1


def find_data_vulnerability(preamble_size: int, n_sum: int, data_lines: List[str], quiet: bool = False) -> int:
    '''
    Find the vulnerability within the given data set after preparing the data set

    Arguments
    ---------

    preamble_size   size of the starting set of numbers
    n_sum           number of values to summate at a time
    data_lines      lines of digits to examine

    (quiet)         do not print outputs

    Returns
    -------

    The value of the invalid entry else -1

    '''
    _int_lines = [int(i.strip()) for i in data_lines]

    _invalid_entry = get_invalid_entry(preamble_size, n_sum, _int_lines, quiet)

    if _invalid_entry == -1:
        if not quiet:
            print(f"No vulnerabilities found.")
        return _invalid_entry

    return _invalid_entry


def get_range_for_total(total: int, data_input: List[int]) -> Tuple[int, int]:
    '''
    Get the indices for the range within a data set, the values within which
    summate to a given total

    Arguments
    ---------

    total       total to try to match
    data_input  list of integers to search within

    Returns
    -------

    Tuple of start, end indices for the range

    '''
    _total_line_index = data_input.index(total)
    _possible_lengths = range(1, _total_line_index+1)

    for length in _possible_lengths:
        for i in range(_total_line_index-length):
            if sum(data_input[i:i+length]) == total:
                return i, i+length
    raise AssertionError(f"Failed to find indices of values summating to {total}")


def scan_file(data_input: str, preamble_size: int, n_sum: int, quiet: bool = False) -> int:
    '''
    Scan the file to find any vulnerability in the cipher

    Arguments
    ---------

    data_input          address of input file
    preamble_size       size of process group (number of lines to process at a time)
    n_sum               number of digits to sum at a time

    (quiet)             do not print anything

    '''
    if not os.path.exists(data_input):
        raise FileNotFoundError(f"Could not find file '{data_input}'")

    return find_data_vulnerability(preamble_size, n_sum, open(data_input).readlines(), quiet)


def calculate_cipher_solution(vulnerability: int, data_input: List[str]) -> int:
    '''
    Calculate the solution to the cipher by summating the lowest and highest values
    in the range that summates to the vulnerability value

    Arguments
    ---------

    vulnerability   value which cracks cipher
    data_input      data set to solve cipher for as list of lines

    Returns
    -------

    Cipher solution

    '''
    _data = [int(i.strip()) for i in data_input]
    i0, i1 = get_range_for_total(vulnerability, _data)
    _data = list(sorted(_data[i0:i1]))
    return _data[0]+_data[-1]


def solve_XMAS_cipher(data_input: str, preamble_size: int, n_sum: int) -> int:
    '''
    Determine vulnerability value and use it to crack the cipher for a given
    data file

    Arguments
    ---------

    data_input      address of data input file
    preamble_size   number of lines to process at a time
    n_sum           number of values to summate within the subset

    Returns
    -------

    Solution to the XMAS cipher

    '''
    _vulnerability = scan_file(data_input, preamble_size, n_sum, True)
    _solution = calculate_cipher_solution(_vulnerability, open(data_input).readlines())
    print(f"Decoded solution for XMAS Cipher : {_solution}")
    return _solution


if __name__ in "__main__":
    DATA_INPUT = os.path.join(os.path.dirname(__file__), 'data.txt')
    PREAMBLE_SIZE = 25
    N_SUM = 2

    print(f'''
==========================================================================================

                        XMAS Decoder and Vulnerability Finder

    Preamble Size   :       {PREAMBLE_SIZE}
    Input File      :       {DATA_INPUT}
    Values per Sum  :       {N_SUM}

=========================================================================================
    ''')

    scan_file(DATA_INPUT, PREAMBLE_SIZE, N_SUM)
    print('\n')
    solve_XMAS_cipher(DATA_INPUT, PREAMBLE_SIZE, N_SUM)
    print('\n')
