"""
Array Extender
Write a program that takes in 2 arrays of unequal length,
    and extends the shorter array by duplicating its values
    until the lengths of the first array and second array are equal in length.
Return the array that was modified. If they are equal in length, return nothing:
"""
from unittest import TestCase


def extend_array(arr_1, arr_2):
    len_1, len_2 = len(arr_1), len(arr_2)
    shorter, longer = (arr_1, arr_2) if len_1 < len_2 else (arr_2, arr_1)
    result = [shorter[x % len(shorter)] for x in range(len(longer))]
    return None if len_1 == len_2 else result


class TestExtendArray(TestCase):

    data = [
        {
            'args': ([1, 2, 3, 4, 5], ['a', 'b', 'c']),
            'expected': ['a', 'b', 'c', 'a', 'b']
        },
        {
            'args': ([1, 2, 3], ['Jack', 'Jill', 'Jimmy', 'Jan', 'Juniper', 'Jenn', 'Jane', 'Jeremy', 'Jerome', 'Jess']),
            'expected': [1, 2, 3, 1, 2, 3, 1, 2, 3, 1]
        },
        {
            'args': ([1, 2, 3], [4, 5, 6]),
            'expected': None
        }
    ]

    def test_data(self):
        for case in self.data:
            assert extend_array(*case['args']) == case['expected']
