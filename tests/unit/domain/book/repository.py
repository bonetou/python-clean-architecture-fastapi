from abc import ABC, abstractmethod

from domain.book.entity import Book


class BookRepository(ABC):
    @abstractmethod
    async def create(self, book: Book) -> None:
        pass
