from app.domain.book.book import Book
from app.domain.book.book_repository import BookRepository


class GetBook:

    def __init__(self, book_repository: BookRepository):
        self.book_repository = book_repository

    def execute(self, book_id: str) -> Book | None:

        return self.book_repository.find_by_id(book_id)