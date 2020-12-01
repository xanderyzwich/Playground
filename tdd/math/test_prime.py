import unittest
import tdd.math.prime as p

class TestPrime(unittest.TestCase):

    def test_my_sqrt(self):
        self.assertEqual(p.my_sqrt(4), 2)
        self.assertEqual(p.my_sqrt(24), 5)

    def test_is_divisible(self):
        self.assertTrue(p.is_divisible(1, 1))
        self.assertFalse(p.is_divisible(1, 2))

    def test_is_prime(self):
        self.assertTrue(p.is_prime(3))


if __name__ == '__main__':
    TestPrime.main()
