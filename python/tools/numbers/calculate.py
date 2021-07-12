"""
Basic Calculator
Create a function that takes two numbers and a mathematical operator + - / * and will perform a calculation with the given numbers.
Notes
If the input tries to divide by 0, return: "Can't divide by 0!"
"""
from unittest import TestCase


def calculator(a, op, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            return "Can't divide by 0!"
        else:
            return a / b


class TestCalc(TestCase):

    def test_calculate(self):
        assert calculator(2, "+", 2) == 4
        assert calculator(2, "*", 2) == 4
        assert calculator(4, "/", 2) == 2
