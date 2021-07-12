"""
No Conditionals?
Write a function that returns 0 if the input is 1, and returns 1 if the input is 0.
"""
from unittest import TestCase


def flip(input_bit):
    return (input_bit + 1) % 2


class TestFlip(TestCase):

    def test_zero(self):
        assert flip(0) == 1

    def test_one(self):
        assert flip(1) == 0