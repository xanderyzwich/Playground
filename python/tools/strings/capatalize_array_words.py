"""
Capitalize the Names
Create a function that takes an array of names and returns an array where only the first letter of each name is capitalized.

Notes
    Don't change the order of the original array.
    Notice in the second example above, "MABELLE" is returned as "Mabelle".
"""
from unittest import TestCase


def normalize(input_str):
    return input_str[0].upper() + input_str[1:].lower()


def cap_me(input_arr):
    return [normalize(s) for s in input_arr]


class TestCap(TestCase):

    def test_one(self):
        assert cap_me(["mavis", "senaida", "letty"]) == ["Mavis", "Senaida", "Letty"]

    def test_two(self):
        assert cap_me(["samuel", "MABELLE", "letitia", "meridith"]) == ["Samuel", "Mabelle", "Letitia", "Meridith"]

    def test_three(self):
        assert cap_me(["Slyvia", "Kristal", "Sharilyn", "Calista"]) == ["Slyvia", "Kristal", "Sharilyn", "Calista"]
