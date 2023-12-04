import pytest

from book_store.domain.book.entity import Book
from book_store.domain.book.value_objects.isbn import ISBN


@pytest.fixture
def lord_of_the_rings_book():
    return Book(
        isbn=ISBN("978-3-16-148410-0"),
        title="O Senhor dos Anéis: A Sociedade do Anel",
        author="J.R.R. Tolkien",
        genres=["Literatura fantástica", "Aventura"],
        price=20.52,
        copies_available=10,
        description="O melhor de todos",
    )
