"""
Oddish vs. Evenish
Create a function that determines whether a number is Oddish or Evenish.
A number is Oddish if the sum of all of its digits is odd, and a number is Evenish if the sum of all of its digits is even.
If a number is Oddish, return "Oddish". Otherwise, return "Evenish".
"""
from unittest import TestCase


def oddish_or_evenish(input_number):
    return 'Evenish' if sum([int(s) for s in str(input_number)]) % 2 == 0 else 'Oddish'


class TestOddishEvenish(TestCase):

    def test_forty_three(self):
        assert oddish_or_evenish(43) == 'Oddish'

    def test_three_seven_three(self):
        assert oddish_or_evenish(373) == 'Oddish'

    def test_four_four_three_three(self):
        assert oddish_or_evenish(4433) == 'Evenish'
