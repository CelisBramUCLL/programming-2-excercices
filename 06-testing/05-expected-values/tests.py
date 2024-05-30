import itertools
import pytest
from mergesort import *


@pytest.mark.parametrize("ns", [[n, n + 1, n + 2, n + 3, n + 4] for n in range(1000)])
def test_split_in_two(ns):
    left, right = split_in_two(ns)

    assert ns == left + right


@pytest.mark.parametrize("left", [[], [1], [1, 1, 2, 3, 4], [4, 9, 23], [-10, 9, 24]])
@pytest.mark.parametrize("right", [[], [1], [1, 1, 2, 3, 4], [4, 9, 23], [-10, 9, 24]])
def test_merge_sorted(left, right):
    assert merge_sorted(left, right) == sorted(left + right)


@pytest.mark.parametrize(
    "expected, ns",
    [
        (ns, list(permutation))
        for ns in [[], [1], [1, 2], [1, 4, 4, 6], [1, 2, 2, 4, 6, 9]]
        for permutation in itertools.permutations(ns)
    ],
)
def test_merge_sort(expected, ns):
    assert merge_sort(ns) == expected
