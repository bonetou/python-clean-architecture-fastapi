from book_store.domain.book.factory import BookFactory


def test_it_should_create_a_book(lord_of_the_rings_book):
    created_book = BookFactory.create_book(
        isbn=lord_of_the_rings_book.isbn.isbn,
        title=lord_of_the_rings_book.title,
        author=lord_of_the_rings_book.author,
        description=lord_of_the_rings_book.description,
        genres=lord_of_the_rings_book.genres,
        price=lord_of_the_rings_book.price,
        copies_available=lord_of_the_rings_book.copies_available,
    )
    assert created_book == lord_of_the_rings_book


def test_it_should_create_a_book_with_default_values(lord_of_the_rings_book):
    created_book = BookFactory.create_book(
        isbn=lord_of_the_rings_book.isbn.isbn,
        title=lord_of_the_rings_book.title,
        author=lord_of_the_rings_book.author,
        price=lord_of_the_rings_book.price,
    )
    assert created_book.isbn.isbn == lord_of_the_rings_book.isbn.isbn
    assert created_book.title == lord_of_the_rings_book.title
    assert created_book.author == lord_of_the_rings_book.author
    assert created_book.price == lord_of_the_rings_book.price
    assert created_book.genres == []
    assert created_book.description == ""
    assert created_book.copies_available == 0
