"""
Hitting the Jackpot
Create a function that takes in an array (slot machine outcome)
and returns true if all elements in the array are identical, and false otherwise.
The array will contain 4 elements.
"""
from unittest import TestCase


def test_jackpot(input_arr):
    if len(input_arr) != 4:
        raise ValueError("test_jackpot expects an array of exactly 4 elements")
    return input_arr.count(input_arr[0]) == len(input_arr)


class TestJackpotTest(TestCase):

    cases = [
        (["@", "@", "@", "@"], True),
        (["abc", "abc", "abc", "abc"], True),
        (["SS", "SS", "SS", "SS"], True),
        (["&&", "&", "&&&", "&&&&"], False),
        (["SS", "SS", "SS", "Ss"], False)
    ]
    errors = [
        (None, TypeError),
        ([], ValueError),
        (["@"], ValueError),
        (["@", "@"], ValueError),
        (["@", "B"], ValueError),
        (["@", "@", "@"], ValueError),
        (["@", "@", "B"], ValueError),
        (["@", "@", "@", "@", "@"], ValueError),
        (["@", "@", "@", "@", "B"], ValueError),
        (["@", "@", "@", "@", "@", "@"], ValueError),
        (["@", "@", "@", "@", "@", "B"], ValueError)
    ]
    
    def test_values(self):
        for case, expectation in self.cases:
            assert test_jackpot(case) == expectation

    def test_errors(self):
        for case, error in self.errors:
            self.assertRaises(error, test_jackpot, case)

