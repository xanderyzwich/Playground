"""
Intermediate
Find the longest number of multicharacter repeats in a string given the repeat string.
Intermediate - Hard
Find the longest number of multicharacter repeats in a string by dynamically determining the repeat for each string.
"""
import re
from unittest import TestCase


def count_repeats(input_str, substring):
    count = 0
    for set in re.split(f'[^{substring}]', input_str):
        this_count = len(re.findall(substring, set))
        count = this_count if this_count > count else count
    return count


def count_most_repeats(input_str):
    count = 0
    for i in range(len(input_str) - 1):
        for j in range(i+1, len(input_str) + 1):
            this_count = count_repeats(input_str, input_str[i:j])
            count = this_count if this_count > count else count
    return count


class TestRepeats(TestCase):

    def test_count(self):
        assert count_repeats('ABCABCABCDDABCABCFFABCABCABCABC', 'ABC') == 4

    def test_find(self):
        assert count_most_repeats('DEFDEFAADEFDEFDEFDEF') == 4
