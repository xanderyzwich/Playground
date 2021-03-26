def box_print(string_array):
    width = max(*map(len, string_array))
    print("*"*(width+4))
    [print_fix_width(x, width) for x in string_array]
    print("*"*(width+4))


def print_fix_width(string, size):
    print(f'* {string}{" "*(size - len(string))} *')


if __name__ == '__main__':
    strings_to_print = 'Hello World in a frame'.split(' ')
    box_print(strings_to_print)
