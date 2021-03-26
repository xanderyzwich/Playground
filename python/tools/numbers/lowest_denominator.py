import math


def lowest_denominator(input_number):
    for guess in range(2, math.ceil(math.sqrt(input_number))):
        if input_number % guess == 0:
            return guess
    return 1


if __name__ == '__main__':
    number_to_try = 95
    print(f'Lowest denominator of {number_to_try} is {lowest_denominator(number_to_try)}')
