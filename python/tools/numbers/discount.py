"""
Find the Discount
Create a function that takes two arguments:
    the final price and the discount percentage as integers and returns the final price after the discount.
"""
from unittest import TestCase


def discount(price, percentage):
    return price * (1 - percentage/100)


class TestDiscount(TestCase):

    data = [  # (price before, discount %, result)
        (1500, 50, 750),
        (89, 20, 71.2),
        (100, 75, 25)
    ]

    def testDiscount(self):
        for price, percent, result in self.data:
            assert discount(price, percent) == result
