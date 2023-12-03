from tests.unit.use_cases.book.conftest import InMemoryBookRepository
from use_cases.book.list_available.dtos import ListAvailableBooksDTO, BookDetailsDto
from use_cases.book.list_available.use_case import ListAvailableBooksUseCase


async def test_it_should_list_available_books(lord_of_the_rings_book):
    fake_book_repository = InMemoryBookRepository(books=[lord_of_the_rings_book])
    use_case = ListAvailableBooksUseCase(book_repository=fake_book_repository)
    dto = await use_case.execute()
    assert dto == ListAvailableBooksDTO(
        books=[
            BookDetailsDto(
                isbn=lord_of_the_rings_book.isbn.isbn,
                title=lord_of_the_rings_book.title,
                author=lord_of_the_rings_book.author,
                description=lord_of_the_rings_book.description,
                genres=lord_of_the_rings_book.genres,
                price=lord_of_the_rings_book.price,
                copies_available=lord_of_the_rings_book.copies_available,
            ),
        ]
    )


async def test_it_should_list_available_books_when_there_are_no_books():
    fake_book_repository = InMemoryBookRepository(books=[])
    use_case = ListAvailableBooksUseCase(book_repository=fake_book_repository)
    dto = await use_case.execute()
    assert dto == ListAvailableBooksDTO(books=[])
