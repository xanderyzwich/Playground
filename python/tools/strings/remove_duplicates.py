"""
Steve has a string of lowercase characters in range ascii['a'..'z'].
He wants to reduce the string to its shortest length by doing a series of operations.
In each operation he selects a pair of adjacent lowercase letters that match, and he deletes them.
For instance, the string aab could be shortened to b in one operation.
Steve’s task is to delete as many characters as possible using this method and print the resulting string.
If the final string is empty, print Empty String

TLDR: Given a string, repeatedly remove adjacent pairs of matching characters and then print the reduced result.
"""
from unittest import TestCase
import math


def recursive_remove_duplicates(input_str):
    test_str = input_str
    if len(test_str) > 2:
        midpoint = math.ceil(len(input_str) / 2)
        test_str = remove_duplicates(test_str[:midpoint]) + remove_duplicates(test_str[midpoint:])
    if len(test_str) == 2:
        if test_str[0] == test_str[1]:
            return ''
        else:
            return test_str
    if len(test_str) == 1:
        return test_str


def remove_duplicates(input_str):
    output_str = ''
    for i, char in enumerate(input_str):
        print(i, char)
        if char == input_str[i+1] or char == input_str[i-1]:
            continue
        else:
            output_str += char
    return output_str if len(output_str) > 0 else 'Empty String'


class TestRemoveDuplicates(TestCase):

    def test_remove_duplicates(self):
        assert remove_duplicates('aa') == 'Empty String'
        assert remove_duplicates('ab') == 'ab'
        assert remove_duplicates('aab') == 'b'
        assert remove_duplicates('abb') == 'a'
        assert remove_duplicates('abbc') == 'ac'
