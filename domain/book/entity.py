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
        quantity: int,
    ):
        self._isbn = isbn
        self._title = self._validate_title(title)
        self._author = self._validate_author(author)
        self._description = description
        self._genres = genres
        self._price = self._validate_price(price)
        self._quantity = self._validate_quantity(quantity)

    def sell_copies(self, quantity: int):
        if quantity > self.quantity:
            raise QuantityGreaterThanCopiesAvailable
        self._quantity -= quantity

    @property
    def quantity(self):
        return self._quantity

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
