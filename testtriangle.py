import unittest
from triangle import *

class TriangleTestCase(unittest.TestCase):
    def test_small_mul(self):
        res = area(10, 5)
        self.assertEqual(res, 25)
    def test_big_mul(self):
        res = area(1234567, 2345678)
        self.asseertEqual(res, 1447948325713)
    def test_small_mul(self):
        res = perimeter(5, 6, 7)
        self.assertEqual(res, 18)
    def test_big_mul(self):
        res = perimeter(1234567890, 2345678901, 3456789012)
        self.assertEqual(res, 7037035803)
