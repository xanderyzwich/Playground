"""
Given a string, Encode any stretch of characters to an encoding of <char><count>.
This should account for any character, and should encode upper and lower case differently.
"""
from unittest import TestCase
from tools.decorators import function_details

@function_details
def encode(plaintext):
    ciphertext = ''
    current, count = '', 0
    for p in plaintext:
        if p == current:
            count += 1
        else:
            ciphertext += f'{current}{count}'if len(current)>0 else ''
            current, count = p, 1
    ciphertext += f'{current}{count}'
    return ciphertext


class TestEncode(TestCase):
    def test_one(self):
        assert encode('AABBAACCDaaTTttcc') == 'A2B2A2C2D1a2T2t2c2'

    def test_two(self):
        assert encode('ABCAAA') == 'A1B1C1A3'

    def test_three(self):
        assert encode('TTGGCCGTCGT') == 'T2G2C2G1T1C1G1T1'

    def test_four(self):
        assert encode('!!..??%%..') == '!2.2?2%2.2'
