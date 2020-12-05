import pytest
from advent_of_code.day_5 import process_seat_code

def test_seat_binary_search():
    examples = [
        {'alloc': 'FBFBBFFRLR', 'loc': (44, 5)},
        {'alloc': 'BFFFBBFRRR', 'loc': (70, 7)},
        {'alloc': 'FFFBBBFRRR', 'loc': (14, 7)},
        {'alloc': 'BBFFBBFRLL', 'loc': (102, 4)}
    ]

    for example in examples:
        print(f"Checking that pattern \'{example['alloc']}\' returns Row: {example['loc'][0]}, Column: {example['loc'][1]}")
        assert process_seat_code(example['alloc']) == example['loc'], \
            f"Test failed on example: {example}"
        print("SUCCESS!")
