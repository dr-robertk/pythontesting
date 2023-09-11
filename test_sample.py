import pytest
import numpy as np

# this will fail unless in requirements.txt
# import scipy

# content of test_sample.py (from pytest docu)
def func(x):
    return x + 1

def test_answer():
    assert func(4) == 5

@pytest.mark.parametrize("test_input, expected", [(4, 5), (3, 4), (7, 8)])
def test_func(test_input, expected):
    assert func(test_input) == expected
