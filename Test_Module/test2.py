import unittest
from case2 import reverse


class MyTestCase(unittest.TestCase):
    def test_reverse(self):
        self.assertEqual(reverse("hello"), "olleh")
        self.assertEqual(reverse(" "), " ")
        self.assertEqual(reverse("1234"), "4321")
 


if __name__ == '__main__':
    unittest.main()