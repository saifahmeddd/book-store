from app.domain.book.book import Book
from app.domain.book.book_repository import BookRepository


class GetBooks:

    def __init__(self, book_repository: BookRepository):
        self.book_repository = book_repository

    def execute(self) -> list[Book]:

        return self.book_repository.find_all()