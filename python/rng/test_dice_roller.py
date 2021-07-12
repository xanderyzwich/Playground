from unittest import TestCase, mock

from rng.dice_roller import DiceRoller


class TestDiceRoller(TestCase):

    def test_roll_calls_randint(self):
        with mock.patch('random.randint', return_value=3):
            d2 = DiceRoller(2)
            assert d2.roll() == 3

    def test_roll_multiple_calls_roll(self):
        with mock.patch('random.randint', return_value=3):
            d2 = DiceRoller(2)
            assert sum(d2.roll_multiple(12)) == 36
