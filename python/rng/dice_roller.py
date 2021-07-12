"""
    Basic Dice Rolling Application
"""
import random


class DiceRoller:
    def __init__(self, value):
        self.max = int(value)
        print(f'new d{value}')

    def roll(self):
        value = random.randint(1, self.max)
        print(f'd{self.max} rolled {value}')
        return value

    def roll_multiple(self, times):
        results = list([])
        for t in range(int(times)):
            results.append(self.roll())
        return results


class DiceSet:
    def __init__(self, dice_dict):
        self.dice = list([])
        for d in dice_dict.keys():
            value_string = str(d)[1::]
            value = int(value_string)
            self.add(value, dice_dict[d])

    def add(self, value, count):
        for c in range(1, count):
            self.dice.append(DiceRoller(value))

    def roll(self):
        value = 0
        for die in self.dice:
            value += die.roll()
        return value


def summarize(list):
    from collections import Counter
    import pprint
    pp = pprint.PrettyPrinter(indent=4, sort_dicts=True, compact=False)
    counter = Counter(list)
    print("\n", f'Counts for {len(list)} elements')
    for k in sorted(counter.keys()):
        print(f'  {k:<4}:  {counter.get(k)}')
    print(f'  Sum :  {sum(list)}')
    print(f'  Avg :  {sum(list)/len(list)}')


if __name__ == '__main__':
    # d6 = DiceRoller(6)
    # for count in [10, 100, 1000, 10000]:
    #     summarize(d6.roll_multiple(count))

    hp = DiceSet({'d6': 4})
    print(hp.roll())
