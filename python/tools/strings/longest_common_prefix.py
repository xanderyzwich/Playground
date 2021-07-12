"""
Longest Common Prefix
Write a function to find the longest common prefix string among an array of strings.
If there is no common prefix, return an empty string "".
"""
from unittest import TestCase
from numpy import array, transpose


def __longest_of_two(str1, str2):
    common = ''
    for i in range(min(len(str1), len(str2))):
        if str1[i] != str2[i]:
            break
        common += str1[i]
    return common


def longest_common_prefix(strings_arr):  # recursive solution
    if 2 == len(strings_arr):
        return __longest_of_two(*strings_arr)
    else:
        return __longest_of_two(strings_arr[0], longest_common_prefix(strings_arr[1:]))


def dennis_kennetz(arr):  # Dennis' solution
    if len(arr) == 1:
        return arr[0]
    else:
        result = ""
        arr.sort()
        for i in range(len(arr[0])):
            if arr[0][i] == arr[-1][i]:
                result += arr[0][i]
            else:
                break
        return result


def tweak_dennis_kennetz(arr):  # Dennis' solution with my tweaks
    if len(arr) == 1:
        return arr[0]
    else:
        result = ""
        first, *_, last = sorted(arr)
        for i in range(len(first)):
            if first[i] == last[i]:
                result += first[i]
            else:
                break
        return result


def numpy_lcp(strings_arr):
    common = ''
    length = max(len(s) for s in strings_arr)  # longest string length
    same_len = [list(s.ljust(length)) for s in strings_arr]  # strings must be same length
    arr = transpose(array(same_len))  # transpose so that first letters are first row
    # print(arr)
    for i in arr:
        if 1 != len(set(i)):
            break
        common += i[0]
    return common


class TestLCP(TestCase):

    data = [
        {
            'arg': ['flower', 'flow', 'flight'],
            'expected': 'fl'
        },
        {
            'arg': ['dog', 'racecar', 'car'],
            'expected': ''
        }
    ]

    def test_longest_common_prefix(self):
        for case in self.data:
            assert tweak_dennis_kennetz(case['arg']) == case['expected']

    def test_all_funcs(self):
        for func in [longest_common_prefix, dennis_kennetz, tweak_dennis_kennetz, numpy_lcp]:
            for case in self.data:
                print(f'Function: {func.__name__.ljust(25)} Arg: {str(case["arg"]).ljust(30)} Expected: {case["expected"]}')
                assert func(case['arg']) == case['expected']
