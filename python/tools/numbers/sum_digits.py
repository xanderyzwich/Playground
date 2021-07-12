"""
Summing a number’s digits
Write a function named sumDigits which takes a number as input and
returns the sum of the absolute value of each of the number’s decimal digits
"""
from unittest import TestCase


def sum_digits(input_int):
    return sum([int(i) for i in str(input_int) if i in '1234567890'])


def sum_digits_no_strings(input_int):
    temp_int, accumulator = abs(input_int), 0
    while temp_int:
        accumulator += temp_int % 10
        temp_int //= 10
        print(input_int, temp_int, accumulator)
    return accumulator


class TestSumDigits(TestCase):

    data = [
        {
            'arg': 10,
            'expected': 1
        },
        {
            'arg': 99,
            'expected': 18
        },
        {
            'arg': -32,
            'expected': 5
        }
    ]

    def test_sum_digits(self):
        for method in [sum_digits, sum_digits_no_strings]:
            for test in self.data:
                assert method(test['arg']) == test['expected']
