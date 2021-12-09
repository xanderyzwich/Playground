"""
The 24 Game

The `24` game is played as follows. 
You are given a list of four integers, 
    each between 1 and 9, in a fixed order. 
By placing the operators +, -, *, and / between the numbers, 
    and grouping them with parentheses, determine whether it is possible to reach the value `24`.

For example, 
given the input [5, 2, 7, 8], 
you should return True, since (5 * 2 - 7) * 8 = 24.

Write a function that plays the `24` game.

## Business Rules/Errata

- Your input will always consist of an array of four integers. 
    These integers do not all need to be positive.
- Your function should return a boolean value indicating whether the input can be combined to produce `24`. 
    You do not need to produce the formula that yields `24`.
- The results of any division operation should be rounded to the nearest integer. 
    So, `3 / 2 = 2`, not `3 / 2 = 1`.
- The result of division by zero should be zero, not undefined.
"""
from unittest import TestCase
from itertools import product

def group_operands(statement_list):
    """
    input should have operands and operators as strings in a list
    elements 0, 2, 4, 6 should be numbers (operands)
    elements 1, 3, 5 should be operators
    """
    opening, closing = '(', ')'
    return [
        ['1', '+', '2', '-', '3', '*', '4']
        [opening, *statement_list[:3], closing, *statement_list[3:]],  # (1+2)-3*4
        [opening, *statement_list[:5], closing, *statement_list[5:]],  #  (1+2-3)*4
        [*statement_list[:2], opening, *statement_list[2:5], closing, *statement_list[5:]],  #  1+(2-3)*4
        [*statement_list[:2], opening, *statement_list[2:], closing])  #  1+(2-3*4)
        [*statement_list[:4], opening, *statement_list[4:], closing])  #  1+2-(3*4)
        [opening, *statement_list[:3], closing, statement_list[3], opening, *statement_list[4:], closing]  #  (1+2)-(3*4)
    ]

def play(array):
    pass


if __name__ == '__main__':
    print(group_operands['1', '+', '2', '-', '3', '*', '4'])


class TestPlay(TestCase):
    def setUp(self):
        self.prod_sub_prod = [5, 2, 7, 8]
        self.addition = [2, 4, 8, 10]
        self.subtraction = [27, 1, 1, 1]
        self.add_prod_add = [5, 0, 4, 4]
        self.div_roundup = [47, 2, 0, 0]
        self.div_rounddown = [1, 1, 73, 3]
        self.fail = [1, 5, 7, 19]

    def test_addition(self):
        self.assertTrue(play(self.addition), "2 + 4 + 8 + 10 = 24 -> True")

    def test_subtraction(self):
        self.assertTrue(play(self.subtraction), "27 - 1 - 1 - 1 = 24 -> True")

    def test_div_roundup(self):
        self.assertTrue(play(self.div_roundup), "47 / 2 + 0 + 0 = 23.5 -> 24 -> True")

    def test_fail(self):
        self.assertFalse(play(self.fail), "1 ? 5 ? 7 ? 19 != 24 -> False")

    # def test_prod_sub_prod(self):
    #     self.assertTrue(play(self.prod_sub_prod), "(5 * 2 - 7) * 8 = 24 -> True")

    # def test_add_prod_add(self):
    #     self.assertTrue(play(self.add_prod_add), "(5 + 0) * 4 + 4 = 24 -> True")

    # def test_div_rounddown(self):
    #     self.assertTrue(play(self.div_rounddown), "1 - 1 + (73 / 3) = 24.33 -> 24 -> True")

    def tearDown(self):
        pass