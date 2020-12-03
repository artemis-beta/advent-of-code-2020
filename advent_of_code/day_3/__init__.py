#############################################################################################
#                                                                                           #
#                               ADVENT OF CODE 2020: Day 3                                  #
#                                                                                           #
#   @author :   K. Zarebski                                                                 #
#   @date   :   last modified 2020-12-03                                                    #
#                                                                                           #
#############################################################################################

import pandas as pd
import numpy as np
import os
from termcolor import colored
from tabulate import tabulate
from typing import Any, Tuple
from functools import reduce
from operator import mul
from math import ceil


def index_wrap(df: pd.DataFrame, row: int, col: int) -> Any:
    '''
    Loops back through the columns if the index requested is
    greater than the number of columns in the DataFrame

    Argument
    --------

    df      dataframe to search on
    index   index of column to request


    Returns
    -------

    Row, Column indices from the dataframe after wraparound

    '''
    if col > df.shape[1]-1:
        return row, (col % df.shape[1])-1
    else:
        return row, col


def map_dataframe(input_file: str) -> pd.DataFrame:
    '''
    Convert map in ASCII format to a Pandas DataFrame
    

    Arguments
    ---------

    input_file      input file address


    Returns
    -------

    Pandas dataframe of the given input map

    '''

    _df = pd.read_csv(input_file, sep='', engine='python', header=None, index_col=False)
    _df = _df.dropna(axis=1, how='all')

    return _df


def repeat_df(template_df: pd.DataFrame, n: int):
    return template_df.copy(deep=True)[np.tile(template_df.columns.values, n)]


def travel_down_slope(df: pd.DataFrame, slope_gradient: Tuple[int, int], start_pos: Tuple[int, int] = (0,0)):
    position = list(start_pos)

    A = df.shape[0]/slope_gradient[1]

    if A*slope_gradient[0] > df.shape[1]:
        n = ceil(A*slope_gradient[0]/df.shape[1])
    else:
        n = 1

    _out_df = repeat_df(df, n)

    while position[1] < _out_df.shape[1]:
        _indices = index_wrap(df, *position)
        try:
            if _out_df.iat[position[0], position[1]] == '#':
                _out_df.iat[position[0], position[1]] = 'X'
            else:
                _out_df.iat[position[0], position[1]] = 'O'
        except IndexError:
            break
        position[0] += slope_gradient[1]
        position[1] += slope_gradient[0]

    assert _out_df.shape[0] == df.shape[0], "Output dataframe has differing number of rows to input"

    return _out_df


def df_count_char(df: pd.DataFrame, val: str) -> int:
    _count = 0

    for i in range(df.shape[1]):
        try:
            _count += df.iloc[:, i].value_counts()['X']
        except KeyError:
            continue

    return _count


if __name__ in "__main__":
    DATA_FILE = os.path.join(os.path.dirname(__file__), 'data.txt')

    N = 20

    GRADIENTS = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    _map_df = map_dataframe(DATA_FILE)

    _travel_dfs = [travel_down_slope(_map_df, i) for i in GRADIENTS]

    _n_trees = [df_count_char(i, 'X') for i in _travel_dfs]

    _table = [[f'-{g[1]}/{g[0]}', n] for g, n in zip(GRADIENTS, _n_trees)]

    _table = tabulate(_table, headers=['dy/dx', '# Trees'], tablefmt='fancy_grid')

    _example = _travel_dfs[0].replace('.', colored(' ', 'white'))
    _example = _example.replace('#', colored('#', 'green'))
    _example = _example.replace('O', colored('o', 'blue'))
    _example = _example.replace('X', colored('X', 'red'))

    print(f'''

######################################################
    NUMBER OF TREES ENCOUNTERED FOR VARIOUS SLOPES
######################################################

{_table}

Product of all Totals: {reduce(mul, _n_trees, 1)}

######################################################
          EXAMPLE ROUTE FOR GRADIENT -2
######################################################

First {N} Rows:

{_example.head(N).iloc[:,0:N].to_string(header=False, index=False)}
    ''')
