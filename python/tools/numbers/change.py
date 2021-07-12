"""
Can you give the given amount of change from the number of coins provided?
"""


def how_many_coins(coin_value, total):
    number_of_coins = total // coin_value
    leftover = (total - number_of_coins * coin_value)
    # print(coin_value, number_of_coins, leftover)
    return number_of_coins, leftover


def format_change(change_purse):
    return (f'Quarters: {change[0]}\n'
            f'Dimes:    {change[1]}\n'
            f'Nickels:  {change[2]}\n'
            f'Pennies:  {change[3]}')


def ideal_change(total):
    change = list([])
    remainder = total * 100 # lets deal with cents
    for v in [25, 10, 5, 1]:
        coins_used, remainder = how_many_coins(v, remainder)
        change.append(coins_used)
        # print(change, coins_used, remainder)
    print(f'Ideal Change:\n{format_change(change)}')
    return change


def exact_change(coin_purse, total):
    for a, b in zip(coin_purse, ideal_change(total)):
        if a < b:
            return False
    return True


if __name__ == '__main__':
    change = [25, 20, 5, 0]
    value = 4.25
    # print(ideal_change(value))
    print(f'I have exact change. - {exact_change(change, value)}')
