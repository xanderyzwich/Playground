"""
Given an array, put the minimum value first and the maximum value last but do not sort any of the other numbers in the array! Do this in place, without creating a new array.
"""
from unittest import TestCase


def lambda_to_position(input_arr, func, position):
    value = func(input_arr)
    input_arr.remove(value)
    input_arr.insert(position, value)
    return input_arr


def min_first_max_last(input_arr):
    input_arr = lambda_to_position(input_arr, min, 0)
    return lambda_to_position(input_arr, max, len(input_arr) - 1)


class TestMinMax(TestCase):

    def test_one(self):
        assert min_first_max_last([8, 6, 1, 5, 10, 7]) == [1, 8, 6, 5, 7, 10]

    def test_two(self):
        assert min_first_max_last([5, 4, 7, 100, 10]) == [4, 5, 7, 10, 100]
