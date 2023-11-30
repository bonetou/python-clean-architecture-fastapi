from typing import Self


class ISBN:
    def __init__(self, isbn: str):
        self._isbn = self._clean_isbn(isbn)
        if not self._is_valid():
            raise ValueError("Invalid ISBN")

    def _clean_isbn(self, isbn: str):
        return isbn.replace("-", "").replace(" ", "")

    def _is_valid(self):
        if not self._isbn.isdigit():
            return False

        if len(self._isbn) != 13:
            return False

        return True

    @property
    def isbn_code(self):
        return self._isbn

    def __eq__(self, other: Self):
        return self.isbn_code == other.isbn_code
