from decimal import Decimal

from app.domain.book.book import Book
from app.domain.book.book_repository import BookRepository


class FirebaseBookRepository(BookRepository):

    def __init__(self, db):
        self.db = db

    def save(self, book: Book) -> Book:

        book_data = {
            "title": book.title,
            "price": str(book.price)
        }

        document_ref = self.db.collection("books").document()

        document_ref.set(book_data)

        return Book(
            id=document_ref.id,
            title=book.title,
            price=book.price
        )

    def find_by_id(self, book_id: str) -> Book | None:

        document_ref = (
            self.db
            .collection("books")
            .document(book_id)
        )

        document = document_ref.get()

        if not document.exists:
            return None

        data = document.to_dict()

        return Book(
            id=document.id,
            title=data["title"],
            price=Decimal(data["price"])
        )

    def find_all(self) -> list[Book]:

        documents = self.db.collection("books").stream()

        books = []

        for document in documents:

            data = document.to_dict()

            book = Book(
                id=document.id,
                title=data["title"],
                price=Decimal(data["price"])
            )

            books.append(book)

        return books

    def update(self, book: Book) -> Book:

        document_ref = (
            self.db
            .collection("books")
            .document(book.id)
        )

        document_ref.update({
            "title": book.title,
            "price": str(book.price)
        })

        return book

    def delete(self, book_id: str) -> bool:

        document_ref = (
            self.db
            .collection("books")
            .document(book_id)
        )

        document = document_ref.get()

        if not document.exists:
            return False

        document_ref.delete()

        return True