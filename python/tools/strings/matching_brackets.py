"""
Closing Brackets
    Given a string containing round, curly, and square open and closing brackets,
    return whether the brackets are balanced (well-formed).
    The string may also contain other characters.
    Raise an error (or otherwise alert the user) if the string doesn't contain any round, curly, or square brackets.
"""
from unittest import TestCase

opening_brackets, closing_brackets = "{([<", "})]>"


class Stack:
    def __init__(self):
        self.content = []
    def size(self):
        return len(self.content)
    def empty(self):
        return 0 == self.size()
    def push(self, item):
        self.content.append(item)
    def peek(self):
        return self.content[-1]
    def pop(self):
        temp = self.content[-1]
        del self.content[-1]
        return temp


def get_match(bracket):
    if bracket in opening_brackets:
        return closing_brackets[opening_brackets.find(bracket)]
    elif bracket in closing_brackets:
        return opening_brackets[closing_brackets.find(bracket)]


def closed_brackets(input_str):
    temp, has_bracket = Stack(), False
    for char in input_str:
        if char in opening_brackets:
            temp.push(char)
            has_bracket = True
        elif char in closing_brackets:
            if temp.peek() == get_match(char):
                temp.pop()
            else:
                return False
    if not has_bracket:
        e = ValueError()
        e.strerror = "String does not contain brackets"
        raise e
    return True


class TestClosedBrackets(TestCase):

    data = [
        {
            'arg': "([])[]({})",
            'expected': True
        },
        {
            'arg': "(([[))]]",
            'expected': False
        },
        {
            'arg': "(x + (y * z))",
            'expected': True
        }
    ]

    def test_closed_brackets(self):
        for case in self.data:
            print(case)
            assert closed_brackets(case['arg']) == case['expected']

    def test_value_error(self):
        self.assertRaises(ValueError, closed_brackets, 'no brackets')
