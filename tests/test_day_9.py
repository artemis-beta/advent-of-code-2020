import pytest
import os
from advent_of_code.day_9 import find_data_vulnerability, calculate_cipher_solution

PREAMBLE_SIZE = 5
N_SUM = 2


@pytest.fixture
def cipher():
    DATA_FILE = os.path.join(os.path.dirname(__file__), 'day_9.dat')
    return open(DATA_FILE).readlines()


@pytest.mark.day9
def test_data_vulnerability_finder(cipher):
    assert find_data_vulnerability(PREAMBLE_SIZE, N_SUM, cipher) == 127


@pytest.mark.day9
def test_XMAS_cipher_solver(cipher):
    assert calculate_cipher_solution(127, cipher) == 62
