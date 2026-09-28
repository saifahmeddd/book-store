from app.domain.book.book_repository import BookRepository


class DeleteBook:

    def __init__(self, book_repository: BookRepository):
        self.book_repository = book_repository

    def execute(self, book_id: str) -> bool:

        return self.book_repository.delete(book_id)