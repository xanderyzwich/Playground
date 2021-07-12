class CoinPurse:
    def __init__(self, counts):
        self.counts = counts

    def __repr__(self):
        return self.__str__() + ' = ' + str(self.counts)

    def __str__(self):
        amount = self.counts[0] * 25
        amount += self.counts[1] * 10
        amount += self.counts[2] * 5
        amount += self.counts[3] * 1
        return str(amount / 100)

    def has_quarter(self):
        return self.counts[0] > 0

    def has_dime(self):
        return self.counts[1] > 0

    def has_nickel(self):
        return self.counts[2] > 0

    def has_penny(self):
        return self.counts[3] > 0

    def remove_quarter(self):
        if self.has_quarter():
            self.counts[0] -= 1
            return 25
        else:
            return 0

    def remove_dime(self):
        if self.has_dime():
            self.counts[1] -= 1
            return 10
        else:
            return 0

    def remove_nickel(self):
        if self.has_nickel():
            self.counts[2] -= 1
            return 5
        else:
            return 0

    def remove_penny(self):
        if self.has_penny():
            self.counts[3] -= 1
            return 1
        else:
            return 0

    def enough_change(self, total):
        my_total = total * 100
        check_purse = CoinPurse(self.counts.copy())
        while check_purse.has_quarter() and my_total >= 25:
            my_total -= check_purse.remove_quarter()
        while check_purse.has_dime() and my_total >= 10:
            my_total -= check_purse.remove_dime()
        while check_purse.has_nickel() and my_total >= 5:
            my_total -= check_purse.remove_nickel()
        while check_purse.has_penny() and my_total >= 1:
            my_total -= check_purse.remove_penny()
        if my_total > 0:
            return False
        else:
            return True
    
    def remove_change(self, total):
        my_total = total * 100
        if not self.enough_change(total):
            return False

        while self.has_quarter() and my_total >= 25:
            my_total -= self.remove_quarter()
        while self.has_dime() and my_total >= 10:
            my_total -= self.remove_dime()
        while self.has_nickel() and my_total >= 5:
            my_total -= self.remove_nickel()
        while self.has_penny() and my_total >= 1:
            my_total -= self.remove_penny()
        print(f'Remainder after removing {total} change: {self.__repr__()}')
        return True


if __name__ == '__main__':
    coin_purse = CoinPurse([0, 0, 10, 1])
    amount = 0.40
    print(f'Has {amount} to pay? {coin_purse.enough_change(amount)}')
    coin_purse.remove_change(amount)
