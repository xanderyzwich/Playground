"""
Combine Alternating Lists
Write a method that combines two lists by alternatingly taking elements.
For example: given the two lists [a, b, c] and [1, 2, 3]
the method should return [a, 1, b, 2, c, 3]
"""

from unittest import TestCase


def combine_alternating(input_a, input_b):
    list_a, list_b = input_a[::-1], input_b[::-1]
    list_c = []
    for i in range(max(len(input_a), len(input_b))):
        if i < len(input_a):
            list_c.append(list_a.pop())
        if i < len(input_b):
            list_c.append(list_b.pop())
    return list_c


def combine_alternating_alternate(input_a, input_b):
    import itertools
    # return [y for x in itertools.zip_longest(input_a, input_b) for y in x if y is not None]
    return [y for x in itertools.zip_longest(input_a, input_b) for y in x if y]


class TestCombineAlternating(TestCase):
    a, b = ['a', 'b', 'c', 'd', 'e'], ['1', '2', '3']

    def test_data(self):
        print(combine_alternating(self.a, self.b))
        print(combine_alternating_alternate(self.a, self.b))
