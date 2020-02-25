import unittest
import Calculator
import DataTest

from ddt import ddt, data, unpack
@ddt

class CalculatorTests(unittest.TestCase):

    def setUp(self):
        self.system = 10
        self.c = Calculator.Calculator(self.system)

    @data(("2","2",4), ("0","5",5), ("-2","2",0))
    @unpack
    def test_add(self, a, b, expectation):
        r = self.c.add(a,b)
        self.assertEqual(expectation,r)

    @data(("2", "2", 0), ("0", "5", -5), ("-2", "2", -4))
    @unpack
    def test_sub(self, a, b, expectation):
        r = self.c.sub(a, b)
        self.assertEqual(expectation, r)

    @data(("2", "2", 4), ("0", "5", 0), ("-2", "2", -4))
    @unpack
    def test_mul(self, a, b, expectation):
        r = self.c.mul(a, b)
        self.assertEqual(expectation, r)

    @data(("2", "2", 1), ("0", "5", 0), ("-2", "2", -1))
    @unpack
    def test_div(self, a, b, expectation):
        r = self.c.div(a, b)
        self.assertEqual(expectation, r)

    @data(("2+2", 4), ("3 *2", 6))
    @unpack
    def test_process(self, str, expectation):
        r = self.c.process(str)
        self.assertEqual(expectation, r)

if __name__ == "__main__":
    unittest.main()