"""
Array.diff
Our goal in this kata is to implement a difference function,
    which subtracts one list from another and returns the result.
It should remove all values from list a, which are present in list b keeping their order.
"""
from unittest import TestCase


def list_diff(a, b):
    return [x for x in a if x not in b]


class TestListDiff(TestCase):
    def test_one(self):
        assert list_diff([1, 2], [1]) == [2]

    def test_two(self):
        assert list_diff([1, 2, 2, 2, 3], [2]) == [1, 3]

    def test_three(self):
        assert list_diff([1, 2, 2, 2, 3], [1, 3]) == [2, 2, 2]


def list_diff_left_right(a, b):
    left = [x for x in a if x not in b]
    right = [x for x in b if x not in a]
    return left, right


class TestDiffLR(TestCase):
    def test_one(self):
        assert list_diff_left_right([1, 2], [1]) == ([2], [])

    def test_two(self):
        assert list_diff_left_right([1, 2, 2, 2, 3], [2]) == ([1, 3], [])

    def test_three(self):
        assert list_diff_left_right([1, 2, 2, 2], [1, 3, 3]) == ([2, 2, 2], [3, 3])
