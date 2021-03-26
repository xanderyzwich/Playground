"""
Fizz Buzz -
Write a program that prints the numbers from 1 to 100.
But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”.
For numbers which are multiples of both three and five print “FizzBuzz”.

As an added complexity, separate the main functionality from the loop so that a main loop can handle counting,
and a separate function returns the bit to be printed.
"""

from unittest import TestCase


def fizz_buzz(input_int):
    output = ''
    input = int(input_int)
    if input % 3 == 0:
        output += 'Fizz'
    if input % 5 == 0:
        output += 'Buzz'
    if len(output) == 0:
        return input
    return output


def fizz_buzz_golf(input_int):
    return 'FizzBuzz' if input_int % 3 == 0 and input_int % 5 == 0 else 'Fizz' if input_int % 3 == 0 else 'Buzz' if input_int % 5 == 0 else input_int


def fizz_buzz_love(input_int):
    divisible = lambda x: input_int % x == 0
    return [input_int, 'Fizz', 'Buzz', 'FizzBuzz'][divisible(3) + 2 * divisible(5)]


if __name__ == '__main__':
    for i in range(1, 100):
        print(fizz_buzz_golf(i))

function = fizz_buzz_love


class TestFizzBuzz(TestCase):
    data = {
        1: 1,
        3: 'Fizz',
        5: 'Buzz',
        15: 'FizzBuzz'
    }

    def test_one(self):
        for k, v in self.data.items():
            assert function(k) == v

    def test_two(self):
        actual = [function(x) for x in range(1, 16)]
        expected = [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz']
        assert actual == expected

    def test_threes(self):
        for x in range(3, 300, 3):
            assert function(x) == 'FizzBuzz' if x % 15 == 0 else 'Fizz'

    def test_fives(self):
        for x in range(5, 500, 5):
            assert function(x) == 'FizzBuzz' if x % 15 == 0 else 'Buzz'

    def test_fifteens(self):
        for x in range(15, 1500, 15):
            assert function(x) == 'FizzBuzz'
