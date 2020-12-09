import pytest
import os
from advent_of_code.day_9 import find_data_vulnerability


@pytest.mark.day9
def test_data_vulnerability_finder():
    DATA_FILE = os.path.join(os.path.dirname(__file__), 'day_9.dat')
    PREAMBLE_SIZE = 5
    N_SUM = 2

    _lines = open(DATA_FILE).readlines()

    assert find_data_vulnerability(PREAMBLE_SIZE, N_SUM, _lines) == 127

