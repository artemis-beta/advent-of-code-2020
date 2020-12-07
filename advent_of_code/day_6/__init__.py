#############################################################################################
#                                                                                           #
#                               ADVENT OF CODE 2020: Day 6                                  #
#                                                                                           #
#   @author :   K. Zarebski                                                                 #
#   @date   :   last modified 2020-12-06                                                    #
#                                                                                           #
#############################################################################################

import os
from typing import List, Tuple


def num_yes_questions_for_group_or(input_str: str) -> int:
    '''
    For a given group of individuals find the number of questions to which one
    or more individuals answered 'yes' (OR).


    Arguments
    ---------

    input_str       input string for the given group

    Returns
    -------

    Number of questions to which at least one group member answered 'yes'

    '''
    return len(set(list(input_str.strip())))

def num_yes_questions_for_group_and(input_str_list: List[str]) -> int:
    '''
    For a given group of individuals find the number of questions to which the
    all members of the group answered yes (AND).


    Arguments
    ---------

    input_str_list       input string list for the given group

    Returns
    -------

    Number questions to which all members of the group answered 'yes'

    '''

    _all_chars = set(list(''.join(input_str_list)))

    _answered_yes_by_group = [i for i in _all_chars if sum(i in j for j in input_str_list) == len(input_str_list)]

    return len(_answered_yes_by_group)


def get_totals_from_lines(input_lines: List[str]) -> Tuple[int, int]:
    '''
    For the given string input lines return the total number of questions
    for which at least person answered 'yes', and the total number of questions
    for which all people answered 'yes' for all groups

    
    Arguments
    ---------

    input_lines     list of strings which are lines of the input file

    Returns
    -------

    A tuple containing the two totals for:
        - At least one answered yes
        - All answered yes

    '''
    _counter_or = 0
    _counter_and = 0
    _group = []

    for i, line in enumerate(input_lines):
        if not line.strip():
            _counter_or += num_yes_questions_for_group_or(''.join(_group))
            _counter_and += num_yes_questions_for_group_and(_group)
            _group = []
        elif i == len(input_lines)-1 and line.strip():
            _group.append(line.strip())
            _counter_or += num_yes_questions_for_group_or(''.join(_group))
            _counter_and += num_yes_questions_for_group_and(_group)
        else:
            _group.append(line.strip())

    return _counter_or, _counter_and


def get_total_for_flight(input_file: str) -> Tuple[int, int]:

    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Could not find file '{input_file}'")

    lines = open(input_file).readlines()

    return get_totals_from_lines(lines)


if __name__ in "__main__":
    DATA_FILE = os.path.join(os.path.dirname(__file__), 'data.txt')

    _flight_data = get_total_for_flight(DATA_FILE)

    print(f'''
===========================================================================================

                               FLIGHT SURVEY RESULT

    Total Questions Answered 'Yes' for method 'at least one'  :       {_flight_data[0]}
    Total Questions Answered 'Yes' for method 'all'           :       {_flight_data[1]}

===========================================================================================
    ''')
