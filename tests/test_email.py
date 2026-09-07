"""Tests für die E-Mail-Prüfung."""

import time

from validkit import is_valid_email


def test_valid_addresses_are_accepted():
    assert is_valid_email("test@example.com")
    assert is_valid_email("first.last@example.org")
    assert is_valid_email("user.name+tag@sub.example.co.uk")


def test_empty_text_is_invalid():
    assert not is_valid_email("")


def test_missing_at_is_invalid():
    assert not is_valid_email("kein-at")


def test_invalid_characters_are_rejected():
    assert not is_valid_email("test @example.com")
    assert not is_valid_email("test@exam ple.com")
    assert not is_valid_email("te@st@example.com")


def test_domain_without_dot_is_invalid():
    assert not is_valid_email("test@localhost")


def test_long_non_matching_string_terminates_quickly():
    long_text = "a" * 10000 + "@"
    start = time.perf_counter()
    result = is_valid_email(long_text)
    elapsed = time.perf_counter() - start
    assert not result
    assert elapsed < 0.1
