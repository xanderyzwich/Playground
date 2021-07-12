"""
Hard: Eat Chocolates
Arun recently started eating chocolates. The shopkeeper tells Arun that for every three chocolates Arun eats, he will give him one chocolate in exchange for three chocolate wrappers. Now, Arun is confused about how many chocolates he can eat.Given the total money Arun has and the cost of one chocolate, help Arun figure out how many chocolates he can eat.
** Bonus points for Figure out the invalid inputs and take care of them.
"""
from unittest import TestCase
import re


def count_chocolates(total, cost):
    if '-' in total:
        return "Invalid Input"
    money = ''.join(re.split(r'\D', total)) # get numbers only from string
    charge = ''.join(re.split(r'\D', cost))
    wrappers = bars_eaten = int(money) // int(charge)
    while wrappers >= 3:
        traded_bars = wrappers // 3
        extra_wrappers = wrappers % 3
        wrappers = traded_bars + extra_wrappers
        bars_eaten += traded_bars
    return bars_eaten


class TestChocolateCount(TestCase):
    def test_four_one(self):
        assert count_chocolates("4$", "1$") == 5

    def test_fiftyfive_five(self):
        assert count_chocolates("55   $", "5$") == 16

    def test_sixtyeight_two(self):
        assert count_chocolates("I have 68$", "2$") == 50

    def test_negsixtyeight_two(self):
        assert count_chocolates("I got -68$ from my mom ", "2$") == "Invalid Input"
