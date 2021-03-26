"""
I was actually given a coding question in an interview yesterday.

effectively, given a sorted array of random integers (positive and negative),
return the magic index where the value at that particular index matches the index.
if no match is found in the array, return -1. (Follow up, how fast is your solution? How can you improve it?)
"""
from math import floor, ceil
from unittest import TestCase


def magic_index(input_arr):
    pass


def basic_check(input_arr):
    for i, element in enumerate(input_arr):
        if i == element:
            return i
    return -1


def binary_search_check(input_arr):
    low, high = 0, len(input_arr) - 1
    mid = high
    if low == input_arr[low]:
        return low
    if high == input_arr[high]:
        return high
    while True:
        compare = input_arr[mid] - mid
        if 0 == compare:
            return mid
        low, mid, high = move(low, mid, high, compare)
        if mid in (low, high):
            return -1


def move(low, mid, high, compare):
    print('move:', low, mid, high, compare)
    return move_left(low, mid) if compare < 0 else move_right(mid, high)


def move_left(low, mid):
    print('move_left:', low, mid)
    out_low, out_high = low, mid
    out_mid = out_low + floor(out_high - out_low)
    return out_low, out_mid, out_high


def move_right(mid, high):
    print('move_right:', mid, high)
    out_low, out_high = mid, high
    out_mid = out_low + ceil(out_high - out_low)
    return out_low, out_mid, out_high



class TestMagicIndex(TestCase):

    data = [
        {
            'arg': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
            'expected': 0
        },
        {
            'arg': [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
            'expected': -1
        },
        {
            'arg': [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400],
            'expected': -1
        },
        {
            'arg': [-1, 1],
            'expected': 1
        }
    ]

    def test_generate_data(self):
        print(list(range(20)))
        print(list(range(21, 41)))
        print([i**2 for i in range(1, 21)])

    def test_magic_index(self):
        for case in self.data:
            assert binary_search_check(case['arg']) == case['expected']
