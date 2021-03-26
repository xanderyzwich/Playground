"""
How Much is True?
Create a function which returns the number of true values there are in an array.
Notes
+ Return 0 if given an empty array.
+ All array items are of the type bool (true or false).
"""


def count_true(input_array):
    # true_set = list(filter(lambda item: item is True, input_array))
    count = sum([1 for item in input_array if item is True])
    return count


if __name__ == '__main__':
    print(count_true([True, False, False, True, False]))
    print(count_true([False, False, False, False]))
    print(count_true([]))
