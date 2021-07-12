"""
You are given an array of non-negative integers.
Let's say you start at the beginning of the array and are trying to advance to the end.
You can advance at most, the number of steps that you're currently on.
Determine whether you can get to the end of the array.

Example,
given the array [1, 3, 1, 2, 0, 1],
    we can go from indices 0 -> 1 -> 3 -> 5,
    so return true.
Given the array [1, 2, 1, 0, 0],
    we can't reach the end,
    so return false.

Write a function that can take an array of arbitrary length
and determine whether the array can be walked to the end as described.
"""

from unittest import TestCase


def can_walk_array(input_arr):
    most_steps = input_arr[0]
    if 0 == most_steps:
        # Can go no further
        return False
    elif len(input_arr) <= most_steps:
        # End is found
        return True

    # You can advance at most, the number of steps that you're currently on.
    for possible_steps in range(1, most_steps+1):
        if can_walk_array(input_arr[possible_steps:]):
            return True
    return False
    # return any([can_walk_array(input_arr[possible_steps:]) for possible_steps in range(1, most_steps+1)])


class TestWalkArray(TestCase):

    data = [
        {
            'arg': [1, 3, 1, 2, 0, 1],
            'expected': True,
        },
        {
            'arg': [1, 2, 1, 0, 0],
            'expected': False,
        },
    ]

    def test_data(self):
        for test_case in self.data:
            print(f'Beginning Test Case {test_case}')
            assert can_walk_array(test_case['arg']) == test_case['expected']
            print(f' Test Case Successful', end='\n\n')
