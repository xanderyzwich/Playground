"""
Implement a function isMember.
It takes an input list of strings called words eg. ["foo", "bar", "baz"]
    and an input string called query eg. "foo",

It should return true if a query matches any string in words.

If a query includes * it's considered a wildcard.
    ie. it matches exactly one character of any value at the current index of the string.

You may assume that the input will not contain empty strings or empty lists.
"""

from unittest import TestCase
import re


def is_member(input_list, query_str):
    print(f'Looking for {query_str} in {input_list}')
    for word in input_list:
        match = True
        for i, char in enumerate(query_str):
            if char not in ['*', word[i]]:
                match = False
                break
        if match:
            print('Found')
            return True
    print('Not Found')
    return False


class TestIsMember(TestCase):

    data = [
        {
            'args': {
                'words': ["bar", "foo", "baz"],
                'query': "foo"
            },
            'expected': True,
        },
        {
            'args': {
                'words': ["bar", "foo", "baz"],
                'query': "cat"
            },
            'expected': False,
        },
        {
            'args': {
                'words': ["bar", "foo", "baz"],
                'query': "**z"
            },
            'expected': True,
        },
    ]

    def test_data(self):
        for case in self.data:
            args, expected = case['args'].values(), case['expected']
            assert is_member(*args) == expected


def alternate_is_member(wordlist):
    def contains(query):
        clean = query.replace("*", ".")
        return any([re.search(clean, word) for word in wordlist])
    return contains


class TestAlternate(TestCase):
    words = ["bar", "foo", "baz"]
    tests = {
        'foo': True,
        'cat': False,
        '**z': True,
    }

    def test_alternate_data(self):
        fn = alternate_is_member(self.words)
        assert all([fn(x) == y for x, y in self.tests.items()])
