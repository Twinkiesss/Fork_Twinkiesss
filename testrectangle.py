import unittest
from rectangle import *

class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(10, 0)
        self.assertEqual(res, 0)
    def test_small_mul(self):
        res = area(10, 11)
        self.assertEqual(res, 110)
    def test_big_mul(self):
        res = area(1234567890, 2345678901)
        self.asseertEqual(res, 2895899851425088890)
    def test_zero_mul(self):
        res = perimeter(0, 0)
        self.assertEqual(res, 0)
    def test_small_mul(self):
        res = perimeter(1, 2)
        self.assertEqual(res, 6)
    def test_big_mul(self):
        res = perimeter(1234567890, 2345678901)
        self.assertEqual(res, 7160493582)
