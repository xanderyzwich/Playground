"""
Zip It, If You Can?
Given an array of women and an array of men, either:

    Return "sizes don't match" if the two arrays have different sizes.
    If the sizes match, return an array of pairs,
        with the first woman paired with the first man,
        second woman paired with the second man, etc.
"""
from unittest import TestCase


def zip_it(list_one, list_two):
    if len(list_one) != len(list_two):
        return "sizes don't match"
    return [list(x) for x in zip(list_one, list_two)]


class TestZipIt(TestCase):

    data = [
        (["Elise", "Mary"], ["John", "Rick"], [["Elise", "John"], ["Mary", "Rick"]]),
        (["Ana", "Amy", "Lisa"], ["Bob", "Josh"], "sizes don't match"),
        (["Ana", "Amy", "Lisa"], ["Bob", "Josh", "Tim"], [["Ana", "Bob"], ["Amy", "Josh"], ["Lisa", "Tim"]])
    ]

    def test_zip_it(self):
        for one, two, result in self.data:
            print(one, two, result, zip_it(one, two))
            assert zip_it(one, two) == result
