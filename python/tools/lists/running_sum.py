"""
Running Sum of 1d Array
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums. This is an array
"""

from unittest import TestCase


def running_sum(input_arr):
    output_arr = []
    for i in range(len(input_arr)):
        output_arr.append(sum(input_arr[:i+1]))
    return output_arr


class TestRunningSum(TestCase):

    data = [
        {
            'arg': [1, 2, 3, 4],
            'expected': [1, 3, 6, 10]
        },
        {
            'arg': [1, 1, 1, 1, 1],
            'expected': [1, 2, 3, 4, 5]
        },
        {
            'arg': [3, 1, 2, 10, 1],
            'expected': [3, 4, 6, 16, 17]
        }
    ]

    def test_set(self):
        for case in self.data:
            assert running_sum(case['arg']) == case['expected']

    
