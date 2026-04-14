#https://github.com/DChigin/lab11-DC
import unittest
import math 
from calculator import *
 
class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(10, 5), 15)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(77, 42), 119)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(5, 10), -5)
        self.assertEqual(subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(mul(3, 7), 21)
        self.assertEqual(mul(0, 10), 0)
        self.assertEqual(mul(5, -5), -25)

    def test_divide(self):
        self.assertEqual(div(10, 2), 5)
        self.assertEqual(div(9, 3), 3)
        self.assertAlmostEqual(div(10, 3), 3.3333333333333335)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(10, 0)
        
    def test_logarithm(self):
        self.assertAlmostEqual(logarithm(10, 100), 2.0)


    def test_log_invalid_argument(self):
        try:
            logarithm(10, -1)
            raise AssertionError("ValueError for invalid argument was not raised")
        except ValueError:
            pass

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(1, 10)


    def test_hypotenuse(self):
        self.assertAlmostEqual(math.hypot(3, 4), 5.0)
        self.assertAlmostEqual(math.hypot(-3, -4), 5.0)
        self.assertEqual(hypotenuse(5,3), (25+9)**(1/2))

    def test_sqrt(self):
        self.assertAlmostEqual(math.sqrt(25), 5.0)
        try:
            math.sqrt(-1)
            raise AssertionError("ValueError for negative sqrt was not raised")
        except ValueError:
            pass

if __name__ == "__main__":
    unittest.main()
