"""
# Sum of Squares

Given a positive integer `n`, find the smallest number of squared integers which sum to `n` (i.e. `n = x² + y²` should yield `2`).

## Business Rules/Errata

- Any attempt to provide non-integer, non-positive input should return an error.
- Return only the count of squared integers that sum to `n`, not the list of integers.
- Remember that 1² = 1.

## Examples

```
count_squared_addends(13);  // 2
count_squared_addends(27);  // 3
```

- For `n` = 13: 3² + 2² = 9 + 4 = 13
- For `n` = 27:
    - 3² + 3² + 3² =   9 + 9 + 9 = 27
    - 5² + 1² + 1² = 25 + 1 + 1 = 27
"""
import math
from unittest import TestCase
from python.tools.decorators import function_details


@function_details
def count_squared_addends_loop(input_int):
    """
    Doesn't find optimal solution.
    Assumes that the highest number will be involved in best solution.
    """
    options = [(v, v**2) for v in range(1, math.floor(math.sqrt(input_int))+1)]
    print(options)
    addends = []
    remainder = input_int
    index = -1
    while remainder > 0:
        value, square = options[index]
        if square <= remainder:
            print(index, remainder, value, square, remainder - square)
            addends.append(value)
            remainder -= square
        else:
            index -= 1
    return len(addends)


def count_squared_addends_recursive(input_int):
    """
    Doesn't return for 84 test case
    """
    options = [(v, v**2) for v in range(1, math.floor(math.sqrt(input_int)) + 1)]
    options.sort(reverse=True)
    solutions = []
    # print(options)
    for value, square in options:
        if square == input_int:
            return 1
        elif square < input_int:
            count = count_squared_addends_recursive(input_int-square)
            solutions.append(count)
    return min(solutions) + 1


# @function_details
def count_squared_addends_max_four(input_int):
    """
    Due to Lagrange's four square theorem all numbers are representable as the sum of at most 4 squares
    https://en.wikipedia.org/wiki/Lagrange%27s_four-square_theorem
    """
    options = list(range(1, math.floor(math.sqrt(input_int)) + 1))
    options.sort(reverse=True)
    solutions = []
    i = 0
    while i <= len(options) - 1:
        i_square = options[i]**2
        # print(f'i = {i}, i**2 = {i_square}')
        if input_int == i_square:
            return 1  # Skipping the append to solutions as there can't be a better solution

        j = i
        while (j <= len(options) - 1):
            j_square = options[j]**2
            # print(f'j = {j}, i**2 = {j_square}')
            if input_int == i_square + j_square:
                solutions.append(2)
                j += 1
                continue

            k = j
            while k <= len(options) - 1:
                k_square = options[k] ** 2
                # print(f'k = {k}, i**2 = {k_square}')
                if input_int == i_square + j_square + k_square:
                    solutions.append(3)

                k += 1
            j += 1
        i += 1

    # print(solutions)
    if len(solutions) == 0:
        return 4
    return min(solutions)


class TestCountSquaredAddends(TestCase):
    data = [
        (13, 2),
        (27, 3),
        (144, 1),
        (85, 2),
        (84, 3),
    ]

    def testData(self):
        for arg, expected in self.data:
            print(f'Testing arg:{arg: 4} expecting:{expected: 2}', end='')
            assert count_squared_addends_max_four(arg) == expected
            print(f'  PASSED!')
