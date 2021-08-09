"""
How Much is True?
Create a function which returns the number of true values there are in an array.
"""

from unittest import TestCase


def count_true(bool_arr):
    # return sum([b for b in bool_arr if b])
    return sum(bool_arr)

class TestCountTrue(TestCase):

    def test_one(self):
        assert count_true([True, False, False, True, False]) == 2

    def test_two(self):
        assert count_true([False, False, False, False]) == 0

    def test_three(self):
        assert count_true([]) == 0
