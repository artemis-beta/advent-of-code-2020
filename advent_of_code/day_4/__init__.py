
#############################################################################################
#                                                                                           #
#                               ADVENT OF CODE 2020: Day 4                                  #
#                                                                                           #
#   @author :   K. Zarebski                                                                 #
#   @date   :   last modified 2020-12-04                                                    #
#                                                                                           #
#############################################################################################

from typing import Dict, List, Tuple
import os
import re


def passport_validator(passport_data: Dict[str, str], rules_dict: Dict[str, Dict]) -> bool:
    '''
    Check that a passport information dictionary has valid values


    Arguments
    ---------

    passport_data   dictionary containing key-value pairs of passport data
    rules_dict      dictionary containing rules for each value in the passport data
                    as lambdas


    Returns
    -------

    True if all conditions are satisfied else False

    '''
    if not all(i in passport_data for i in rules_dict):
        return False

    for key in rules_dict:
        if not rules_dict[key]['rule'](passport_data[key]):
            return False

    return True


def extract_passport_data(raw_data: str) -> Dict[str, str]:
    '''
    Convert a string of raw passport data to a dictionary


    Arguments
    ---------

    raw_data        raw passport data as a string


    Returns
    -------

    A dictionary of the processed data

    '''
    
    _item_find = re.compile(r'([a-z]+):([a-z0-9\#]+)', re.IGNORECASE)

    _items = _item_find.findall(raw_data)

    if not _items:
        raise AssertionError(f'Failed to extract data from raw data string')

    _out_dict: Dict[str, str] = {}

    for it in _items:
        key, value = it
        _out_dict[key.strip()] = value.strip()

    return _out_dict


def read_passport_data(input_file: str) -> List[Dict[str, str]]:
    '''
    Read passport data from file and convert to list of dictionaries


    Arguments
    ---------

    input_file      data file containing list of passports


    Returns
    -------

    A list of dictionaries containing passport data

    '''

    _passports: List[Dict[str, str]] = []

    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Failed to read passport data file '{input_file}'")

    
    _entry_data = open(input_file).readlines()

    if not _entry_data:
        raise AssertionError(f'Data input file is empty')

    _passport_raw: List[str] = []

    for line in _entry_data:
        if not line.strip():
            _passport = extract_passport_data(' '.join(_passport_raw))
            _passports.append(_passport)
            _passport_raw = []
        else:
            _passport_raw.append(line.strip())

    return _passports


def check_height(height_str: str, range_cm: Tuple[int, int],
                 range_in: Tuple[int, int]) -> bool:
    '''
    Check that provided height string satisfies range constraints


    Arguments
    ---------

    height_str      string to validate
    range_cm        permitted height range in centimetres
    range_in        permitted height range in inches


    Returns
    -------

    True if constraint is satisfied else False

    '''
    _height_check_cm = re.compile(r'([0-9]+)cm', re.IGNORECASE)
    _height_check_in = re.compile(r'([0-9]+)in', re.IGNORECASE)

    _height_cm = _height_check_cm.findall(height_str)
    _height_in = _height_check_in.findall(height_str)

    if not _height_in and not _height_cm:
        return False

    elif _height_in:
        _height = int(_height_in[0])
        return _height >= range_in[0] and _height <= range_in[1]

    else:
        _height = int(_height_cm[0])
        return _height >= range_cm[0] and _height <= range_cm[1]


def check_hair(hair_str: str) -> bool:

    _hair_check = re.compile(r'(#[0-9a-f]{6})', re.IGNORECASE)

    if len(hair_str) > 7:
        return False

    _hair_id = _hair_check.findall(hair_str)

    return len(_hair_id) == 1

if __name__ in "__main__":
    DATA_FILE = os.path.join(os.path.dirname(__file__), 'data.txt')

    REQUIRED_FIELDS = {
        'byr' : {
            'name': "Birth Year",
            'rule': lambda x: int(x) >= 1920 and int(x) <= 2002
        },
        'iyr' : {
            'name': "Issue Year",
            'rule': lambda x: int(x) >= 2010 and int(x) <= 2020
        },
        'eyr' : {
            'name': "Expiration Year",
            'rule': lambda x: int(x) >= 2020 and int(x) <= 2030
        },
        'hgt' : {
            'name': "Height",
            'rule': lambda x: check_height(x, (150, 193), (59, 76))
        },
        'hcl' : {
            'name': "Hair Color",
            'rule': lambda x: check_hair(x)
        },
        'ecl' : {
            'name': "Eye Color",
            'rule': lambda x: x in ['amb', 'blu', 'brn', 'gry',
                                    'grn', 'hzl', 'oth']
        },
        'pid' : {
            'name': "Passport ID",
            'rule': lambda x: x.isdigit() and len(x) == 9
        }
    }


    _passport_data = read_passport_data(DATA_FILE)

    _validator = lambda p : passport_validator(p, REQUIRED_FIELDS)

    _n_valid = sum(_validator(i) for i in _passport_data)
    
    print(f'''
##############################################################
                
                      PASSPORT CHECKER

    Input File                  : {DATA_FILE}
    Number of Valid Passports   : {_n_valid}/{len(_passport_data)}

##############################################################
    ''')
