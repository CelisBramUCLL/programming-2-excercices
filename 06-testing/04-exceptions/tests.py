import pytest
from book import Book


@pytest.mark.parametrize("title, isbn", [("Bram", "978-3-16-148410-0")])
def test_valid_creation(title, isbn):
    book = Book(title, isbn)

    assert book.title == title
    assert book.isbn == isbn


@pytest.mark.parametrize(
    "title, isbn", [("", "978-3-16-148410-0"), (None, "978-3-16-148410-0")]
)
def test_creation_with_invalid_title(title, isbn):
    with pytest.raises(Exception):
        Book(title, isbn)


@pytest.mark.parametrize(
    "title, isbn",
    [
        ("Bram", "978-3-16-148410-2"),
        ("Bram", "978-3-16-148410"),
        ("Bram", "978-3-16-148410-23"),
    ],
)
def test_creation_with_invalid_isbn(title, isbn):
    with pytest.raises(RuntimeError):
        Book(title, isbn)
