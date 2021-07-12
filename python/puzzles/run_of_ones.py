"""
Given an integer input
return the length of the longest section of sequential ones from the binary representation
"""
import re
from unittest import TestCase
from python.tools.decorators import function_details


# @function_details
def run_of_ones(input_num):
    clean = str(bin(input_num))[2:]
    runs = re.split(r'[0]+', clean)
    return max([len(run) for run in runs])


class TestRunOfOnes(TestCase):
    data = {
        7: 3,
        156: 3,
        1979: 4,
        2731: 2,
        2185: 1,
    }

    def test_data(self):
        for arg, expected in self.data.items():
            print(f'Testing{arg: 5} expecting{expected: 2}', end=' -- ')
            assert run_of_ones(arg) == expected
            print('PASSED!')


if __name__ == '__main__':
    print(str(bin(1979))[2:])
    print(re.split(r'[0]+', str(bin(1979))[2:]))
