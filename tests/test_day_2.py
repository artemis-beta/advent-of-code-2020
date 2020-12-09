import pytest
import os
from advent_of_code.day_2 import process_file


@pytest.fixture
def processed_data():
    DATA_FILE = os.path.join(os.path.dirname(__file__), 'day_2.dat')
    return process_file(DATA_FILE)


@pytest.mark.day2
def test_sled_rental_pwd_check(processed_data):
    assert processed_data["sled"]["num"] == 2


@pytest.mark.day2
def test_toboggan_rental_pwd_check(processed_data):
    assert processed_data["toboggan"]["num"] == 1

