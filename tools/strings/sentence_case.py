"""
CAPS LOCK DAY is over!
October 22nd is CAPS LOCK DAY.
Apart from that day, every sentence should be lowercase, so write a function to normalize a sentence.
Create a function that takes a string.
If the string is all uppercase characters, convert it to lowercase and add an exclamation mark at the end.
"""
from unittest import TestCase


def normalize(input_str):
    not_capslock = input_str != input_str.upper()
    output_str = input_str[0].upper() + input_str[1:].lower()
    return output_str if not_capslock else output_str + '!'


class TestNormalize(TestCase):

    def test_normalize(self):
        assert normalize("CAPS LOCK DAY IS OVER") == "Caps lock day is over!"
        assert normalize("Today is not caps lock day.") == "Today is not caps lock day."
        assert normalize("Let us stay calm, no need to panic.") == "Let us stay calm, no need to panic."
