from dataclasses import dataclass


@dataclass
class AddBookDTO:
    isbn: str
    title: str
    author: str
    description: str
    genres: list
    price: float
    copies_available: int
