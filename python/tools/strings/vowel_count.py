"""
How Many Vowels?
Create a function that takes a string and returns the number (count) of vowels contained within it.

Notes
    a, e, i, o, u are considered vowels (not y).
    All test cases are one word and only contain letters.
"""
from unittest import TestCase
import re


def count_vowels(input_str):
    # return sum([1 for x in input_str.lower() if x in 'aeiou'])
    return len(re.findall("[aeiou]{1}", input_str.lower()))

class TestVowelCount(TestCase):

    def test_vowel_count(self):
        assert count_vowels("Celebration") == 5
        assert count_vowels("Palm") == 1
        assert count_vowels("Prediction") == 4
