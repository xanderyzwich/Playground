"""
Return true if the string contains all letters in the alphabet.
"""


def contains_alphabet(input_string):
    for char in 'abcdefghijklmnopqrstuvwxyz':
        if char not in input_string.lower():
            return False
    return True


if __name__ == '__main__':
    check_strings = [
        'The quick brown fox jumps over the lazy dog',
        'I like cheese',
        'abcdefghijklmnopqrstuvwxyz',
        'my_name',
        'Sphinx of black quartz, judge my vow'
        ]
    for check_string in check_strings:
        print(f'{str(contains_alphabet(check_string)):<6}: {check_string}')
