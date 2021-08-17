"""
Given two lists
    the first of length two
    the second of unknown length
return a list with all values of second inserted between the elements of the first.
"""
from unittest import TestCase
from tools.decorators import function_details


@function_details
def tuck_in(arr1, arr2):
    return [arr1[0], *arr2, arr1[-1]]


class TestTuckIn(TestCase):

    def test_one(self):
        assert tuck_in([1, 10], [2, 3, 4, 5, 6, 7, 8, 9]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def test_two(self):
        assert tuck_in([15,150], [45, 75, 35]) == [15, 45, 75, 35, 150]

    def test_three(self):
        assert tuck_in([[1, 2], [5, 6]], [[3, 4]]) == [[1, 2], [3, 4], [5, 6]]