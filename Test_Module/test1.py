import unittest
from case1 import odd_even

class TestOddEven(unittest.TestCase):
    def test_odd(self):
        self.assertFalse(odd_even(1))
        self.assertFalse(odd_even(3))
        self.assertFalse(odd_even(5))
        self.assertFalse(odd_even(7))
        self.assertFalse(odd_even(9))

    def test_even(self):
        self.assertTrue(odd_even(2))
        self.assertTrue(odd_even(4))
        self.assertTrue(odd_even(6))
        self.assertTrue(odd_even(8))
        self.assertTrue(odd_even(10))

    def test_zero(self):
        self.assertIsNone(odd_even(0))

if __name__ == '__main__':
    unittest.main()