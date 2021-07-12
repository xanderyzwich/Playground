"""
Perform calculations on a string
"""
import re
from unittest import TestCase

func = {
    '^': lambda x, y: x**y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y
}


def evaluate_base(elements):
    working_set = elements
    for operator in func:
        i = 1
        print(f'Perfoming {operator} on {working_set}')
        while operator in working_set:
            # print(working_set)
            if working_set[i] == operator:
                left, right = float(working_set[i - 1]), float(working_set[i + 1])
                result = func[operator](left, right)
                # print(f'{left} {operator} {right} = {result}')
                working_set = [*working_set[:i - 1], str(result), *working_set[i + 2:]]
            else:
                i += 1
    return float(working_set[0])


def evaluate_parens(elements):
    count, _close = 0, len(elements)
    _open = elements.index('(')
    updated_elements = elements[:_open]  # elements before paren
    for i in range(_open, len(elements)):  # lets find the closing peren
        if elements[i] == '(':
            count += 1
        elif elements[i] == ')':
            count -= 1
            if count == 0:
                _close = i + 1
                break
    priority = evaluate(elements[_open + 1:_close - 1])  # omit the outer-most perens
    # print(f'{elements[_open+1:_close-1]} = {priority}')
    updated_elements.append(priority)
    updated_elements.extend(elements[_close:])
    return evaluate(updated_elements)


def evaluate(elements):
    # print(elements)
    if '(' in elements:  # Assuming all parens are matched
        return evaluate_parens(elements)
    else:
        return evaluate_base(elements)


def solve(expression_str):
    fixed = expression_str.replace('(', '( ').replace(')', ' )')
    elements = fixed.split()
    # print(expression_str, fixed, elements)
    return evaluate(elements)


class TestThing(TestCase):
    tests = [
        {'arg': '1 + 2', 'want': 3},
        {'arg': '4 - 1', 'want': 3},
        {'arg': '3 * 2', 'want': 6},
        {'arg': '9 / 3', 'want': 3},
        {'arg': '2 * 2 + 3', 'want': 7},
        {'arg': '2 * (2 + 3)', 'want': 10}
    ]

    def setUp(self) -> None:
        print(f'\n--- Running test: {self._testMethodName} ---')

    def test_one_example(self):
        for t in self.tests:
            print(f'Testing {t} - ')
            result = solve(t['arg'])
            assert result == float(t['want'])
            print('--- PASS ---')

