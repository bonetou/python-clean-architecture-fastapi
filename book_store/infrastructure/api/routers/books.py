from typing import Annotated

from fastapi import APIRouter, Depends
from pydantic import BaseModel, PositiveInt, NonNegativeFloat, AfterValidator
from starlette import status

from book_store.domain.book.value_objects.isbn import ISBN
from book_store.infrastructure.dependencies import list_available_books_use_case, add_book_use_case
from book_store.use_cases.book.add.dtos import AddBookDTO
from book_store.use_cases.book.add.use_case import AddBookUseCase
from book_store.use_cases.book.list_available.use_case import ListAvailableBooksUseCase

books_router = APIRouter(prefix="/books", tags=["Books"])


def non_empty_string_validator(v):
    assert len(v) > 0, "Must not be empty"
    return v


def valid_isbn(v):
    ISBN(v)
    return v


NonEmptyString = Annotated[str, AfterValidator(non_empty_string_validator)]
ValidISBN = Annotated[str, AfterValidator(valid_isbn)]


class AddBookPayload(BaseModel):
    isbn: ValidISBN
    title: NonEmptyString
    author: NonEmptyString
    description: str = ""
    genres: list[str] = []
    price: NonNegativeFloat
    copies_available: PositiveInt

    def to_dto(self) -> AddBookDTO:
        return AddBookDTO(
            isbn=self.isbn,
            title=self.title,
            author=self.author,
            description=self.description,
            genres=self.genres,
            price=self.price,
            copies_available=self.copies_available,
        )


@books_router.post("/", status_code=status.HTTP_201_CREATED)
async def add_new_book(
    payload: AddBookPayload,
    use_case: Annotated[AddBookUseCase, Depends(add_book_use_case)],
):
    books = await use_case.execute(dto=payload.to_dto())
    return books


@books_router.get("/")
async def list_available_books(use_case: Annotated[ListAvailableBooksUseCase, Depends(list_available_books_use_case)]):
    books = await use_case.execute()
    return [book.model_dump() for book in books.books]
