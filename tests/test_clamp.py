"""Tests für die Wert-Begrenzung ``clamp``."""

import pytest

from validkit import clamp


def test_value_within_interval_is_unchanged():
    assert clamp(5, 0, 10) == 5


def test_value_below_interval_returns_low():
    assert clamp(-3, 0, 10) == 0


def test_value_above_interval_returns_high():
    assert clamp(42, 0, 10) == 10


def test_low_greater_than_high_raises_valueerror():
    with pytest.raises(ValueError):
        clamp(1, 10, 0)


def test_value_equal_to_low_returns_low():
    assert clamp(0, 0, 10) == 0


def test_value_equal_to_high_returns_high():
    assert clamp(10, 0, 10) == 10


def test_negative_bounds():
    assert clamp(-3, -10, -2) == -3
    assert clamp(-100, -10, -2) == -10
    assert clamp(0, -10, -2) == -2


def test_float_values_are_clamped():
    assert clamp(1.5, 0.5, 2.0) == 1.5
    assert clamp(0.1, 0.5, 2.0) == 0.5
    assert clamp(3.7, 0.5, 2.0) == 2.0


def test_error_message_does_not_contain_input_values():
    with pytest.raises(ValueError) as excinfo:
        clamp(123.456, 10, 0)
    message = str(excinfo.value)
    assert "123.456" not in message
    assert "10" not in message
    assert "0" not in message
