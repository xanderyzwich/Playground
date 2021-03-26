"""
Print the numbers 1 to 100 in reverse order
"""
def count_reversed(input_integer):
    if input_integer == 100:
        print(input_integer)
        return
    else:
        count_reversed(input_integer+1)
        print(input_integer)


def print_count_reversed():
    print_count_reversed(1)


if __name__ == '__main__':
    count_reversed()
