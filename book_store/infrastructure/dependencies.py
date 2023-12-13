from typing import Annotated

from fastapi import Depends

from book_store.use_cases.book.add.use_case import AddBookUseCase
from book_store.use_cases.book.list_available.use_case import ListAvailableBooksUseCase
from tests.unit.domain.book.repository import BookRepository


class InMemoryBookRepository(BookRepository):
    def __init__(self):
        self.books = []

    async def create(self, book):
        self.books.append(book)

    async def list_available_books(self):
        return self.books


def in_memory_book_repository():
    return InMemoryBookRepository()


def list_available_books_use_case(
    repository: Annotated[BookRepository, Depends(in_memory_book_repository)],
) -> ListAvailableBooksUseCase:
    return ListAvailableBooksUseCase(repository)


def add_book_use_case(repository: Annotated[BookRepository, Depends(in_memory_book_repository)]) -> AddBookUseCase:
    return AddBookUseCase(repository)
