"""
RIGHT PLACEMENT:
Given a map / dict of {Partition: Memory}, and a memory value, return the optimal partition name for the memory given (job). If no partitions satisfy the memory requirements, return a scary error message and exit.
Partition:

{'XSMALL': 1000,
 'SMALL': 4000,
 'MEDONE': 8000,
 'MEDTWO': 16000,
 'MEDTHREE': 24000,
 'LARGEONE': 32000,
 'LARGETWO': 54000,
 'LARGETHREE': 64000,
 'XLARGE': 128000,}

Clarifications:
You will need to create your own partition map to use, but the numbers should be the ones from the above example!
If a job has a memory requirement of 2000, you should place it in SMALL, because this is optimal:

XSMALL < 2000 < SMALL
"""
from unittest import TestCase

sizing = [
    ('XSMALL', 1000),
    ('SMALL', 4000),
    ('MEDONE', 8000),
    ('MEDTWO', 16000),
    ('MEDTHREE', 24000),
    ('LARGEONE', 32000),
    ('LARGETWO', 54000),
    ('LARGETHREE', 64000),
    ('XLARGE', 128000),
]


def find_partition_by_memory(partition_map, address):
    for name, max in partition_map:
        print(name, max)
        if address < max:
            return name
    return 'ABORT! THIS MUCH MEMORY DOES NOT EXIST!'


class TestFindPartitionByMemory(TestCase):
    data = {
        (900, 'XSMALL'),
        (2000, 'SMALL'),
        (6000, 'MEDONE'),
        (10000, 'MEDTWO'),
        (20000, 'MEDTHREE'),
        (30000, 'LARGEONE'),
        (40000, 'LARGETWO'),
        (60000, 'LARGETHREE'),
        (100000, 'XLARGE'),
        (200000, 'ABORT! THIS MUCH MEMORY DOES NOT EXIST!'),
    }

    def setUp(self):
        print(f'\n--- Running test: {self._testMethodName} ---')

    def test_data(self):
        for input, expected in self.data:
            assert find_partition_by_memory(sizing, input) == expected