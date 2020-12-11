#############################################################################################
#                                                                                           #
#                               ADVENT OF CODE 2020: Day 11                                 #
#                                                                                           #
#   @author :   K. Zarebski                                                                 #
#   @date   :   last modified 2020-12-11                                                    #
#                                                                                           #
#############################################################################################

import os
import numpy as np


def demo_ruleset(x, grid):
    '''
    First part ruleset:
        - If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
        
        - If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
        Otherwise, the seat's state does not change.

    Arguments
    ---------

    grid    numpy array showing seat occupancy
    x       coordinate to process

    Returns
    -------

    New value for the given seat given the current environment

    '''
    _neighbours = []

    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            _neighbours.append([i, j])

    assert len(_neighbours) == 8, _neighbours

    _n_occupied = 0

    _current = grid[x[0]][x[1]]
    for coord in _neighbours:
        _neighbour = x+coord
        try:
            assert _neighbour[0] >= 0 and _neighbour[0] < grid.shape[0]
            assert _neighbour[1] >= 0 and _neighbour[1] < grid.shape[1]
            if grid[_neighbour[0]][_neighbour[1]] == '#':
                _n_occupied += 1
        except AssertionError:
            continue

    if _n_occupied == 0 and _current == 'L':
        return '#'
    elif _n_occupied >= 4 and _current == '#':
        return 'L'
    else:
        return _current

def demo_ruleset_2(x, grid):
    '''
    Second part ruleset:
        - If a seat is empty (L) and the nearest seats adjacent to it are not occupied, the seat becomes occupied.
        
        - If a seat is occupied (#) and five or more seats adjacent to it are also occupied, the seat becomes empty.
        Otherwise, the seat's state does not change.

    Arguments
    ---------

    grid    numpy array showing seat occupancy
    x       coordinate to process

    Returns
    -------

    New value for the given seat given the current environment

    '''
    _neighbours = []

    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            _neighbours.append([i, j])

    assert len(_neighbours) == 8, _neighbours

    _n_occupied = 0

    _current = grid[x[0]][x[1]]
    for coord in _neighbours:
        for i in range(1, int(0.5*grid.shape[1])):
            _neighbour = x+np.array([i*coord[0], i*coord[1]])
            try:
                assert _neighbour[0] >= 0 and _neighbour[0] < grid.shape[0]
                assert _neighbour[1] >= 0 and _neighbour[1] < grid.shape[1]
                if grid[_neighbour[0]][_neighbour[1]] == '#':
                    _n_occupied += 1
                    break
                elif grid[_neighbour[0]][_neighbour[1]] == 'L':
                    break
            except AssertionError:
                continue

    if _n_occupied == 0 and _current == 'L':
        return '#'
    elif _n_occupied >= 5 and _current == '#':
        return 'L'
    else:
        return _current


def find_stable_occupation(grid, rule_set = demo_ruleset) -> int:
    '''
    Find the point at which the seat occupancy no longer changes
    and return the total occupancy

    Arguments
    ---------

    grid        numpy array showing seat occupancy
    rule_set    rule set to follow

    Returns
    -------

    Return the occupancy at this stable point
    
    '''

    while True:
        _new_grid = np.full(grid.shape, '')

        for i in range(grid.shape[0]):
            for j in range(grid.shape[1]):
                _new_grid[i][j] = rule_set(np.array([i, j]), grid)

        if (_new_grid == '#').sum() == (grid == '#').sum():
            break

        grid = np.copy(_new_grid)

    return (grid == '#').sum()

def process_file(input_data: str, ruleset_id=0) -> int:
    '''
    Read lines from a data file and find the maximum occupancy for the dataset

    Arguments
    ---------

    input_data      input data file address
    ruleset_id      either 0 or 1 for the two rulesets

    Returns
    -------

    Maximum occupancy for the given data set

    '''
    _lines = open(input_data).readlines()
    _grid = [list(i.strip()) for i in _lines]
    _grid = np.array(_grid)
    _rulesets = {
        0: demo_ruleset,
        1: demo_ruleset_2
    }
    return find_stable_occupation(_grid, _rulesets[ruleset_id])


if __name__ in "__main__":
    DATA_INPUT = os.path.join(os.path.dirname(__file__), 'data.txt')

    print(f'''
======================================================

                SEAT OCCUPANCY

    Input File  :   {DATA_INPUT}

======================================================

Final stable occupancy Part 1 :   {process_file(DATA_INPUT, 0)}
Final stable occupancy Part 2 :   {process_file(DATA_INPUT, 1)}
    ''')
