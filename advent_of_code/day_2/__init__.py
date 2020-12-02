#############################################################################################
#                                                                                           #
#                               ADVENT OF CODE 2020: Day 2                                  #
#                                                                                           #
#   @author :   K. Zarebski                                                                 #
#   @date   :   last modified 2020-12-02                                                    #
#                                                                                           #
#############################################################################################

import os
from typing import Dict, List


def check_password_sled_rental(pswd_cp: str, password: str) -> bool:
    '''
    Verify password satifies criteria of having N occurences of a character using a
    rule in the form: "lower_limit - upper_limit char" where the limits are integers
    for the maximum and minimum permitted occurences of character "char" in the password

    Arguments
    ---------

    pswd_cp     password corporate policy (i.e. validation rule)
    password    password to perform check on


    Returns
    -------

    Either True/False depending on if the password passes/fails the convention

    '''
    _permitted_range, char = pswd_cp.split(' ')
    _permitted_range = [int(i) for i in _permitted_range.split('-')]

    _count = password.count(char)

    return _count >= _permitted_range[0] and _count <= _permitted_range[1]


def check_password_toboggan_corp(pswd_cp: str, password: str) -> bool:
    '''
    Verify password satisfies criteria of having a character at exactly one of two index
    specified positions within a password string.
    The rule is in the form: "index_1 - index_2 char"

    Arguments
    ---------

    pswd_cp     password corporate policy (i.e. validation rule)
    password    password to perform check on


    Returns
    -------

    Either True/False depending on if the password passes/fails the convention

    '''

    _permitted_indices, char = pswd_cp.split(' ')
    _permitted_indices = [int(i) for i in _permitted_indices.split('-')]

    return sum([password[i-1] == char for i in _permitted_indices]) == 1

def process_file(input_file: str) -> Dict[str, Dict]:
    '''
    Run password checking on a list containing a password and the convention it must
    follow in order to be valid

    Arguments
    ---------

    input_file      File containing conventions along with password in the form, e.g.:
                    '1-3 c: dhsxxccskw'


    Returns
    -------

    Tuple containing total number of passwords and the number that pass the criteria

    '''

    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Failed to locate file '{input_file}'")
    
    _results = {t: {'list': [], 'num': None, 'denom': None} for t in ['sled', 'toboggan']}
    with open(input_file) as f:
        _lines = f.readlines()
        for line in _lines:
            password_cp, password = line.split(':')
            password_cp = password_cp.strip()
            password = password.strip()
            _results['sled']['list'].append(check_password_sled_rental(password_cp, password))
            _results['toboggan']['list'].append(check_password_toboggan_corp(password_cp, password))

    _results['sled']['denom'] = len(_results['sled']['list'])
    _results['sled']['num'] = sum(_results['sled']['list'])
    _results['toboggan']['denom'] = len(_results['toboggan']['list'])
    _results['toboggan']['num'] = sum(_results['toboggan']['list'])

    return _results

if __name__ in "__main__":
    DATA_FILE = os.path.join(os.path.dirname(__file__), 'data.txt')

    _results = process_file(DATA_FILE)

    print(f'''

Validation of Password Data Input File: {DATA_FILE}

Password Pass Rate for Sled Rental: {_results["sled"]["num"]}/{_results["sled"]["denom"]}
Password Pass Rate for Toboggan Rental: {_results["toboggan"]["num"]}/{_results["toboggan"]["denom"]}
    ''')
