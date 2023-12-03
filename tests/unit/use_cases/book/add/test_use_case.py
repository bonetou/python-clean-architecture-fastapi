from tests.unit.domain.book.repository import BookRepository
from use_cases.book.add.use_case import AddBookUseCase
from use_cases.book.add.dtos import AddBookDTO


class InMemoryBookRepository(BookRepository):
    def __init__(self, books: list | None = None):
        self.books = books or []

    async def create(self, book):
        self.books.append(book)


async def test_it_should_create_a_book(lord_of_the_rings_book):
    fake_book_repository = InMemoryBookRepository()
    use_case = AddBookUseCase(book_repository=fake_book_repository)
    dto = AddBookDTO(
        isbn=lord_of_the_rings_book.isbn.isbn,
        title=lord_of_the_rings_book.title,
        author=lord_of_the_rings_book.author,
        description=lord_of_the_rings_book.description,
        genres=lord_of_the_rings_book.genres,
        price=lord_of_the_rings_book.price,
        copies_available=lord_of_the_rings_book.copies_available,
    )

    assert await use_case.execute(dto) == dto
    assert fake_book_repository.books == [lord_of_the_rings_book]
