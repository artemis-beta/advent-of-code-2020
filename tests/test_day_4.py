import pytest
import os
from advent_of_code.day_4 import passport_validator, read_passport_data


@pytest.mark.day4
def test_validator():
    DATA_FILE = os.path.join(os.path.dirname(__file__), 'day_4.dat')
    REQUIRED_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    _data = read_passport_data(DATA_FILE)

    _validator = lambda p : passport_validator(p, REQUIRED_FIELDS)

    _n_valid = sum(_validator(i) for i in _data)

    assert _n_valid == 2
