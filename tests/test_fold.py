"""This module is performing unit tests of the implementation of the fold function.
Run this module from the root directory by calling pytest tests/test_fold.py in the console."""

from src.fold import fold_implementation

def test_fold_addition():
    """Test the fold function with the simple addition operator"""
    expected = [({1,2,3}, 10, 16), 
                ([1,2,3], 10, 16), 
                ({1:'a', 2: 'b', 3: 'c'}, 10, 16),
                ((1,2,3), 10, 16),
                (range(1,4), 10, 16)]
    addition_fct = lambda x, y: x + y

    for input_sequence, starting_value, expected_value in expected:
        assert fold_implementation.fold(addition_fct, input_sequence, starting_value) == expected_value

def test_fold_multiplication():
    """Test the fold function with the simple multiplication operator"""
    expected = [([1,2,3], 2, 12),
                ([-1,-2,-3], 2, -12),
                ([1, 2, 2], "a", "aaaa"),
                ({1: "a", 2: "b", 3: "c"}, 2, 12)]
    multiplication_fct = lambda x, y: x*y

    for input_sequence, starting_value, expected_value in expected:
        assert fold_implementation.fold(multiplication_fct, input_sequence, starting_value) == expected_value
