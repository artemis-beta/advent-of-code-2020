#############################################################################################
#                                                                                           #
#                               ADVENT OF CODE 2020: Day 5                                  #
#                                                                                           #
#   @author :   K. Zarebski                                                                 #
#   @date   :   last modified 2020-12-05                                                    #
#                                                                                           #
#############################################################################################

import os
from typing import Dict, List, Callable, Optional, Tuple


def binary_search(search_str: str, delimiter_char: str) -> int:
    '''
    For a given binary search string, return the resulting integer from
    a list of numbers.


    Arguments
    ---------

    search_str      binary search string describing integer position
    delimiter_char  character to indicate "take first half" in integer list

    Returns
    -------

    Integer matching search result

    '''
    _numbers = [i for i in range(0, 2**len(search_str))]
    for char in list(search_str):
        _mid_point = int(len(_numbers)/2)
        if char == delimiter_char:
            _numbers = _numbers[:_mid_point]
        else:
            _numbers = _numbers[_mid_point:]
    return _numbers[0]


def get_row(row_str: str):
    '''Get row ID for a given row search string'''
    return binary_search(row_str, 'F')


def get_col(col_str: str):
    '''Get column ID for a given column search string'''
    return binary_search(col_str, 'L')


def process_seat_code(seat_binary_str: str) -> Tuple[int, int]:
    '''
    Get the row and column number for a given search string


    Arguments
    ---------

    seat_binary_str     seat search string in the form 7*[F|B]+3*[L|R]

    Returns
    -------

    Tuple containing integer ID for the row and column

    '''
    _row_str = [i for i in list(seat_binary_str) if i in ['F', 'B']]
    _col_str = [i for i in list(seat_binary_str) if i in ['R', 'L']]
    r = get_row(_row_str)
    c = get_col(_col_str)
    return r, c


def get_seat_id(row: int, col: int, calc_func: Optional[Callable]=None) -> int:
    '''
    Calculate the row ID using a given function


    Arguments
    ---------

    row         row integer ID
    col         column integer ID

    Optional Arguments
    ------------------

    calc_func   function to calculate the seat ID. Default is 8*r+c.

    Returns
    -------

    Seat ID as integer

    '''
    if not calc_func:
        calc_func = lambda r, c: 8*r+c
    return calc_func(row, col)


def get_allocations_as_dict(input_file: str) -> Dict[int, List[int]]:
    '''
    Create dictionary of seat allocations


    Arguments
    ---------

    input_file      string address of input file

    Returns
    -------

    A dictionary with row number as a key, and a list of occupied seats in that
    row as the value

    '''

    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Could not find file '{input_file}'")

    _allocations = open(input_file).readlines()

    _allocated: Dict[int, List[int]] = {}

    for alloc in _allocations:
        r, c = process_seat_code(alloc)
        if r not in _allocated:
            _allocated[r] = []
        _allocated[r].append(c)

    return _allocated


def get_highest_booked_seat_id(bookings_dict: Dict[int, List[int]]) -> int:
    '''
    Get the seat ID for the highest numbered booked seat on the plane


    Arguments
    ---------

    bookings_dict           dictionary of seat allocations with rows as keys and columns
                            which are occupied as value lists.

    Returns
    -------

    Seat ID integer

    '''
    _highest_booked_row = list(sorted(bookings_dict.keys()))[-1]
    _highest_booked_col = list(sorted(bookings_dict[_highest_booked_row]))[-1]

    return get_seat_id(_highest_booked_row, _highest_booked_col)


def find_unallocated_seat(allocations_dict: Dict[int, List[int]], expected_n_cols: int) -> int:
    '''
    Given that all but one seat of the plane is occupied, find the seat ID of the
    unoccupied seat using the expected number seat occupancies per row.

    Arguments
    ---------

    allocations_dict        dictionary of seat allocations with rows as keys and columns
                            which are occupied as value lists.

    expected_n_cols         expected number of occupied seats per row.

    Returns
    -------

    Unallocated seat ID integer

    '''
    for r in sorted(list(allocations_dict.keys())):
        if len(allocations_dict[r]) == expected_n_cols - 1:
            for i in range(expected_n_cols):
                if i not in allocations_dict[r]:
                    return get_seat_id(r, i)
    raise AssertionError(f"Failed to find unoccupied seat ID")


if __name__ in "__main__":
    DATA_FILE = os.path.join(os.path.dirname(__file__), 'data.txt')

    _example_search_str = open(DATA_FILE).readlines()[0]

    bookings = get_allocations_as_dict(DATA_FILE)
    expected_n_cols = 2**sum(i in ['L', 'R'] for i in _example_search_str)
    highest_id = get_highest_booked_seat_id(bookings)

    print("======================= AIRCRAFT SEAT RESERVATIONS ===================")
    print(f'\tHighest Booked Seat ID  : {highest_id}')
    print(f'\tUnoccupied Seat ID      : {find_unallocated_seat(bookings, expected_n_cols)}')
    print("======================================================================")
