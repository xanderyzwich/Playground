"""
Substitution Ciphers

In a substitution cipher characters or groups of bits are replaced by other characters or groups of bits.
Julius Caesar used aa shift of the alphabet by 3 positions to communicate with the commanders of his garrison

Write one function that will take the plaintext string and perform the encoding by this cipher.
A second function should be created to decode the same.

The letter plus 3 cipher will encode A to D, B to E, C to F and so on with X to A, Y to B, and Z to C.
"""
from unittest import TestCase

arg, expected, alternate = 'arg', 'expected', 'alternate'
# alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet = "".join([chr(i) for i in range(97, 123)])


def __slide_letter(char, offset):
    if not char.isalpha():
        return char
    result = alphabet[(alphabet.find(char.lower()) + offset) % len(alphabet)]
    return result if char.islower() else result.upper()


def __slide_alternate(char, offset):
    return chr(ord(char) + offset)


def encode(plaintext_string, offset=3, alternate=False, decode=False):
    encoded_string = ''
    slide = offset * ((-1)**decode)  # negate if decoding
    func = __slide_alternate if alternate else __slide_letter
    for char in plaintext_string:
        encoded_string += func(char, slide)
    return encoded_string


def decode(ciphertext_string, offset=3, alternate=False):
    return encode(ciphertext_string, offset, alternate, decode=True)


class TestSubstitutionCipher(TestCase):

    data = [
        {
            arg: "hello world!",
            expected: "khoor zruog!",
            alternate: 'khoor#zruog$'
        },
        {
            arg: "code connector",
            expected: "frgh frqqhfwru",
            alternate: 'frgh#frqqhfwru'
        },
        {
            arg: "i like spam",
            expected: "l olnh vsdp",
            alternate: 'l#olnh#vsdp'
        },
        {
            arg: "Fu Bar Baz?",
            expected: "Ix Edu Edc?",
            alternate: 'Ix#Edu#Ed}B'
        }
    ]

    def test_encode(self):
        for entry in self.data:
            assert encode(entry[arg]) == entry[expected]

    def test_decode(self):
        for entry in self.data:
            assert decode(entry[expected]) == entry[arg]                # wrapper
            assert encode(entry[expected], decode=True) == entry[arg]   # without wrapper

    def test_roundtrip(self):
        for entry in self.data:
            assert decode(encode(entry[arg])) == entry[arg]             # forward
            assert encode(decode(entry[expected])) == entry[expected]   # reverse

    def test_alternate(self):
        for entry in self.data:
            assert encode(entry[arg], alternate=True) == entry[expected]
            assert decode(entry[expected], alternate=True) == entry[arg]
            assert decode(encode(entry[arg], alternate=True), alternate=True) == entry[arg]
            assert encode(decode(entry[expected], alternate=True), alternate=True) == entry[expected]
