"""Tests für validkit.phone.normalize_phone."""

import pytest

from validkit.phone import normalize_phone


def test_normalizes_local_number_with_leading_zero():
    assert normalize_phone("0170 1234567", "49") == "+491701234567"


def test_normalizes_number_already_with_country_code():
    assert normalize_phone("+49 170 1234567", "49") == "+491701234567"
    assert normalize_phone("491701234567", "49") == "+491701234567"


def test_normalizes_formatting_variants():
    assert normalize_phone("0170-123-4567", "49") == "+491701234567"
    assert normalize_phone("(0170) 1234567", "49") == "+491701234567"


def test_country_code_with_plus_sign_is_accepted():
    assert normalize_phone("0170 1234567", "+49") == "+491701234567"


def test_input_without_digits_raises_value_error():
    for value in ("abc", "", "---", "   "):
        with pytest.raises(ValueError):
            normalize_phone(value, "49")


def test_country_code_without_digits_raises_value_error():
    with pytest.raises(ValueError):
        normalize_phone("0170 1234567", "")


def test_error_message_does_not_contain_input():
    with pytest.raises(ValueError) as excinfo:
        normalize_phone("geheim-nicht-oeffentlich", "49")
    assert "geheim" not in str(excinfo.value)
    assert "nicht-oeffentlich" not in str(excinfo.value)
