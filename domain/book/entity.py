from domain.book.exceptions import QuantityGreaterThanCopiesAvailable
from domain.book.value_objects.isbn import ISBN


class Book:
    def __init__(
        self,
        isbn: ISBN,
        title: str,
        author: str,
        description: str,
        genres: list,
        price: float,
        copies_available: int,
    ):
        self._isbn = isbn
        self._title = self._validate_title(title)
        self._author = self._validate_author(author)
        self._description = description
        self._genres = genres
        self._price = self._validate_price(price)
        self._copies_available = self._validate_quantity(copies_available)

    def sell_copies(self, quantity: int):
        if quantity > self._copies_available:
            raise QuantityGreaterThanCopiesAvailable
        self._copies_available -= quantity

    def add_copies(self, quantity: int):
        self._copies_available += quantity

    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        return self._isbn == other._isbn

    def to_dict(self):
        return {
            "isbn": self._isbn.isbn,
            "title": self._title,
            "author": self._author,
            "description": self._description,
            "genres": self._genres,
            "price": self._price,
            "quantity": self._copies_available,
        }

    @property
    def isbn(self):
        return self._isbn

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def description(self):
        return self._description

    @property
    def genres(self):
        return self._genres

    @property
    def price(self):
        return self._price

    @property
    def copies_available(self):
        return self._copies_available

    def _validate_price(self, price: float):
        if price < 0:
            raise ValueError("Price must be greater than or equal to zero")
        return price

    def _validate_quantity(self, quantity: int):
        if quantity < 0:
            raise ValueError("Quantity must be greater than or equal to zero")
        return quantity

    def _validate_title(self, title: str):
        if not title:
            raise ValueError("Title must not be empty")
        return title

    def _validate_author(self, author: str):
        if not author:
            raise ValueError("Author must not be empty")
        return author
