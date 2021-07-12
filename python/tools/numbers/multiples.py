"""
Beginner: Array of Multiples
Create a function that takes two numbers as arguments (num, length) and returns an array of multiples of num up to length.
"""
from unittest import TestCase


def array_of_multiples(num, length):
    return [x * num for x in range(1, length + 1)]

class TestMultiples(TestCase):

    def test_seven_five(self):
        assert array_of_multiples(7, 5) == [7, 14, 21, 28, 35]
    def test_twelve_10(self):
        assert array_of_multiples(12, 10) == [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]
    def test_seventeen_six(self):
        assert array_of_multiples(17, 6) == [17, 34, 51, 68, 85, 102]


