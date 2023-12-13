import pytest

from book_store.domain.book.entity import Book
from book_store.domain.book.exceptions import QuantityGreaterThanCopiesAvailable
from book_store.domain.book.value_objects.isbn import ISBN


def test_it_should_instantiate(lord_of_the_rings_book):
    assert lord_of_the_rings_book


def test_it_should_raise_value_error_when_title_is_empty():
    with pytest.raises(ValueError, match="Title must not be empty"):
        Book(
            isbn=ISBN("978-3-16-148410-0"),
            title="",
            author="J.R.R. Tolkien",
            genres=["Literatura fantástica", "Aventura"],
            price=20.52,
            copies_available=10,
            description="O melhor de todos",
        )


def test_it_should_raise_value_error_when_author_is_empty():
    with pytest.raises(ValueError, match="Author must not be empty"):
        Book(
            isbn=ISBN("978-3-16-148410-0"),
            title="O Senhor dos Anéis: A Sociedade do Anel",
            author="",
            genres=["Literatura fantástica", "Aventura"],
            price=20.52,
            copies_available=10,
            description="O melhor de todos",
        )


def test_it_should_raise_value_error_when_price_is_less_than_zero():
    with pytest.raises(ValueError, match="Price must be greater than or equal to zero"):
        Book(
            isbn=ISBN("978-3-16-148410-0"),
            title="O Senhor dos Anéis: A Sociedade do Anel",
            author="J.R.R. Tolkien",
            genres=["Literatura fantástica", "Aventura"],
            price=-20.52,
            copies_available=10,
            description="O melhor de todos",
        )


def test_it_should_raise_value_error_when_quantity_is_less_than_zero():
    with pytest.raises(ValueError, match="Quantity must be greater than or equal to zero"):
        Book(
            isbn=ISBN("978-3-16-148410-0"),
            title="O Senhor dos Anéis: A Sociedade do Anel",
            author="J.R.R. Tolkien",
            genres=["Literatura fantástica", "Aventura"],
            price=20.52,
            copies_available=-10,
            description="O melhor de todos",
        )


def test_it_should_decrease_quantity_when_selling_book_copies(lord_of_the_rings_book):
    lord_of_the_rings_book.sell_copies(2)
    assert lord_of_the_rings_book.copies_available == 8


def test_it_should_increase_quantity_when_adding_book_copies(lord_of_the_rings_book):
    lord_of_the_rings_book.add_copies(2)
    assert lord_of_the_rings_book.copies_available == 12


def test_it_should_raise_value_error_when_selling_more_copies_than_available(lord_of_the_rings_book):
    with pytest.raises(QuantityGreaterThanCopiesAvailable):
        lord_of_the_rings_book.sell_copies(11)


def test_it_books_should_be_equal_when_isbn_is_the_same(lord_of_the_rings_book):
    another_lord_of_the_rings_book = Book(
        isbn=ISBN("978-3-16-148410-0"),
        title="O Senhor dos Anéis: A Sociedade do Anel",
        author="J.R.R. Tolkien",
        genres=["Literatura fantástica", "Aventura"],
        price=20.52,
        copies_available=10,
        description="O melhor de todos",
    )
    assert lord_of_the_rings_book == another_lord_of_the_rings_book
