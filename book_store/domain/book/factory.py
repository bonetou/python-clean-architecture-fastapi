from book_store.domain.book.entity import Book
from book_store.domain.book.value_objects.isbn import ISBN


class BookFactory:
    @staticmethod
    def create_book(
        isbn: str,
        title: str,
        author: str,
        price: float,
        genres: list[str] | None = None,
        description: str = "",
        copies_available: int = 0,
    ) -> Book:
        return Book(
            isbn=ISBN(isbn),
            title=title,
            author=author,
            genres=genres or [],
            description=description,
            price=price,
            copies_available=copies_available,
        )
