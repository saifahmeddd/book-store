from abc import ABC, abstractmethod

from app.domain.book.book import Book


class BookRepository(ABC):

    @abstractmethod
    def save(self, book: Book) -> Book:
        pass

    @abstractmethod
    def find_by_id(self, book_id: str) -> Book | None:
        pass

    @abstractmethod
    def find_all(self) -> list[Book]:
        pass

    @abstractmethod
    def update(self, book: Book) -> Book:
        pass

    @abstractmethod
    def delete(self, book_id: str) -> bool:
        pass