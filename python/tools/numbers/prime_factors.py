import math
from pprint import pprint


def factor(input_number):
    sieve_max = math.ceil(math.sqrt(input_number))
    sieve_results = list(range(2, sieve_max))
    print("Begin finding primes")
    for num in range(2, math.ceil(math.sqrt(sieve_max))):
        multiple = num
        while multiple < sieve_max:
            multiple += num
            if multiple in sieve_results:
                sieve_results.remove(multiple)
    print(f'Primes found {sieve_results}')
    primes = sieve_results
    prime_factors = list([])
    remainder = input_number
    while remainder not in primes:
        for p in primes:
            print(f'Checking if {remainder} is divisible by {p}')
            if remainder % p == 0:
                print(f'   {remainder} is divisible by {p}')
                prime_factors.append(p)
                remainder = remainder // p
    prime_factors.append(remainder)
    return prime_factors


if __name__ == '__main__':
    number_to_factor = 1890
    print(f'The prime factors of {number_to_factor} are {pprint(factor(number_to_factor))}')
