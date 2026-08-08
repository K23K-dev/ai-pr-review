import unittest

from src.pricing import CartItem, calculate_subtotal


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


if __name__ == "__main__":
    unittest.main()