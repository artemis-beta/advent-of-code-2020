import pytest
import os
from advent_of_code.day_10 import get_prod_jolt_sums, get_n_distinct


@pytest.fixture
def data_1():
    DATA_INPUT = os.path.join(os.path.dirname(__file__), 'day_10_1.dat')
    return open(DATA_INPUT).readlines()


@pytest.fixture
def data_2():
    DATA_INPUT = os.path.join(os.path.dirname(__file__), 'day_10_2.dat')
    return open(DATA_INPUT).readlines()


@pytest.mark.day10
def test_1_3_prod1(data_1):
    assert get_prod_jolt_sums(data_1) == 35


@pytest.mark.day10
def test_1_3_prod2(data_2):
    assert get_prod_jolt_sums(data_2) == 220


@pytest.mark.day10
def test_ndistinct1(data_1):
    assert get_n_distinct(data_1) == 8


@pytest.mark.day10
def test_ndistinct2(data_2):
    assert get_n_distinct(data_2) == 19208
