from decimal import Decimal

from app.domain.book.book import Book
from app.domain.book.book_repository import BookRepository


class CreateBook:

    def __init__(self, book_repository: BookRepository):
        self.book_repository = book_repository

    def execute(
        self,
        title: str,
        price: Decimal
    ) -> Book:

        book = Book(
            id=None,
            title=title,
            price=price
        )

        return self.book_repository.save(book)