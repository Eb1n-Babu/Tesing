import unittest
from anagram_check import anagram


class TestAnagram(unittest.TestCase):
    def test_anagram(self):
        self.assertTrue(anagram(string_1='listen', string_2='silent'))

if __name__ == '__main__':
    unittest.main()