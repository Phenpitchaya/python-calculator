import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:
    def test_add(self):
        self.assertEqual(self.calc.add(3, 7), 10)

    def test_add2(self):
        self.assertEqual(self.calc.add(-4, -6), -10)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10, 5), -5)

    def test_subtract2(self):
        self.assertEqual(self.calc.subtract(-3, -8), -5)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)

    def test_multiply2(self):
        self.assertEqual(self.calc.multiply(0, 5), 0)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_divide2(self):
        self.assertEqual(self.calc.divide(9, 3), 3)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)
        
    def test_modulo2(self):
        self.assertEqual(self.calc.modulo(8, 4), 0)

if __name__ == '__main__':
    unittest.main()