from decimal import Decimal

from app.domain.book.book import Book
from app.domain.book.book_repository import BookRepository


class UpdateBook:

    def __init__(self, book_repository: BookRepository):
        self.book_repository = book_repository

    def execute(
        self,
        book_id: str,
        title: str,
        price: Decimal
    ) -> Book | None:

        existing_book = self.book_repository.find_by_id(book_id)

        if existing_book is None:
            return None

        updated_book = Book(
            id=book_id,
            title=title,
            price=price
        )

        return self.book_repository.update(updated_book)