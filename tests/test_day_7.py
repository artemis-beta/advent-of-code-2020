import pytest
import os
from advent_of_code.day_7 import assemble_bag_data, iterative_search, get_bag_cost


@pytest.fixture
def data_dict_1():
    DATA_FILE = os.path.join(os.path.dirname(__file__), 'day_7_1.dat')
    return assemble_bag_data(DATA_FILE)


@pytest.fixture
def data_dict_2():
    DATA_FILE = os.path.join(os.path.dirname(__file__), 'day_7_2.dat')
    return assemble_bag_data(DATA_FILE)


@pytest.mark.day7
def test_n_possible_parents(data_dict_1):
    TARGET_BAG_COLOUR = 'shiny gold'
    n_outer_bag_options = len(
            iterative_search(TARGET_BAG_COLOUR, data_dict_1)
    )

    assert n_outer_bag_options == 4


@pytest.mark.day7
def test_bag_cost_1(data_dict_1):
    TARGET_BAG_COLOUR = 'shiny gold'
    assert get_bag_cost(TARGET_BAG_COLOUR, data_dict_1) == 32


@pytest.mark.day7
def test_bag_cost_2(data_dict_2):
    TARGET_BAG_COLOUR = 'shiny gold'
    assert get_bag_cost(TARGET_BAG_COLOUR, data_dict_2) == 126
