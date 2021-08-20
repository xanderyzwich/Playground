"""
Short Long Short
Given 2 strings, a and b, return a string of the form short+long+short,
    with the shorter string on the outside and the longer string on the inside.
The strings will not be the same length, but they may be empty ( length 0 ).
"""
from unittest import TestCase


def short_long_short(first, second):
    first_longer = len(first) > len(second)
    long, short = (first, second) if first_longer else (second, first)
    return f'{short}{long}{short}'


def short_long_short_golf(first, second):
    return f'{second}{first}{second}' if len(first) > len(second) else f'{first}{second}{first}'


class TestFunction(TestCase):
    def test_one(self):
        assert short_long_short('1', '22') == '1221'

    def test_two(self):
        assert short_long_short('22', '1') == '1221'
