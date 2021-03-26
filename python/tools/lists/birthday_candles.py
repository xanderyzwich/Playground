"""
Birthday Cake Candles:
You are in charge of the cake for a child's birthday.
You have decided the cake will have one candle for each year of their total age.
They will only be able to blow out the tallest of the candles.
Count how many candles are tallest.
"""

from unittest import TestCase


def candle_count(input_set):
    return sum([1 for x in input_set if x == max(input_set)])


class TestCandleCount(TestCase):

    def test_case(self):
        candle_heights = [3, 2, 1, 3]
        assert candle_count(candle_heights) == 2