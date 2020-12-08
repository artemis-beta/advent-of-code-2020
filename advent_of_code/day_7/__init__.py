#############################################################################################
#                                                                                           #
#                               ADVENT OF CODE 2020: Day 7                                  #
#                                                                                           #
#   @author :   K. Zarebski                                                                 #
#   @date   :   last modified 2020-12-07                                                    #
#                                                                                           #
#############################################################################################

import os
import re
import sympy
from typing import Dict, Any, List, Iterable

LINE_REGEX = re.compile(r'^([a-z\s]+) bags contain (.+)', re.IGNORECASE)


def process_line(line: str, data_dict_int: Dict) -> None:
    '''
    Process line in bag colour transport rule specification

    Arguments
    ---------

    line            string containing the requirements for a given
                    bag type

    data_dict_int   dictionary to save the result to

    '''
    if not LINE_REGEX.findall(line):
        return
    _parent, _contents = LINE_REGEX.findall(line)[0]
    for symbol in ['bags', 'bag', '.']:
        _contents = _contents.replace(symbol, '')
    _contents = [i.strip() for i in _contents.split(',')]

    data_dict_int[_parent] = {}

    for item in _contents:
        if item.lower() == "no other":
            data_dict_int[_parent] = 0
            continue
        parts = item.split(' ')
        n = int(parts[0])
        colour = ' '.join(parts[1:])
        data_dict_int[_parent][colour] = n


def assemble_bag_data(input_file: str) -> Dict:
    '''
    Create dictionary of bag requirements for a given bag colour


    Arguments
    ---------

    input_file      file containing bag requirement descriptions

    
    Returns
    -------

    A dictionary for the given requirements, number of bags of a given colour needed

    '''
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Could not find input file '{input_file}'")

    _data_dict_int: Dict[str, Any] = {}

    for line in open(input_file).readlines():
        process_line(line, _data_dict_int)
    
    return _data_dict_int


def iterative_search(bag_colour: str, bag_data: Dict,
                     colour_list: List[str] = []) -> Iterable[str]:
    '''
    Search for the outermost bags that contain a given bag colour

    Arguments
    ---------

    bag_colour      target bag colour to be contained
    bag_data        dictionary to search through
    colour_list     colours which meet requirement (iteration variable)

    Returns
    -------

    List of colour bags which can contain the target bag

    '''
    for colour in bag_data:
        try:
            if bag_colour in bag_data[colour]:
                colour_list.append(colour)
                iterative_search(colour, bag_data, colour_list)
        except TypeError:
            continue
    return set(colour_list)

def get_bag_cost(bag_colour: str, bag_data: Dict, nested: bool=False) -> int:
    '''
    Get the contents of a given colour of bag

    Arguments
    ---------

    bag_colour      colour of bag to examine contents of
    bag_data        data to perform search on

    (nested)        if being run within another call to the same function

    Returns
    -------

    Total bag cost
    '''
    total_exp = int(nested)
    if bag_data[bag_colour] == 0:
        return 1
    for key in bag_data[bag_colour]:
        total_exp += bag_data[bag_colour][key]*get_bag_cost(key, bag_data, True)
    return total_exp

if __name__ in "__main__":
    DATA_FILE = os.path.join(os.path.dirname(__file__), 'data.txt')
    TARGET_BAG_COLOR = 'shiny gold'

    bag_data_dict_int = assemble_bag_data(DATA_FILE)

    n_outer_bag_options = len(
            iterative_search(TARGET_BAG_COLOR, bag_data_dict_int)
    )

    _bag_cost = get_bag_cost(TARGET_BAG_COLOR, bag_data_dict_int)

    print(f'''
========================================================================

                       Luggage Transport

    For a {TARGET_BAG_COLOR} bag the number of outermost bag types
    which can ultimately transport this target luggage type is {n_outer_bag_options}.

    The number of bags in total required to transport a {TARGET_BAG_COLOR}
    bag is {_bag_cost}.

========================================================================
    ''')
