from app.domain.book.book_repository import BookRepository


class FakeBookRepository(BookRepository):

    def save(self, book):
        return book

    def find_by_id(self, book_id):
        return None


repository = FakeBookRepository()

print("Repository works!")