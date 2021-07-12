"""
There is a secret string which is unknown to you.
Given a collection of random triplets from the string, recover the original string.
A triplet here is defined as a sequence of three letters
    such that each letter occurs somewhere before the next in the given string.
"whi" is a triplet for the string "whatisup".
As a simplification, you may assume that no letter occurs more than once in the secret string.
You can assume nothing about the triplets given to you other than that they are valid triplets
    and that they contain sufficient information to deduce the original string. In particular,
    this means that the secret string will never contain letters that do not occur in one of the triplets given to you.
"""

from unittest import TestCase


def recover_secret(triplets):
    secret = triplets[0]
    for triple in triplets[1:]:
        first, second, third = tuple(triple)
        first_in_secret, second_in_secret, third_in_secret = (x in secret for x in (first, second, third))
        if all([first_in_secret, third_in_secret, not second_in_secret]):
            secret.insert(secret.index(first)+1, second)
        elif all([second_in_secret, third_in_secret, not first_in_secret]):
            secret.insert(secret.index(second), first)
        elif all([first_in_secret, second_in_secret, not third_in_secret]):
            secret.insert(secret.index(second)+1, third)
        else:
            print("I borked")
    return ''.join(secret)


class TestSecretRecovery(TestCase):
    def test_whatisup(self):
        rules = [
          ['t', 'u', 'p'],
          ['w', 'h', 'i'],
          ['t', 's', 'u'],
          ['a', 't', 's'],
          ['h', 'a', 'p'],
          ['t', 'i', 's'],
          ['w', 'h', 's'],
        ]
        assert recover_secret(rules) == 'whatisup'
