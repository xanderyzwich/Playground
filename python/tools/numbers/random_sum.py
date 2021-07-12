"""
Definite Sum from randoms:
Create a function that takes number, and the number of numbers you want you function to use which sum up to that number.
The output array should contain numbers that sum up to the first number. This one will be
"""
from random import randint
from unittest import TestCase


def definite_sum(total, count):
    big_total = total * 10  # I we can allow for 1 place past the decimal
    results = []
    while len(results) < count - 1:
        room_left = big_total - sum(results)
        buffer = count - len(results)
        thing = randint(1, room_left - buffer)
        results.append(thing)
        print(f'Room_left = {room_left}, buffer =  {buffer}, thing = {thing}, results = {results}')
    results.append(big_total - sum(results))
    return sorted([x/10 for x in results])


def helper(total, count):
    result = definite_sum(total, count)
    print(f'Testing - Total= {total}, Count = {count} and result= {result}')
    print(len(result), sum(result))
    return len(result) == count and sum(result) == total


class TestSum(TestCase):

    def test_sum_one(self):
        assert helper(10, 3)

    def test_sum_two(self):
        assert helper(1, 4)

    def test_sum_three(self):
        assert helper(5, 5)

    def test_thousand(self):
        for a in range(1000):
            self.test_sum_one()


