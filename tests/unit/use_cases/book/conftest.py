from book_store.domain.book.repository import BookRepository


class InMemoryBookRepository(BookRepository):
    def __init__(self, books: list | None = None):
        self.books = books or []

    async def create(self, book):
        self.books.append(book)

    async def list_available_books(self):
        return self.books
