import unittest

from src.pricing import (
    CartItem,
    apply_percentage_discount,
    calculate_subtotal,
)


class TestCalculateSubtotal(unittest.TestCase):
    def test_calculates_multiple_items(self):
        items = [
            CartItem("Keyboard", 49.99),
            CartItem("Mouse", 19.50, quantity=2),
        ]

        self.assertEqual(calculate_subtotal(items), 88.99)

    def test_empty_cart_returns_zero(self):
        self.assertEqual(calculate_subtotal([]), 0.0)

    def test_rejects_negative_price(self):
        items = [CartItem("Keyboard", -49.99)]

        with self.assertRaises(ValueError):
            calculate_subtotal(items)

    def test_rejects_invalid_quantity(self):
        items = [CartItem("Keyboard", 49.99, quantity=0)]

        with self.assertRaises(ValueError):
            calculate_subtotal(items)

    def test_zero_percent_keeps_subtotal(self):
        self.assertEqual(apply_percentage_discount(100.00, 0), 100.00)

    def test_rejects_percentage_above_100(self):
        with self.assertRaises(ValueError):
            apply_percentage_discount(100.00, 101)

    def test_applies_ten_percent_discount(self):
        self.assertEqual(apply_percentage_discount(100.00, 10), 90.00)

    def test_rejects_negative_subtotal(self):
        with self.assertRaises(ValueError):
            apply_percentage_discount(-1.00, 10)

    def test_rejects_negative_percent(self):
        with self.assertRaises(ValueError):
            apply_percentage_discount(100.00, -1)

    def test_one_hundred_percent_returns_zero(self):
        self.assertEqual(apply_percentage_discount(100.00, 100), 0.00)

    def test_rounds_discounted_total(self):
        self.assertEqual(apply_percentage_discount(10.01, 33), 6.71)

    def test_rejects_fractional_percent(self):
        with self.assertRaises(ValueError):
            apply_percentage_discount(100.00, 10.5)

if __name__ == "__main__":
    unittest.main()