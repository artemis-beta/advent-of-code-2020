import pytest
import os
import numpy as np
from advent_of_code.day_11 import find_stable_occupation, demo_ruleset, demo_ruleset_2


@pytest.fixture
def data_set():
    DATA_FILE = os.path.join(os.path.dirname(__file__), 'day_11.dat')
    _lines = open(DATA_FILE).readlines()
    _grid = [list(i.strip()) for i in _lines]
    return np.array(_grid)


@pytest.mark.day11
def test_find_stable_position_1(data_set):
    assert find_stable_occupation(data_set, demo_ruleset) == 37

@pytest.mark.day11
def test_find_stable_position_2(data_set):
    assert find_stable_occupation(data_set, demo_ruleset_2) == 26