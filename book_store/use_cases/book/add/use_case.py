from book_store.domain.book.factory import BookFactory
from book_store.use_cases.book.add.dtos import AddBookDTO
from book_store.domain.book.repository import BookRepository


class AddBookUseCase:
    def __init__(self, book_repository: BookRepository):
        self.book_repository = book_repository

    async def execute(self, dto: AddBookDTO) -> AddBookDTO:
        book = BookFactory.create_book(
            isbn=dto.isbn,
            title=dto.title,
            author=dto.author,
            price=dto.price,
            genres=dto.genres,
            description=dto.description,
            copies_available=dto.copies_available,
        )
        await self.book_repository.create(book)
        return dto
