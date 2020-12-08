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

def run_lines(script_lines: List[str], test:bool = False, quiet: bool = False) -> int:
    '''
    Run system using the given configuration

    Arguments
    ---------

    script_lines        lines of boot startup script
    
    Optional Arguments
    ------------------

    test                run in unit test mode
    quiet               turn off printout statements

    Returns
    -------

    If successful, returns the final value of the allocator
    
    '''
    accumulator = 0

    _current_line = 0
    
    if not quiet:
        print(f"[{colored('info', 'blue')}] Reading config lines")
        print(f"[ {colored('ok', 'green')} ] Determining accumulator value")

    _visited_lines = []

    while True:
        if _current_line in _visited_lines:
            if not quiet:
                print(f"[{colored('FAIL', 'red')}] Infinite boot sequence ... aborting")
                print(f"[....] accumulator returned {accumulator}")
            if test:
                return accumulator
            raise RuntimeError(f"Entering infinite loop")
        if _current_line >= len(script_lines):
            return accumulator
        _visited_lines.append(_current_line)
        if test:
            print(f"[{colored('TEST', 'yellow')}] LINE {_current_line}: {script_lines[_current_line].strip()}")
        cmd, arg = script_lines[_current_line].strip().split(' ')
        if cmd in ['acc', 'nop']:
            _current_line += 1
            if cmd == 'acc':
                accumulator += int(arg.replace('+', ''))
                if not quiet:
                    print(f"[....] Adjusting, acc = {accumulator}")
            else:
                if not quiet:
                    print(f"[ {colored('ok', 'green')} ] {choice(RANDOM_CMDS)} {choice(RANDOM_VARS)}")
        elif cmd == 'jmp':
            _current_line += int(arg.replace('+', ''))
        else:
            if not quiet:
                print(f"[{colored('FAIL', 'red')}] Command '{cmd}' not recognised ... boot failed!")
            exit()
        
    return accumulator

def run_boot_sequence(boot_config: str) -> None:
    '''
    Run the startup procedure using a given boot script

    Arguments
    ---------

    boot_config         script from which to perform boot procedure. Uses 

    '''
    if not os.path.exists(boot_config):
        raise FileNotFoundError(f"Could not locate file '{boot_config}'")

    print(f"[ {colored('ok', 'green')} ] Locating bootup config")
    with open(boot_config) as f:
        try:
            _accumulator = run_lines(f.readlines())
        except RuntimeError:
            return
    print(f"[ {colored('ok', 'green')} ] Accumulator set to value {_accumulator}")

def repair_boot_config(boot_script_lines: List[str]) -> int:
    '''
    Attempt a repair of the boot config script by switching jmp <-> nop statements

    Arguments
    ---------

    boot_script_lines       boot command lines from a run script

    '''
    _accumulator = None
    _lines_copy = [m for m in boot_script_lines]
    for i, line in enumerate(boot_script_lines):
        if 'jmp' in line:
            _lines_copy[i] = _lines_copy[i].replace('jmp', 'nop')
        elif 'nop' in line:
            _lines_copy[i] = _lines_copy[i].replace('nop', 'jmp')
        try:
            _accumulator = run_lines(_lines_copy, quiet=True)
            break
        except RuntimeError:
            _lines_copy = [m for m in boot_script_lines]
            continue
    return _accumulator

def fix_boot_sequence(boot_config: Optional[str] = BOOT_SCRIPT) -> None:
    '''
    Attempt a fix on the bootloader

    Optional Arguments
    ------------------

    boot_config             option to supply custom boot script, default will
                            repair existing configuration

    '''
    print(f"\nAttempting system repair...\n")
    if not os.path.exists(boot_config):
        raise FileNotFoundError(f"Could not locate file '{boot_config}'")

    _accumulator = repair_boot_config(open(boot_config).readlines())

    with open(boot_config) as f:
        _lines = f.readlines()

    if not _accumulator:
        print("Error: System boot could not be repaired, shutting down...")
        exit()
    print("Success: System boot repaired, rebooting...\n")
    _accumulator = run_lines(_lines_copy)
    print(f"[ {colored('ok', 'green')} ] Accumulator set to value {_accumulator}")

if __name__ in "__main__":
    run_boot_sequence()
    fix_boot_sequence()
