import pytest


@pytest.mark.parametrize("component, sum", [(5, 10), (2, 4)])
def test_addition(component, sum):
    assert component + component == sum
