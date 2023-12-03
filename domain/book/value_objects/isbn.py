from dataclasses import dataclass


@dataclass(frozen=True)
class ISBN:
    isbn: str

    @property
    def formatted(self):
        return self._clean_isbn(self.isbn)

    def __post_init__(self):
        if not self._is_valid():
            raise ValueError("Invalid ISBN")

    def _clean_isbn(self, isbn: str):
        return isbn.replace("-", "").replace(" ", "")

    def _is_valid(self):
        clean_isbn = self._clean_isbn(self.isbn)

        if not clean_isbn.isdigit():
            return False

        if len(clean_isbn) != 13:
            return False

        return True
