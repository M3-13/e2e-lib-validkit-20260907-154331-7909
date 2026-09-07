"""Luhn-Prüfung Tests."""

import pytest

from validkit.luhn import luhn_check


def test_valid_number_is_true():
    assert luhn_check("79927398713") is True


def test_single_digit_change_is_false():
    assert luhn_check("79927398714") is False


def test_non_digit_raises_value_error():
    with pytest.raises(ValueError):
        luhn_check("12a")


def test_error_message_names_error_kind_only():
    with pytest.raises(ValueError, match="Nicht-Ziffern"):
        luhn_check("12a")


def test_error_message_excludes_input_value():
    with pytest.raises(ValueError) as exc_info:
        luhn_check("12a")
    assert "12a" not in str(exc_info.value)


def test_empty_input_raises_value_error():
    with pytest.raises(ValueError):
        luhn_check("")


def test_int_input_is_accepted():
    assert luhn_check(79927398713) is True
