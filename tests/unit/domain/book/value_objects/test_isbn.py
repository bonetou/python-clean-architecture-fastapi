import pytest

from domain.book.value_objects.isbn import ISBN


def test_valid_isbn_code():
    assert ISBN("978-8595084742")


def test_should_return_code_formatted():
    isbn = ISBN("978-8595084742")
    assert isbn.isbn_code == "9788595084742"


def test_should_be_invalid_when_length_is_not_13():
    with pytest.raises(ValueError, match="Invalid ISBN"):
        ISBN("123456")


def test_should_be_invalid_when_does_not_contain_only_digits():
    with pytest.raises(ValueError, match="Invalid ISBN"):
        ISBN("A78-8595084742")


def test_two_isbn_with_same_code_should_be_equal():
    assert ISBN("978-8595084742") == ISBN("978-8595084742")
