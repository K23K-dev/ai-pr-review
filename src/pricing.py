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