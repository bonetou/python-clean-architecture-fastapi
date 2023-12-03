from dataclasses import dataclass


@dataclass
class BookDetailsDto:
    isbn: int
    title: str
    author: str
    description: str
    genres: list[str]
    price: float
    copies_available: int


@dataclass
class ListAvailableBooksDTO:
    books: list[BookDetailsDto]
