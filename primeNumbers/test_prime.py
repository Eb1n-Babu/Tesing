import unittest
from primeNumber import findPrime


class TestPrime(unittest.TestCase):
    def test_findPrime(self):
        self.assertEqual(findPrime(2), True)
        self.assertEqual(findPrime(3), True)
        self.assertEqual(findPrime(4), False)

if __name__ == '__main__':
    unittest.main()