"""
Dashed Vowels:
Create a function that takes a string and returns dashes on the left and right side of every vowel (a e i o u).
"""
from unittest import TestCase


def dashed(input_str):
    output = ''
    for char in input_str:
        output += f'-{char}-' if char in 'aAeEiIoOuU' else f'{char}'
    return output


class TestDashed(TestCase):

    def test_edabit(self):
        assert dashed('Edabit') == '-E-d-a-b-i-t'

    def test_carpe_diem(self):
        assert dashed('Carpe Diem') == 'C-a-rp-e- D-i--e-m'

    def test_fight_for_your_right_to_party(self):
        assert dashed('Fight for your right to party!') != 'F-i-ght f-o-r y-o--u-r r-i-ght t-o- p-a-rty!'
