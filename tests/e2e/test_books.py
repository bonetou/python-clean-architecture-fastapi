import pytest
from starlette import status

from book_store.infrastructure.dependencies import in_memory_book_repository, InMemoryBookRepository


@pytest.fixture
def add_book_valid_payload():
    return {
        "isbn": "978-0544003415",
        "title": "The Lord of the Rings",
        "author": "J. R. R. Tolkien",
        "description": "The Lord of the Rings ...",
        "genres": ["fantasy"],
        "price": 10.0,
        "copies_available": 10,
    }


def test_it_should_add_a_new_book(test_client, add_book_valid_payload):
    response = test_client.post("/books", json=add_book_valid_payload)
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == add_book_valid_payload


def test_it_should_respond_with_bad_request_when_payload_is_invalid(test_client, add_book_valid_payload):
    invalid_payload = {
        **add_book_valid_payload,
        "isbn": "1234",
        "title": "",
        "author": "",
        "price": 0,
        "copies_available": 0,
    }
    response = test_client.post("/books", json=invalid_payload)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert response.json() == {
        "detail": [
            {
                "ctx": {"error": {}},
                "input": "1234",
                "loc": ["body", "isbn"],
                "msg": "Value error, Invalid ISBN",
                "type": "value_error",
                "url": "https://errors.pydantic.dev/2.5/v/value_error",
            },
            {
                "ctx": {"error": {}},
                "input": "",
                "loc": ["body", "title"],
                "msg": "Assertion failed, Must not be empty",
                "type": "assertion_error",
                "url": "https://errors.pydantic.dev/2.5/v/assertion_error",
            },
            {
                "ctx": {"error": {}},
                "input": "",
                "loc": ["body", "author"],
                "msg": "Assertion failed, Must not be empty",
                "type": "assertion_error",
                "url": "https://errors.pydantic.dev/2.5/v/assertion_error",
            },
            {
                "ctx": {"gt": 0},
                "input": 0,
                "loc": ["body", "copies_available"],
                "msg": "Input should be greater than 0",
                "type": "greater_than",
                "url": "https://errors.pydantic.dev/2.5/v/greater_than",
            },
        ]
    }


async def test_it_should_list_available_books(test_client, add_book_valid_payload, lord_of_the_rings_book):
    from tests.e2e.conftest import app

    async def override_repo():
        book = lord_of_the_rings_book
        repo = InMemoryBookRepository()
        await repo.create(book=book)
        return repo

    app.dependency_overrides[in_memory_book_repository] = override_repo
    test_client.post("/books", json=add_book_valid_payload)
    response = test_client.get("/books")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [lord_of_the_rings_book.to_dict()]
    app.dependency_overrides = {}
