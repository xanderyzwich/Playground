"""
Future ProfitsYou work for a hedge fund as a backend developer,
    particularly on the stock buying/selling service.
    Your firm has just had a major breakthrough:
        they've hired some god-like consultants to develop an algorithm that is able to reliably predict the
        stock price at 5 future times.
        Unfortunately, god-like consultants demand ungodly hourly rates,
        and your firm can't afford to keep them on for long enough to actually put that algorithm to use.
        That's where you come in...
        Given a number of buy/sell actions n and the next five prices for a given stock prices,
        identify the maximum profit your firm could make from buying (and then selling) that stock.
        For this proof-of-concept phase, don't worry about your starting budget,
        just assume you can buy an initial stock whenever is best (thus going into negative profit to start).
        For this limited test, you'll only be working with 5 prices and a small n,
        but your solution should be extensible to larger values of n and more price predictions
        (assuming your firm makes enough profit to pay the consultants to extend their pre-cognitive algorithm).

Some business rules:
    You can only hold one stock at a time, no pumping up the results by buying an arbitrarily large number of stocks then selling for marginal profit.
    You need to buy a stock before you can sell it.
    You need to sell a stock before you can buy another.
    It doesn't matter whether you are holding the stock or not at the end of the simulation.
    Each time you buy and each time you sell will count against your actions.
    You don't need to use all n actions.
    Stock prices are given in the order that they occur.
        You are not a time-traveler and thus are unable to buy stocks from the future to sell them in the past.
"""

from unittest import TestCase


def maximum_profit(n, prices):
    actions_remain = n
    have_stock = False
    profit = 0
    profits = []

    deltas = []
    for i in range(len(prices)-1):
        trend = 'up' if 0 < prices[i+1] - prices[i] else 'down'
        deltas.append(trend)
    deltas.append('down')
    log('  Deltas', deltas)

    for i, trend in enumerate(deltas):
        price = prices[i]
        if trend == 'up' and not have_stock:  # buy
            have_stock = True
            profit -= price
            print(f'    Buying at {price}, for {profit} total profit')
        elif trend == 'down' and have_stock:  # sell
            have_stock = False
            profits.append(profit+price)
            print(f'    Selling at {price}, with {profit} profit')
            log(f'      profits list', profits)
            profit = 0

    log('  possible profits', profits)
    actual_profits = log('  chosen profits', sorted(profits, reverse=True)[:(n//2)])
    return log('  profit', sum(actual_profits))


def log(label, value):
    print(f'{label}: {value}')
    return value


class TestMaxProfit(TestCase):
    data = [
        [4, [5, 2, 4, 0, 1], 3],
        [3, [0, 1, 2, 3, 4], 4],
        [4, [5, 8, 9, 3, 3], 4],
        [1, [5, 4, 9, 1, 6], 0],
        [4, [5, 8, 0, 9, 3], 12],
        [3, [5, 8, 0, 9, 3], 9],
    ]

    def test_max_profit_examples(self):
        for n, prices, expected in self.data:
            print(f'Testing that ({n}, {prices}) -> {expected}')
            assert maximum_profit(n, prices) == expected
