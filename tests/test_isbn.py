"""Tests für die ISBN-13-Prüfung."""

from validkit.isbn import is_valid_isbn13


def test_valid_isbn13():
    assert is_valid_isbn13("9780306406157") is True


def test_wrong_checksum_digit_is_false():
    assert is_valid_isbn13("9780306406158") is False


def test_twelve_digits_is_false():
    assert is_valid_isbn13("978030640615") is False


def test_isbn13_with_hyphens():
    assert is_valid_isbn13("978-0-306-40615-7") is True


def test_isbn13_with_spaces():
    assert is_valid_isbn13("978 0 306 40615 7") is True


def test_non_digit_characters_is_false():
    assert is_valid_isbn13("9780X06406157") is False


def test_empty_string_is_false():
    assert is_valid_isbn13("") is False
