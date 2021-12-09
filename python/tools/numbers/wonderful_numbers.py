"""
You are given a string num, representing a large integer, and an integer k.
We call some integer wonderful if it is a permutation of the digits in num and is greater in value than num. There can be many wonderful integers. However, we only care about the smallest-valued ones.

For example, when num = "5489355142":
    The 1st smallest wonderful integer is "5489355214".
    The 2nd smallest wonderful integer is "5489355241".
    The 3rd smallest wonderful integer is "5489355412".
    The 4th smallest wonderful integer is "5489355421".

Return the minimum number of adjacent digit swaps that needs to be applied to num to reach the kth smallest wonderful integer.
The tests are generated in such a way that kth smallest wonderful integer exists.

Constraints:
2 <= num.length <= 1000
1 <= k <= 1000
num only consists of digits.
"""

from unittest import TestCase


def get_wonderful_numbers(given_str):
    """
    Return all of the wonderful numbers for the given numeric string
    """
    wonderfuls = []
    # get permutations
    # add permutation to wonderfuls if greater than given_str
    return wonderfuls


def count_swaps(str_one, str_two):
    """
    return the minimum number of swaps necessary to change str_one into str_two
    """
    left, right = '', ''
    swap_count = 0
    # iterate strings and find differences. store non-matching characters in left and right
    # evaluate, and count matching pairs that can be swapped
    return swap_count


def pick_a_wonderful_number(given_str, k):
    """
    Return the k'th smallest wonderful number
    """
    wonderful_numbers = get_wonderful_numbers(given_str)
    wonderful_numbers.sort()
    wanted = wonderful_numbers[k-1]
    return wanted


def necessary_swaps_for_picked_wonderful_number(given_str, k):
    """
    Return the # of swaps needed to transform given_str into k'th smallest wonderful number
    """
    destination = pick_a_wonderful_number(given_str, k)
    return count_swaps(given_str, destination)


class TestWonderfulNumbers(TestCase):

    def test_one(self):
        num = '5489355142'
        assert pick_a_wonderful_number(num, 1) == '5489355214'
        assert pick_a_wonderful_number(num, 2) == '5489355241'
        assert pick_a_wonderful_number(num, 3) == '5489355412'
        assert pick_a_wonderful_number(num, 4) == '5489355421'

    def test_two(self):
        assert pick_a_wonderful_number('11112', 4) == '21111'

    def test_three(self):
        assert  pick_a_wonderful_number('00123', ) == '00132'

