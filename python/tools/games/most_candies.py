"""
Kids With the Greatest Number of Candies
Given the array candies and the integer extraCandies, where candies[i] represents the number of candies that the ith kid has.
For each kid check if there is a way to distribute extraCandies among the kids such that he or she can have the greatest
number of candies among them.
Notice that multiple kids can have the greatest number of candies.
"""
from unittest import TestCase


def check(candies, extraCandies):
    all_is_well = [2 <= len(candies) <= 100]
    for c in candies:
        all_is_well.append(1 <= c <=100)
    all_is_well.append(1 <= extraCandies <= 50)
    if not all(all_is_well):
        raise ValueError


def most_candies(candies, extraCandies):
    check(candies, extraCandies)
    most = max(candies)
    return [most <= x + extraCandies for x in candies]


class TestCandies(TestCase):

    data = [
        {
            'args': {
                'candies': [2, 3, 5, 1, 3],
                'extraCandies': 3
            },
            'expected': [True, True, True, False, True]
        },
        {
            'args': {
                'candies': [4, 2, 1, 1, 2],
                'extraCandies': 1
            },
            'expected': [True, False, False, False, False]
        },
        {
            'args': {
                'candies': [12, 1, 12],
                'extraCandies': 1
            },
            'expected': [True, False, True]
        }
    ]

    def test_set(self):
        for case in self.data:
            assert most_candies(**case['args']) == case['expected']

    def test_negatives(self):
        # Test the constraints for candies.length
        self.assertRaises(ValueError, check, [1], 1)
        self.assertRaises(ValueError, check, list(range(102)), 1)

        # Test value of candies
        self.assertRaises(ValueError, check, [0 for _ in range(10)], 1)
        self.assertRaises(ValueError, check, list(range(90, 110)), 1)

        # Test extraCandies count
        self.assertRaises(ValueError, check, list(range(10)), 0)
        self.assertRaises(ValueError, check, list(range(10)), 51)
