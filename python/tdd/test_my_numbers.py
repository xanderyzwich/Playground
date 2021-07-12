import unittest

from tdd.my_numbers import MyNumber


class TestNumbers(unittest.TestCase):

    def test_is_positive(self):
        assert MyNumber(1).is_positive()
        assert not MyNumber(-1).is_positive()

    def test_my_sqrt(self):
        assert MyNumber(4).my_sqrt() == 2
        assert MyNumber(23).my_sqrt() == 5

    def test_is_divisible(self):
        assert MyNumber(4).is_divisible_by(2)
        assert not MyNumber(5).is_divisible_by(3)

    def test_is_prime(self):
        assert MyNumber(3).is_prime()
        assert not MyNumber(4).is_prime()


if __name__ == '__main__':
    TestNumbers.main()
