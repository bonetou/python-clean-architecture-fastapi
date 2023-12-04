from book_store.domain.book.entity import Book
from tests.unit.domain.book.repository import BookRepository
from book_store.use_cases.book.list_available.dtos import ListAvailableBooksDTO, BookDetailsDto


class ListAvailableBooksUseCase:
    def __init__(self, book_repository: BookRepository):
        self._book_repository = book_repository

    async def execute(self) -> ListAvailableBooksDTO:
        books = await self._book_repository.list_available_books()
        dto = ListAvailableBooksDTO(books=[self._get_book_details(book) for book in books])
        return dto

    def _get_book_details(self, book: Book):
        return BookDetailsDto(
            isbn=book.isbn.isbn,
            title=book.title,
            author=book.author,
            description=book.description,
            genres=book.genres,
            price=book.price,
            copies_available=book.copies_available,
        )
