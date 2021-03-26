"""
Triangular Number Sequence
This Triangular Number Sequence is generated from a pattern of dots that form a triangle. The first 5 numbers of the sequence, or dots, are:
    1, 3, 6, 10, 15
This means that the first triangle has just one dot, the second one has three dots, the third one has 6 dots and so on.
Write a function that gives the number of dots with its corresponding triangle number of the sequence.
"""
from unittest import TestCase


def basic_triangle(side_count):
    count = 0
    for i in range(1, side_count+1):
        count += i
    return count


def triangle(side_count):
    return sum(range(1, side_count + 1))


class TestTriangle(TestCase):

    def test_one(self):
        assert triangle(1) == 1

    def test_six(self):
        assert triangle(6) == 21

    def test_twohundredfifteen(self):
        assert triangle(215) == 23220