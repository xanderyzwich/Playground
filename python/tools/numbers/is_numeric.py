"""
It's a Number!:

Well, it's that time of year again:
    Time to review employee time-cards!
    Unfortunately, you work for a company that employs a large number of malicious software quality testers,
    and they like to enter their time "creatively".
Your job is to check the time entries and figure out which ones are valid entries and which ones are not,
so management can bilk appropriately refrain from compensating these mischievous employees for invalid time entries.

Given a string, indicate whether it represents a number.
The string may be of any length,
and may contain non-numeric characters such as periods, commas, preceding dashes (minus signs),
and scientific notation characters, i.e. any reasonable numeric format (does not include Roman numerals).

Importantly,
numbers don't have spaces.
You don't need to determine what *type* of number (integer, float) or the numeric value,
but you do get bonus points for not using a regular expression!
Extra street cred if you don't use your language's built-in number identification function (if it has one).
"""

from unittest import TestCase


def is_numeric(input_str):
    if valid_num(input_str):
        return True
    if len(input_str) < 2:
        return False
    if ' ' in input_str:
        return False

    # invalid_negative = (('-' in input_str) and ())
    if is_valid_scientific(input_str):
        return True
    if is_alpha(input_str) or is_alpha(input_str[0:1]):
        return False

    if all(['-' in input_str, input_str.index('-') == 0, 0 < len(input_str[1:])]):
        return True

    # print(f'invalid_negative: {invalid_negative} all_alpha:  {all_alpha}')
    # is_valid = not any([invalid_negative,  all_alpha])
    # print(is_valid, input_str)
    # return is_valid
    return False

def valid_num(num_str):
    try:
        _ = float(num_str.replace(',', '_'))
    except ValueError:
        return False
    return True

def is_valid_scientific(sci_str):
    if 'e' in sci_str:
        print('has e')
        parts = sci_str.split('e')
        print(parts)
        parts_are_nums = all([valid_num(p) for p in parts])
        print(parts_are_nums)
        return parts_are_nums

    elif 'x' in sci_str:
        print('has x')
        if len(sci_str) < 5:
            return False
        if ('x' in sci_str) and ('-' in sci_str):
            base, ten_power = sci_str.split('x')
            ten, power = ten_power.split('-')
            print('Has x parts:', base, ten, power)
            return all([valid_num(x) for x in [base, ten, power]])
        return False

    else:
        print('no e or x')
        return False


def is_alpha(check_str):
    for c in check_str:
        if c not in 'abcdefghijklmnopqrstuvwxyz':
            return False
    return True


class TestIsNumeric(TestCase):
    data = {
        '10': True,
        '-10': True,
        '10.0': True,
        '1,000,000': True,
        '1e5': True,
        '5x10-3': True,
        'a': False,
        'x1': False,
        'a -2': False,
        '-': False,
        '5 00': False,
    }

    def test_data(self):
        for arg, expected in self.data.items():
            print(f'Testing {arg} expecting {expected}')
            assert is_numeric(arg) == expected
