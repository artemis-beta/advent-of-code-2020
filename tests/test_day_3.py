import os
import pytest
from functools import reduce
from operator import mul
from advent_of_code.day_3 import map_dataframe, travel_down_slope, df_count_char


GRADIENTS = [(3, 1), (1, 1), (5, 1), (7, 1), (1, 2)]


@pytest.fixture
def data_set():
    DATA_FILE = os.path.join(os.path.dirname(__file__), 'day_3.dat')
    return map_dataframe(DATA_FILE)


@pytest.mark.day3
def test_n_trees(data_set):
    df = travel_down_slope(data_set, GRADIENTS[0])
    assert df_count_char(df, 'X') == 7


def test_product_many_routes(data_set):
    dfs = [travel_down_slope(data_set, i) for i in GRADIENTS]
    n = [df_count_char(df, 'X') for df in dfs]
    assert reduce(mul, n, 1) == 336

