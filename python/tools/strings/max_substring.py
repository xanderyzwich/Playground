"""
This is an INTERMEDIATE challenge:Given a string, find the longest substring based on the following conditions:

1. The substring must be the longest one of all the possible substring in the given string.
2. There must not be any repeating characters in the substring.
3. If there is more than one substring satisfying the above two conditions, then print the substring which occurs first.
4. If there is no substring satisfying all the aforementioned conditions then print -1.
"""
from unittest import TestCase


def find_substring(input_string):
    winner = ''
    for i in range(len(input_string)):  # first char
        for j in range(len(input_string)+1):  # not char after cut
            candidate = input_string[i:j]
            if len(candidate) > len(winner):
                if no_duplicate(candidate):
                    winner = candidate
    return winner if len(winner) > 1 else -1


def no_duplicate(input_string):
    for i in range(len(input_string)):
        if input_string[i] in input_string[i+1:]:
            return False
    return True


class TestSubstring(TestCase):

    def test_rejoice(self):
        assert find_substring('rejoice') == 'rejoic'

    def test_juice(self):
        assert find_substring('juice') == 'juice'

    def test_aaaa(self):
        assert find_substring('aaaa') == -1

    def test_blacklist(self):
        assert find_substring('blacklist')
