"""
Converting Objects to Arrays
Write a function that converts an object into an array,
where each element represents a key-value pair in the form of an array.
"""

from unittest import TestCase


def dict_to_list(data):
    return [[k, v] for k, v in data.items()]


class TestDictToList(TestCase):

    def test_one(self):
        assert dict_to_list({'a': 1, 'b': 2}) == [["a", 1], ["b", 2]]

    def test_two(self):
        assert dict_to_list({'shrimp': 15, 'tots': 12}) == [["shrimp", 15], ["tots", 12]]

    def test_three(self):
        assert dict_to_list({}) == []
