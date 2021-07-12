"""
Sort y value of array from least to greatest!
In today's challenge, we will sort an array of (x, y) coordinate pairs by their y values from least to greatest.
"""
from unittest import TestCase


def sort_by_y(array):
    return sorted(array, key=lambda x: x[1])


class TestSortY(TestCase):

    def test_one(self):
        arr1 = [(10.1, 15.4), (100.6, 9.8), (8.8, 100.2), (15.6, 15.2)]
        assert sort_by_y(arr1) == [(100.6, 9.8), (15.6, 15.2), (10.1, 15.4), (8.8, 100.2)]

    def test_two(self):
        arr2 = [(10, 1), (15, 1), (20, 0.5), (11, 12)]
        assert sort_by_y(arr2) in [[(20, 0.5), (10, 1), (15, 1), (11, 12)],
                                   [(20, 0.5), (15, 1), (10, 1), (11, 12)]]  # both are ok
