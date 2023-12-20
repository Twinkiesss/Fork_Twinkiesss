import unittest
from square import *

class SquareTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(0)
        self.assertEqual(res, 0)
    def test_small_mul(self):
        res = area(10)
        self.assertEqual(res, 100)
    def test_big_mul(self):
        res = area(1234567890)
        self.asseertEqual(res, 1524157875019052100)
    def test_float_mul(self):
        res = area(2.22)
        self.assertEqual(res, 4.9284)
    def test_zero_mul(self):
        res = perimeter(0)
        self.assertEqual(res, 0)
    def test_small_mul(self):
        res = perimeter(1)
        self.assertEqual(res, 4)
    def test_big_mul(self):
        res = perimeter(1234567890)
        self.assertEqual(res, 4938271560)
    def test_float_mul(self):
        res = perimeter(2.22)
        self.assertEqual(res, 8.88)
