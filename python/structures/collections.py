"""
Collection Type Data Structures
"""
from unittest import TestCase


class Stack:

    def __init__(self):
        self.data = []

    @property
    def count(self):
        return len(self.data)

    def is_empty(self):
        return 0 == self.count

    def push(self, element):
        self.data.append(element)

    def peek(self):
        return self.data[-1]

    def pop(self):
        del self.data[-1]


class Queue:

    def __init__(self):
        self.data = []

    @property
    def count(self):
        return len(self.data)

    def is_empty(self):
        return 0 == self.count

    def add(self, element):
        self.data.append(element)

    def element(self):
        return self.data[0]

    def remove(self):
        result = self.data[0]
        del self.data[0]
        return result
