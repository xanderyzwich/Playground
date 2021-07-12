"""
FIND INTERSECTION:
Have the function FindIntersection(strArr) read the array of strings stored in strArr which will contain 2 elements:
    the first element will represent a list of comma-separated numbers sorted in ascending order,
    the second element will represent a second list of comma-separated numbers (also sorted).

Your goal is to return a comma-separated string containing the numbers that occur in elements of strArr in sorted order.
If there is no intersection, return the string false.
"""
import re
from unittest import TestCase


def arrays_from_strings(input_str_1, input_str_2):
    return re.split(', ', input_str_1), re.split(', ', input_str_2)


def find_intersection(str_1, str_2):
    arr_1, arr_2 = arrays_from_strings(str_1, str_2)
    intersection = tuple([int(x) for x in arr_1 if x in arr_2])
    return intersection if len(intersection) > 0 else False


class TestIntersection(TestCase):

    def test_one(self):
        assert find_intersection("1, 3, 4, 7, 13", "1, 2, 4, 13, 15") == (1, 4, 13)

    def test_two(self):
        assert find_intersection("1, 3, 9, 10, 17, 18", "1, 4, 9, 10") == (1, 9, 10)

    def test_three(self):
        assert find_intersection("1, 2, 3", "4, 5, 6") is False


def alternate(string_array):
    sets = [set(re.split(', ', x)) for x in string_array]
    result_set = sets[0].intersection(*sets[1:])
    result = sorted([int(x) for x in result_set])
    return False if len(result) == 0 else result[0] if len(result) == 1 else tuple(result) # this feels dirty but works
    # if len(result) == 0:
    #     return False
    # elif len(result) == 1:
    #     return result[0]
    # else:
    #     return tuple(result)


class TestAlternate(TestCase):

    def test_prior(self):
        assert alternate(["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]) == (1, 4, 13)
        assert alternate(["1, 3, 9, 10, 17, 18", "1, 4, 9, 10"]) == (1, 9, 10)
        assert alternate(["1, 2, 3", "4, 5, 6"]) is False

    def test_new(self):
        assert alternate(["1, 2, 3", "1, 2, 3, 4", "1, 3, 4, 5"]) == (1, 3)
        assert alternate(["1, 2, 3", "2, 3, 4", "3, 4, 5"]) == (3)
