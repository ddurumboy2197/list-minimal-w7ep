# test_minimal_number.py
import pytest
from minimal_number import find_minimal_number

def test_empty_list():
    assert find_minimal_number([]) == None

def test_single_element_list():
    assert find_minimal_number([5]) == 5

def test_multiple_element_list():
    assert find_minimal_number([10, 5, 3, 8, 2]) == 2

def test_negative_numbers():
    assert find_minimal_number([-5, -10, -3, -8, -2]) == -10

def test_zero():
    assert find_minimal_number([0, 5, 3, 8, 2]) == 0

def test_all_positive_numbers():
    assert find_minimal_number([5, 10, 3, 8, 2]) == 2

def test_all_negative_numbers():
    assert find_minimal_number([-5, -10, -3, -8, -2]) == -10
