import pytest
import os
from advent_of_code.day_8 import run_lines, repair_boot_config


@pytest.fixture
def boot_config():
    DATA_INPUT = os.path.join(os.path.dirname(__file__), 'day_8.dat')
    return open(DATA_INPUT).readlines()

@pytest.mark.day8
def test_bootup(boot_config):
    assert run_lines(boot_config, test=True) == 5

@pytest.mark.day8
def test_boot_repair(boot_config):
    assert repair_boot_config(boot_config)[1] == 8
