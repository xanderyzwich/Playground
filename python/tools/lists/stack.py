"""
Print the numbers 1 to 100 in reverse order
"""


class Stack:
    def __init__(self):
        self.elements = []

    def push(self, element):
        self.elements.append(element)

    def pop(self):
        return self.elements.pop()

    def has_next(self):
        return 0 < len(self.elements)


if __name__ == '__main__':
    # stack = Stack()
    # for i in range(1, 100):
    #     stack.push(i)
    # while stack.has_next():
    #     print(stack.pop())

    print(list(range(1, 100))[::-1])
