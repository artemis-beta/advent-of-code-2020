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
from typing import Dict, Any

LINE_REGEX = re.compile(r'^([a-z\s]+) bags contain (.+)', re.IGNORECASE)

def process_line(line: str, data_dict: Dict):
    if not LINE_REGEX.findall(line):
        return
    _parent, _contents = LINE_REGEX.findall(line)[0]
    for symbol in ['bags', 'bag', '.']:
        _contents = _contents.replace(symbol, '')
    _contents = [i.strip() for i in _contents.split(',')]

    data_dict[_parent] = {}

    for item in _contents:
        if item.lower() == "no other":
            continue
        parts = item.split(' ')
        n = int(parts[0])
        colour = ' '.join(parts[1:])
        data_dict[_parent][colour] = n

def assemble_bag_data(input_file: str) -> Dict:
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Could not find input file '{input_file}'")

    _data_dict: Dict[str, Any] = {}

    for line in open(input_file).readlines():
        process_line(line, _data_dict)

    return _data_dict

def iterative_search(bag_colour: str, bag_data: Dict):
    if 

if __name__ in "__main__":
    DATA_FILE = os.path.join(os.path.dirname(__file__), 'data.txt')
    assemble_bag_data(DATA_FILE)
