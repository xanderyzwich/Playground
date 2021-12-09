"""
Two Oldest Ages
The two oldest ages function/method needs to be completed.
It should take an array of numbers as its argument and return the two highest numbers within the array.
The returned value should be an array in the format [second oldest age, oldest age].
The order of the numbers passed in could be any order.
The array will always include at least 2 items.
If there are two or more oldest age, then return both of them in array format.
"""
from unittest import TestCase


def two_oldest_ages(ages):
    ordered_ages = ages
    ordered_ages.sort()
    return ordered_ages[-2:]


class TestOldest(TestCase):
    def test_one(self):
        assert two_oldest_ages([1, 2, 10, 8]) == [8, 10]
