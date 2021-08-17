"""
Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.
"""
from unittest import TestCase
import re


def last_word_length(input_str):
    indefinite_whitespace = r'[\W]+'
    clean_input = input_str.strip()
    words = re.split(indefinite_whitespace, clean_input)
    return len(words[-1])


def last_word_length_golf(input_str):
    return len(re.split(r'[\W]+', input_str.strip())[-1])


class TestLastWordLength(TestCase):

    def test_one(self):
        assert(last_word_length_golf('Hello World')) == 5

    def test_two(self):
        assert(last_word_length_golf('   fly me   to   the moon  ')) == 4

    def test_three(self):
        assert(last_word_length_golf('luffy is still joyboy')) == 6
