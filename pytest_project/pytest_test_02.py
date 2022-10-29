import pytest

def test_method_2():
    x = 5
    y = 2
    assert x+y == 7, "Assertion failed, expected 7 but was " + str(x+y)
    assert x-y == 4, "Assertion failed, expected 4 but was " + str(x-y)