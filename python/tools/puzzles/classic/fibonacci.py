"""
generate the fibonacci sequence
"""
from functools import lru_cache
from unittest import TestCase
from python.tools.decorators import function_details


@lru_cache(maxsize=2)
def generate_fibonacci(input_int):
    # classic recursion
    return 1 if input_int < 3 else generate_fibonacci(input_int - 1) + generate_fibonacci(input_int - 2)


@function_details
def recursive_wrapper(input_int):
    return generate_fibonacci(input_int)


@function_details
def generate_fibonacci_list(input_int):
    # linear list creation
    output = [1, 1]
    for i in range(2, input_int):
        output.append(output[i - 2] + output[i - 1])
    return output


def get_fibonacci(input_int):
    # return n term from list creation
    return generate_fibonacci_list(input_int)[-1]


class TestFibonacci(TestCase):
    first_ten = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

    def test_recurse(self):
        assert [generate_fibonacci(x) for x in range(1, 11)] == self.first_ten

    def test_list(self):
        assert generate_fibonacci_list(10) == self.first_ten

    def test_get(self):
        assert [get_fibonacci(x) for x in range(1, 11)] == self.first_ten

    def test_compare_list_and_recursive(self):
        n = 50
        listed = generate_fibonacci_list(n)[-1]
        fib = recursive_wrapper(n)
        assert fib == listed
