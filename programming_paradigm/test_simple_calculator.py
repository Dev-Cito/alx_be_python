from test_simple_calculator import SimpleCalculator
import unittest

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()


    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)

    def test_subtract():
         self.assertEqual(self.calc.subtract(4, 3), 1)
         self.assertEqual(self.calc.add(2, 0), 2)
         self.assertEqual(self.calc.add(-7, 3), -10)

    def test_multiply():
         self.assertEqual(self.calc.multiply(2, 3), 6)
         self.assertEqual(self.calc.add(3, 0), 0)
         self.assertEqual(self.calc.add(-5, 2), 10)
         self.assertEqual(self.calc.add(-5, 3), -15)

    def test_divide():
         self.assertEqual(self.calc.divide(8, 2), 4)
         self.assertEqual(self.calc.add(12, 0), 0)