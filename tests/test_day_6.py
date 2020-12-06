import pytest
import os
from advent_of_code.day_6 import get_totals_from_lines


@pytest.fixture
def day_6_totals():
    DATA_FILE = os.path.join(os.path.dirname(__file__), 'day_6.dat')

    lines = open(DATA_FILE).readlines()

    _totals = get_totals_from_lines(lines)

    return _totals

@pytest.mark.day6
def test_total_yes_or(day_6_totals):
    assert day_6_totals[0] == 11


@pytest.mark.day6
def test_total_yes_and(day_6_totals):
    assert day_6_totals[1] == 6
