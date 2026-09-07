"""Tests für die IBAN-Prüfung."""

import pytest

from validkit.iban import is_valid_iban


def test_known_valid_iban_returns_true():
    assert is_valid_iban("DE89370400440532013000") is True


def test_modified_check_digit_returns_false():
    assert is_valid_iban("DE88370400440532013000") is False


def test_invalid_characters_raise_value_error():
    with pytest.raises(ValueError):
        is_valid_iban("DE8937040044053201300!")


def test_iban_with_spaces_returns_true():
    assert is_valid_iban("DE89 3704 0044 0532 0130 00") is True


def test_lowercase_iban_returns_true():
    assert is_valid_iban("de89370400440532013000") is True


def test_empty_input_returns_false():
    assert is_valid_iban("") is False


def test_whitespace_only_returns_false():
    assert is_valid_iban("   ") is False


def test_wrong_length_returns_false():
    assert is_valid_iban("DE89370400440532013") is False


def test_value_error_message_does_not_leak_input():
    bad = "DE89-3704-0044-0532-0130-00"
    with pytest.raises(ValueError) as exc_info:
        is_valid_iban(bad)
    assert bad not in str(exc_info.value)
