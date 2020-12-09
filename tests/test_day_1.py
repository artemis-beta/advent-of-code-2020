import pytest
import os
from functools import reduce
from operator import mul
from advent_of_code.day_1 import get_numbers_totalling_N, tidy_data


@pytest.fixture
def data_set():
    DATA_FILE = os.path.join(os.path.dirname(__file__), 'day_1.dat')
    return tidy_data(DATA_FILE)


@pytest.mark.day1
def test_prod_of_2_nums_that_sum_to(data_set):
    nums = get_numbers_totalling_N(data_set, 2020, 2)
    assert reduce(mul, nums, 1) == 514579


@pytest.mark.day1
def test_prod_of_3_nums_that_sum_to(data_set):
    nums = get_numbers_totalling_N(data_set, 2020, 3)
    assert reduce(mul, nums, 1) == 241861950

