"""
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero.
Print the decimal value of each fraction on a new line with  places after the decimal.

Note: This challenge introduces precision problems.
The test cases are scaled to six decimal places,
though answers with absolute error of up to  are acceptable.

Function Description
Complete the plusMinus function in the editor below.
plusMinus has the following parameter(s):

    int arr[n]: an array of integers

Print
Print the ratios of positive, negative and zero values in the array. Each value should be printed on a separate line with  digits after the decimal. The function should not return a value.
"""
from unittest import TestCase


def plus_minus(input_arr):
    counts = [0, 0, 0]
    for i in input_arr:
        if i > 0:  # pos
            counts[0] += 1
        elif i < 0:  # neg
            counts[1] += 1
        else:  # zero
            counts[2] += 1
    return [f'{x/len(input_arr):.6f}' for x in counts]


class TestPlusMinus(TestCase):

    def test_one(self):
        assert plus_minus([-2, -1, 0, 1, 2]) == ['0.400000', '0.400000', '0.200000']

