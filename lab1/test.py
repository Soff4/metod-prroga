import unittest
from main import factorial

class TestFactorial(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(6), 720)
        self.assertEqual(factorial(10), 3628800)
        self.assertEqual(factorial(3), 6)

if __name__ == '__main__':
    unittest.main()