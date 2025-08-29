import unittest
from safe_eval import safe_eval

class TestSafeEval(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(safe_eval("3 + 5"), 8)

    def test_subtraction(self):
        self.assertEqual(safe_eval("10 - 4"), 6)

    def test_multiplication(self):
        self.assertEqual(safe_eval("3 * 4"), 12)

    def test_division(self):
        self.assertEqual(safe_eval("10 / 2"), 5)

    def test_nested_expression(self):
        self.assertEqual(safe_eval("3 * 4 + 5"), 17)

    def test_complex_expression(self):
        self.assertEqual(safe_eval("2 * 3 - 8 / 2 + 5"), 7)

    def test_invalid_operator(self):
        with self.assertRaises(ValueError):
            safe_eval("3 $ 5")

    def test_invalid_expression(self):
        with self.assertRaises(ValueError):
            safe_eval("3 + ")

    def test_empty_expression(self):
        with self.assertRaises(ValueError):
            safe_eval("")

if __name__ == '__main__':
    unittest.main()
