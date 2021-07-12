"""
Max Subset Sum, No Adjacent:
    Write a function that takes in an array of positive integers and
    returns the maximum sum of non-adjacent elements in the array.
    If the input array is empty, the function should return 0.
Business Rules / Errata:
    Don't sort the input array
    You should return a Maximum sum that can be derived from any combination of non-adjacent numbers,
    even if that comes from a single value in the array
    (consider the sum of an array of length 1 == the numeric in the array).
"""

from unittest import TestCase


def max_subset_sum_no_adjacent(input_set):
    input_length = len(input_set)

    # special cases first to short circuit
    if input_length < 1:
        return 0
    elif input_length <= 2:
        return max(input_set)

    max_sum = 0
    for i, i_val in enumerate(input_set[:-1]):
        max_sum = max([max_sum, i_val + max_subset_sum_no_adjacent(input_set[i + 2:])])
    return max_sum


def dennis_solution(array):
    if not array:
        return 0
    elif len(array) == 1:
        return array[0]
    initializer = array[0]
    guess = max(array[0], array[1])
    for i in range(2, len(array)):
        current = max(guess, initializer + array[i])
        # update vals
        initializer = guess
        guess = current
    print(guess)
    return guess

class TestThat(TestCase):
    data = [
        {'input': [75, 105, 120, 75, 90, 135],
         'output': 330,  # 75 + 120 + 135
         },
        {'input': [],
         'output': 0,
         },
        {'input': [1],
         'output': 1,
         },
        {'input': [1, 2],
         'output': 2,  # 2 should not be summed with 1 because they are adjacent, and 2 is the highest value
         },
        {'input': [1, 2, 3],
         'output': 4,  # 1 + 3
         },
        {'input': [1, 15, 3],
         'output': 15,  # This is a tricky one, since 15 is greater than 1 + 3, 15 is the max subset sum
         },
        {'input': [7, 10, 12, 7, 9, 14],
         'output': 33,  # 7 + 12 + 14
         },
        {'input': [4, 3, 5, 200, 5, 3],
         'output': 207,  # 4 + 200 + 3 // (array[0] + array[3] + array[5]), again this is tricky
         },

        {'input': [10, 5, 20, 25, 15, 5, 5, 15],
         'output': 60,  # 10 + 20 + 15 + 15 // (array[0] + array[2] + array[4] + array[7])
         },

        {'input': [10, 5, 20, 25, 15, 5, 5, 15, 3, 15, 5, 5, 15],
         'output': 90,  # 10 + 20 + 15 + 15 + 15 + 15
         # // (array[0] + array[2] + array[4] + array[7] + array[9] + array[12])
         },
        {'input': [100, 3, 1, 1, 1, 1], 'output': 102},
    ]

    def test_data(self):
        for test in self.data:
            function_call = max_subset_sum_no_adjacent
            # function_call = dennis_solution
            assert function_call(test['input']) == test['output']
