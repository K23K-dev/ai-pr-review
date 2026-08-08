from dataclasses import dataclass


@dataclass(frozen=True)
class CartItem:
    name: str
    price: float
    quantity: int = 1


def calculate_subtotal(items: list[CartItem]) -> float:
    total = 0.0

    for item in items:
        if item.price < 0:
            raise ValueError("Price cannot be negative")

        if item.quantity < 1:
            raise ValueError("Quantity must be at least 1")

        total += item.price * item.quantity

    return round(total, 2)

def apply_percentage_discount(subtotal: float, percent: float) -> float:
    """Apply a whole-number percentage where 10 represents 10%."""

    if subtotal < 0:
        raise ValueError("Subtotal cannot be negative")

    if percent < 0 or percent > 100:
        raise ValueError("Percent must be between 0 and 100")

    return round(subtotal * (1 - percent), 2)