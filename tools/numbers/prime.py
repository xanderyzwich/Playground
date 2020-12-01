from math import ceil, sqrt
prime_count = 1000
prime_list = [2, 3]
current_check = 4
while len(prime_list) <= prime_count:
    is_prime = True
    square_root = ceil(sqrt(current_check))
    check_set = [i for i in prime_list if i <= square_root]
    for num in check_set:
        # print(f'For loop on {num}')
        if current_check % num == 0:
            is_prime = False
            break
    if is_prime:
        prime_list.append(current_check)
        print(f'{current_check} is prime')
    current_check += 1

print(prime_list)
