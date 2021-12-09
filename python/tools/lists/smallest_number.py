"""
Smallest value of an array

Write a function that can return the smallest value of an array or the index of that value. 
The function's 2nd parameter will tell whether it should return the value or the index.
Assume the first parameter will always be an array filled with at least 1 number and no duplicates. 
Assume the second parameter will be a string holding one of two values: 'value' and 'index'.
 min([1,2,3,4,5], 'value') // => 1
 min([1,2,3,4,5], 'index') // => 0
"""

from unittest import TestCase


def min(numbers, return_type='value'):
    type_value = 'index' != return_type.lower()
    data = list(enumerate(numbers))
    data.sort(key= lambda x: x[1])
    print(data)
    return data[0][1] if type_value else data[0][0]


class TestMin(TestCase):

    def test_value(self):
        assert min([1,2,3,4,5], 'value') == 1

    def test_index(self):
        assert min([1,2,3,4,5], 'index') == 0

    def test_default(self):
        assert min([1,2,3,4,5]) == 1
