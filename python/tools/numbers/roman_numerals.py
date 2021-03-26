"""
We would like to be able to convert Arabic numbers into their Roman numeral equivalents.
We just need some kind of program that can accept a numeric input and output the Roman numeral for the input number.
There is no need to be able to convert numbers larger than about 3000. (The Romans themselves didn't tend to go any higher.)

The Romans wrote their numbers using letters - I, V, X, L, C, D, and M.  (These letters have straight lines that are easy to hack into stone tablets.) Specifically the letter 'I' means '1', 'V' means '5', 'X' means '10', 'L' means '50', 'C' means '100', 'D' means '500', and 'M' means '1000'.There were certain rules that the numerals followed which should be observed:
·         The symbols 'I', 'X', 'C', and 'M' can be repeated at most 3 times in a row.
·         The symbols 'V', 'L', and 'D' can never be repeated.
·         The '1' symbols ('I', 'X', and 'C') can only be subtracted from the 2 next highest values ('IV' and 'IX', 'XL' and 'XC', 'CD' and 'CM').
·         Only one subtraction can be made per numeral ('XC' is allowed, 'XXC' is not).
·         The '5' symbols ('V', 'L', and 'D') can never be subtracted.
"""

from unittest import TestCase

numeral_values = {
    1: 'I',
    4: 'IV',
    5: 'V',
    9: 'IX',
    10: 'X',
    40: 'XL',
    50: 'L',
    90: 'XC',
    100: 'C',
    400: 'CD',
    500: 'D',
    900: 'CM',
    1000: 'M',
}


def to_roman_numeral(input_int):
    output, remainder = '', input_int

    for val in sorted(numeral_values.keys(), reverse=True):
        # print(f'Checking key {val} and remainder {remainder}')
        if val <= remainder:
            count = remainder // val
            remainder = remainder % val
            output += str(numeral_values[val]) * count

    print(f'Input: "{input_int}" \t\t Output: "{output}"')
    return output


class TestRomanNumerals(TestCase):
    data = {
        1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX',
        10: 'X', 20: 'XX', 30: 'XXX', 40: 'XL', 50: 'L', 60: 'LX', 70: 'LXX', 80: 'LXXX', 90: 'XC',
        100: 'C', 200: 'CC', 400: 'CD', 500: 'D', 900: 'CM',
        1000: 'M',
        1066: 'MLXVI',
        1989: 'MCMLXXXIX',
    }

    def test_roman_numerals(self):
        for arg, expected in self.data.items():
            assert to_roman_numeral(arg) == expected


