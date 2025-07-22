import unittest
from case3 import alphabet

class Test(unittest.TestCase):
    def test_alphabet(self):
        self.assertEqual(alphabet("hello"), "Hello")
        self.assertEqual(alphabet(" hello"), " hello")


if __name__ == '__main__':
    unittest.main()