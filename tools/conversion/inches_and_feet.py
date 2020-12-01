"""
Inches to Feet
Create a function that accepts a measurement value in inches and returns the equivalent of the measurement value in feet.
"""
from unittest import TestCase


def inches_to_feet(inches):
    return inches // 12, inches % 12


def feet_to_inches(feet, inches=0):
    return feet * 12 + inches


class TestInchesAndFeet(TestCase):

    test_cases = {
        324: (27, 0),
        12:  (1,  0),
        36:  (3,  0),
        13:  (1,  1)
    }

    def test_inches_to_feet(self):
        for inches, feet_and_inches in self.test_cases.items():
            assert inches_to_feet(inches) == feet_and_inches

    def test_feet_to_inches(self):
        for inches, feet_and_inches in self.test_cases.items():
            assert feet_to_inches(*feet_and_inches) == inches

    def test_roundtrip_one(self):
        for inches, feet_and_inches in self.test_cases.items():
            assert feet_and_inches == inches_to_feet(feet_to_inches(*feet_and_inches))

    def test_roundtrip_two(self):
        for inches, feet_and_inches in self.test_cases.items():
            assert inches == feet_to_inches(*inches_to_feet(inches))


