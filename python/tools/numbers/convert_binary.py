"""
Convert a Number to Base-2
Create a function that returns a base-2 (binary) representation of a base-10 (decimal) string number. To convert is simple: ((2) means base-2 and (10) means base-10) 010101001(2) = 1 + 8 + 32 + 128.
Going from right to left, the value of the most right bit is 1, now from that every bit to the left will be x2 the value, value of an 8 bit binary numbers are (256, 128, 64, 32, 16, 8, 4, 2, 1).
"""
from unittest import TestCase


def binary(decimal):
    current_decimal = int(decimal)
    next_binary_value = 2
    output_string = ""

    while current_decimal > 0:
        output_string = str(current_decimal % next_binary_value) + output_string
        current_decimal = current_decimal // next_binary_value

    return output_string


class TestBinary(TestCase):

    def test_one(self):
        assert binary(1) == "1"
        # 1*1 = 1

    def test_five(self):
        assert binary(5) == "101"
        # 1*1 + 1*4 = 5

    def test_ten(self):
        assert binary(10) == "1010"
        # 1*2 + 1*8 = 10

    def test_bigger_number(self):
        assert binary(8675309) == "100001000101111111101101"
