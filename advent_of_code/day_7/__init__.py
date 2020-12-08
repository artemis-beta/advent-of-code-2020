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
import tqdm
import sympy
from typing import Dict, Any, List, Iterable

LINE_REGEX = re.compile(r'^([a-z\s]+) bags contain (.+)', re.IGNORECASE)

GLOBALS = {}


def get_symbol(full_str: str):
    return ''.join(''.join(i[0:2]).upper() for i in full_str.split(' '))


def create_sympy_object(full_str: str):
    _symbol = get_symbol(full_str)
    GLOBALS[_symbol] = sympy.Symbol(_symbol)


def process_line(line: str, data_dict_int: Dict, data_dict_sym: Dict) -> None:
    if not LINE_REGEX.findall(line):
        return
    _parent, _contents = LINE_REGEX.findall(line)[0]
    for symbol in ['bags', 'bag', '.']:
        _contents = _contents.replace(symbol, '')
    _contents = [i.strip() for i in _contents.split(',')]

    data_dict_int[_parent] = {}
    data_dict_sym[_parent] = 0


    create_sympy_object(_parent)

    for item in _contents:
        parts = item.split(' ')
        colour = ' '.join(parts[1:])
        create_sympy_object(colour)


    for item in _contents:
        if item.lower() == "no other":
            data_dict_int[_parent] = 0
            data_dict_sym[_parent] = 1
            continue
        parts = item.split(' ')
        n = int(parts[0])
        colour = ' '.join(parts[1:])
        data_dict_int[_parent][colour] = n
        data_dict_sym[_parent] += n*GLOBALS[get_symbol(colour)]


def update_subs_list(subs_list):
    for i, item in enumerate(subs_list):
        subs_list[i] = subs_list[i].subs(subs_list)


def assemble_bag_data(input_file: str, search_for: str) -> Dict:
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Could not find input file '{input_file}'")

    _data_dict_int: Dict[str, Any] = {}
    _data_dict_sym: Dict[str, Any] = {}

    for line in open(input_file).readlines():
        process_line(line, _data_dict_int, _data_dict_sym)
    

    subs_list = [(GLOBALS[get_symbol(k)], _data_dict_sym[k]) for k in _data_dict_sym]

    print("Performing substitutions, this may take a while...")

    for key in tqdm.tqdm(_data_dict_sym):
        try:
            _data_dict_sym[key] = _data_dict_sym[key].subs(subs_list)
            update_subs_list(subs_list)
        except AttributeError:
            continue

    _unit_subs_list = [(k[0], 1) for k in subs_list]
    
    _data_dict_sym[search_for] = _data_dict_sym[search_for].subs(subs_list)
    _data_dict_sym[search_for] = _data_dict_sym[search_for].subs(_unit_subs_list)

    return _data_dict_int, _data_dict_sym


def iterative_search(bag_colour: str, bag_data: Dict,
                     colour_list: List[str] = []) -> Iterable[str]:
    for colour in bag_data:
        try:
            if bag_colour in bag_data[colour]:
                colour_list.append(colour)
                iterative_search(colour, bag_data, colour_list)
        except TypeError:
            continue
    return set(colour_list)


if __name__ in "__main__":
    DATA_FILE = os.path.join(os.path.dirname(__file__), 'data.txt')
    TARGET_BAG_COLOR = 'shiny gold'

    bag_data_dict_int, bag_data_dict_sym = assemble_bag_data(DATA_FILE, TARGET_BAG_COLOR)

    n_outer_bag_options = len(
            iterative_search(TARGET_BAG_COLOR, bag_data_dict_int)
    )

    print(bag_data_dict_sym[TARGET_BAG_COLOR])

    print(f'''

========================================================================

                       Luggage Transport

    For a {TARGET_BAG_COLOR} bag the number of outermost bag types
    which can ultimately transport this target luggage type is {n_outer_bag_options}.

========================================================================
    ''')
