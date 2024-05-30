import pytest
from mystatistics import average
from pytest import approx


@pytest.mark.parametrize(
    "ns, expected", [([1, 2, 3], 2), ([1, 1, 1], 1), ([0.1, 0.1, 0.1], 0.1)]
)
def test_average(ns, expected):
    assert average(ns) == approx(expected)
