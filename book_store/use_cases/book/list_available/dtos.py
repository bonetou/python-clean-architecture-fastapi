from pydantic import BaseModel


class BookDetailsDto(BaseModel):
    isbn: str
    title: str
    author: str
    description: str
    genres: list[str]
    price: float
    copies_available: int


class ListAvailableBooksDTO(BaseModel):
    books: list[BookDetailsDto]
