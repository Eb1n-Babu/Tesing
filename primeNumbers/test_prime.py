import  unittest
from primeNumber import findPrime


class TestPrime(unittest.TestCase):
    def test_prime(self):
        self.assertEqual(findPrime(2), True)
        self.assertEqual(findPrime(3), True)
        self.assertEqual(findPrime(4), False)
        self.assertEqual(findPrime(5), True)
        self.assertEqual(findPrime(6), False)

if __name__ == '__main__':
    unittest.main()