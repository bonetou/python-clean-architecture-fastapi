import pytest

from domain.book.entity import Book
from domain.book.exceptions import QuantityGreaterThanCopiesAvailable
from domain.book.value_objects.isbn import ISBN


@pytest.fixture
def lord_of_the_rings_book():
    return Book(
        isbn=ISBN("978-3-16-148410-0"),
        title="O Senhor dos Anéis: A Sociedade do Anel",
        author="J.R.R. Tolkien",
        genres=["Literatura fantástica", "Aventura"],
        price=20.52,
        quantity=10,
        description="O melhor de todos",
    )


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
            quantity=10,
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
            quantity=10,
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
            quantity=10,
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
            quantity=-10,
            description="O melhor de todos",
        )


def test_it_should_decrease_quantity_when_selling_book_copies(lord_of_the_rings_book):
    lord_of_the_rings_book.sell_copies(2)
    assert lord_of_the_rings_book.quantity == 8


def test_it_should_raise_value_error_when_selling_more_copies_than_available(lord_of_the_rings_book):
    with pytest.raises(QuantityGreaterThanCopiesAvailable):
        lord_of_the_rings_book.sell_copies(11)
