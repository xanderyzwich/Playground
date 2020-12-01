from unittest import TestCase

from structures.collections import *


class TestStack(TestCase):

    def test_all(self):
        stack = Stack()
        assert stack.is_empty()
        assert 0 == stack.count
        stack.push('test')
        assert 1 == stack.count
        assert stack.peek() == 'test'
        stack.pop()
        assert stack.is_empty()


class TestQueue(TestCase):

    def test_all(self):
        queue = Queue()
        assert 0 == queue.count
        assert queue.is_empty()
        queue.add('test')
        assert 1 == queue.count
        assert not queue.is_empty()
        assert 'test' == queue.element()
        queue.remove()
        assert queue.is_empty()