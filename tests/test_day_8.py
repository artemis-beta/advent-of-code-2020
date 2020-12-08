import pytest
import os
from advent_of_code.day_8 import run_lines


@pytest.mark.day8
def test_bootup():
    DATA_INPUT = os.path.join(os.path.dirname(__file__), 'day_8.dat')

    assert run_lines(open(DATA_INPUT).readlines(), test=True) == 5
