"""
This is just a tinker space for string funcitonality
"""
from unittest import TestCase


def sentence_case(input_str):
    return input_str.capitalize() if not input_str.isupper() else input_str.capitalize() + '!'


class TestSentenceCase(TestCase):

    def test_one(self):
        assert sentence_case('i like cheese') == 'I like cheese'

    def test_two(self):
        assert sentence_case("I LIKE CHEESE") == "I like cheese!"
