"""
# Dictionary Decompression

Given a nested dictionary, flatten the dictionary such that the keys of the final result are namespaced with a period between the original keys leading to the value.

## Business Rules/Errata

- ***Data Structure Required: Dictionary/Map/HashMap*** This challenge requires a language that supports a version of a Dictionary.
- Your function should be able to flatten dictionaries nested arbitrarily deeply.
- You can assume that none of the dictionary keys contain a period.
- The type of the dictionary values is not important to this exercise. Assume they will always be unsigned integers.
"""

from unittest import TestCase
from python.structures.stack_abuse import AbuseStack


def flatten_dict_solved(input_dict, key_stack=AbuseStack()):
    stack = key_stack
    output_dict = {}
    #  Do Something here
    for key, value in input_dict.items():
        stack += key

        if isinstance(value, dict):
            # # First try
            # for k, v in temp.items():
            #     stack += k
            #     output_dict[str(stack)] = v
            #     stack -= 1

            # Second try
            # output_dict = {**output_dict, **flatten_dict(value, stack)}

            # Third try
            output_dict.update(flatten_dict(value, stack))

        else:
            output_dict[str(stack)] = value
        stack -= 1
    # print(str(output_dict))
    return output_dict


def flatten_dict(input_dict):
    output_dict = {}
    for key, value in input_dict.items():
        if isinstance(value, dict):
            temp = flatten_dict(value)
            for k, v in temp.items():
                output_dict['.'.join([key, k])] = v
        else:
            output_dict[key] = value
    print(output_dict)
    return output_dict



class TestFlattenDict(TestCase):

    def test_flat(self):
        flat = {'fu': 1}
        assert flatten_dict(flat) == flat
        # flat['bar'] = 2
        # assert flatten_dict(flat) == flat

    # def test_nested(self):
    #     nested = {
    #         'fu': {
    #             'bar': 'baz',
    #         },
    #     }
    #     flat = {
    #         'fu.bar': 'baz',
    #     }
    #     assert flatten_dict(nested) == flat
    #     nested['fu']['thing'] = {'other': 'value'}
    #     flat['fu.thing.other'] = 'value'
    #     assert flatten_dict(nested) == flat
    #
    # def test_example(self):
    #     nested_dict = {
    #         'key': 3,
    #         'foo': {
    #             'a': 5,
    #             'bar': {
    #                 'baz': 8,
    #             }
    #         }
    #     }
    #     flat_dict = {
    #         "key": 3,
    #         "foo.a": 5,
    #         "foo.bar.baz": 8,
    #     }
    #     assert flatten_dict(nested_dict) == flat_dict

