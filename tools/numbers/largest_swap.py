"""
Largest Swap
Write a function that takes a two-digit number and determines if it's the largest of two possible digit swaps.
"""
from unittest import TestCase


def largest_swap(input_int):
    # return input_int >= int(str(input_int)[::-1])
    return int(str(input_int)[0]) >= int(str(input_int)[1])


class TestLargestSwap(TestCase):

    def test_one(self):
        assert largest_swap(27) is False
        assert largest_swap(43) is True

    def test_two(self):
        assert largest_swap(14) is False
        assert largest_swap(53) is True
        assert largest_swap(99) is True
