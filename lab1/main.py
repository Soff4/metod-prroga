import unittest

def factorial(x):
    if x == 0:
        return 1

    if x == 1:
        return 1

    return (x * factorial(x-1))


class TestFactorial(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(6), 720)
        self.assertEqual(factorial(10), 3628800)
        self.assertEqual(factorial(3), 6)

if __name__ == '__main__':
    unittest.main()