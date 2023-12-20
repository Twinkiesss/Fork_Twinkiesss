import unittest
from circle import *

class CircleTestCase(unittest.TestCase):
    def test_small_mul(self):
        res = area(10)
        self.assertEqual(res, 314.1592653589793)
    def test_big_mul(self):
        res = area(123456789)
        self.asseertEqual(res, 4.788283183070884e+16)
    def test_float_mul(self):
        res = area(2.22)
        self.assertEqual(res, 15.483025233951938)
    def test_small_mul(self):
        res = perimeter(5)
        self.assertEqual(res, 31.41592653589793)
    def test_big_mul(self):
        res = perimeter(123456789)
        self.assertEqual(res, 775701882.7163703)
    def test_float_mul(self):
        res = perimeter(2.22)
        self.assertEqual(res, 13.948671381938683)
