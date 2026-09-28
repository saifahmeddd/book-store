from app.application.book.create_book import CreateBook
from app.application.book.get_book import GetBook
from app.application.book.get_books import GetBooks
from app.application.book.update_book import UpdateBook
from app.application.book.delete_book import DeleteBook

from app.infrastructure.firebase.firebase_config import (
    create_firestore_client
)

from app.infrastructure.firebase.firebase_book_repository import (
    FirebaseBookRepository
)


db = create_firestore_client()

book_repository = FirebaseBookRepository(db)


create_book = CreateBook(book_repository)

get_book = GetBook(book_repository)

get_books = GetBooks(book_repository)

update_book = UpdateBook(book_repository)

delete_book = DeleteBook(book_repository)