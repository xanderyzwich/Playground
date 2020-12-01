"""
Sort by String Length
Create a function that returns an array of strings sorted by length in ascending order.
"""
from unittest import TestCase


def sort_by_length(input_list):
    return sorted(input_list, key=len)


class TestStringSortLength(TestCase):
    def test_one(self):
        assert sort_by_length(["a", "ccc", "dddd", "bb"]) == ["a", "bb", "ccc", "dddd"]

    def test_two(self):
        assert sort_by_length(["apple", "pie", "shortcake"]) == ["pie", "apple", "shortcake"]

    def test_three(self):
        assert sort_by_length(["may", "april", "september", "august"]) == ["may", "april", "august", "september"]

    def test_empty(self):
        assert sort_by_length([]) == []
