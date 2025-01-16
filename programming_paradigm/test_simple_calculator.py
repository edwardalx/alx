import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1, -11), -12)
        self.assertEqual(self.calc.add(3000.5, -1), 2999.5)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(1, 1), 0)
        self.assertEqual(self.calc.subtract(2000, -1000), 3000)
        self.assertEqual(self.calc.subtract(-10, 1), -11)
        self.assertEqual(self.calc.subtract(-11.25, -11.25), 0)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(-1, -11), 11)
        self.assertEqual(self.calc.multiply(3000.5, -1), -3000.5)

    def test_division(self):
        self.assertEqual(self.calc.divide(1, 1), 1)
        self.assertEqual(self.calc.divide(2000, -1000), -2)
        self.assertEqual(self.calc.divide(-10, 1), -10)
        self.assertEqual(self.calc.divide(-11.25, -11.25), 1)
        self.assertEqual(self.calc.divide(-11.25, 0), None)
    
if __name__ == "__main__":
  unittest.main()
