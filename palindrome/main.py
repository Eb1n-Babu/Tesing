from palindrome.palindrome_Test import palindrome
import unittest

class TestPalindrome(unittest.TestCase):
    def test_basic_palindrome(self):
        self.assertTrue(palindrome('malayalam'))
        self.assertTrue(palindrome('malayalam  '))
        self.assertTrue(palindrome('  ma lay a lam '))

if __name__ == '__main__':
    unittest.main()