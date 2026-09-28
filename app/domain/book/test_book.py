from decimal import Decimal

from app.domain.book.book import Book


book = Book(
    id=None,
    title="Clean Code",
    price=Decimal("30.00")
)

print(book)