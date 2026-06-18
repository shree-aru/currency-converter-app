import unittest
from converter_logic import convert_currency

class TestCurrencyConverter(unittest.TestCase):

    def test_valid_conversion(self):
        amount, error = convert_currency(100, "USD", "EUR")
        self.assertAlmostEqual(amount, 92.0)
        self.assertIsNone(error)

    def test_same_currency_conversion(self):
        amount, error = convert_currency(50, "GBP", "GBP")
        self.assertAlmostEqual(amount, 50.0)
        self.assertIsNone(error)

    def test_invalid_source_currency(self):
        amount, error = convert_currency(100, "XYZ", "USD")
        self.assertIsNone(amount)
        self.assertIn("Source currency 'XYZ' not supported", error)

    def test_invalid_target_currency(self):
        amount, error = convert_currency(100, "USD", "XYZ")
        self.assertIsNone(amount)
        self.assertIn("Target currency 'XYZ' not supported", error)

    def test_case_insensitivity(self):
        amount, error = convert_currency(100, "usd", "eur")
        self.assertAlmostEqual(amount, 92.0)
        self.assertIsNone(error)

if __name__ == '__main__':
    unittest.main()
