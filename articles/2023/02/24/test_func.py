import unittest

from check_cov import fibonacci, factorial

class TestFibonacci(unittest.TestCase):

    def test_fibonacci_1(self):
        self.assertEqual(fibonacci(1), 1)

    def test_fibonacci_10(self):
        self.assertEqual(fibonacci(10), 89)

    def test_fibonacci_100(self):
        self.assertEqual(fibonacci(15), 987)


class TestFactorial(unittest.TestCase):
    def test_factorial_1(self):
        self.assertEqual(factorial(1), 1)

# if __name__ == '__main__':
#     unittest.main()
