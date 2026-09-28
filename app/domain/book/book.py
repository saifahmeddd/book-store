from dataclasses import dataclass
from decimal import Decimal

@dataclass
class Book:
    id: str | None
    title: str
    price: Decimal

    def __post_init__(self):
        if not self.title.strip():
            raise ValueError("Book title is required")

        if self.price < 0:
            raise ValueError("Book price cannot be negative")