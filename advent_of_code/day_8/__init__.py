#############################################################################################
#                                                                                           #
#                               ADVENT OF CODE 2020: Day 8                                  #
#                                                                                           #
#   @author :   K. Zarebski                                                                 #
#   @date   :   last modified 2020-12-08                                                    #
#                                                                                           #
#############################################################################################

import os
from termcolor import colored
from typing import List, Optional
from random import choice

BOOT_SCRIPT = os.path.join(os.path.dirname(__file__), 'data.txt')
RANDOM_CMDS = ['Configuring', 'Updating', 'Verifying options for process',
               'Checking runtime latency for process', 'Finding libraries from process']
RANDOM_VARS = ['dhoc', 'lbfort', 'imgf', 'dsk2', 'xsfc', 'hmd0', 'apr-cr', 'ts3']

def run_lines(script_lines: List[str], test:bool = False) -> int:
    accumulator = 0

    _current_line = 0
    
    print(f"[{colored('info', 'blue')}] Reading config lines")
    print(f"[ {colored('ok', 'green')} ] Determining accumulator value")

    _visited_lines = []

    while True:
        if _current_line in _visited_lines:
            print(f"[{colored('FAIL', 'red')}] Infinite boot sequence ... aborting")
            print(f"[....] accumulator returned {accumulator}")
            if test:
                return accumulator
            exit()
        _visited_lines.append(_current_line)
        if test:
            print(f"[{colored('TEST', 'yellow')}] LINE {_current_line}: {script_lines[_current_line].strip()}")
        cmd, arg = script_lines[_current_line].strip().split(' ')
        if cmd in ['acc', 'nop']:
            _current_line += 1
            if cmd == 'acc':
                accumulator += int(arg.replace('+', ''))
                print(f"[....] Adjusting, acc = {accumulator}")
            else:
                print(f"[ {colored('ok', 'green')} ] {choice(RANDOM_CMDS)} {choice(RANDOM_VARS)}")
        elif cmd == 'jmp':
            _current_line += int(arg.replace('+', ''))
        else:
            print(f"[{colored('FAIL', 'red')}] Command '{cmd}' not recognised ... boot failed!")
            exit()
        
    return accumulator

def run_boot_sequence(boot_config: Optional[str] = BOOT_SCRIPT) -> None:
    if not os.path.exists(boot_config):
        raise FileNotFoundError(f"Could not locate file '{boot_config}'")

    print(f"[ {colored('ok', 'green')} ] Locating bootup config")
    with open(boot_config) as f:
        _accumulator = run_lines(f.readlines())
    print(f"[ {colored('ok', 'green')} ] Accumulator set to value {_accumulator}")


if __name__ in "__main__":
    run_boot_sequence()
