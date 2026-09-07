"""Tests für slugify."""

import time

from validkit import slugify


def test_slugify_accents_and_special_chars():
    assert slugify("Héllo Wörld! 123") == "hello-world-123"


def test_slugify_lowercases():
    assert slugify("HELLO WORLD") == "hello-world"


def test_slugify_no_double_hyphens():
    assert slugify("a   b") == "a-b"
    assert slugify("a--b") == "a-b"
    assert slugify("a__b") == "a-b"


def test_slugify_no_leading_or_trailing_hyphens():
    assert slugify("  hello world  ") == "hello-world"
    assert slugify("---hello---") == "hello"
    assert slugify("-hello-world-") == "hello-world"


def test_slugify_only_special_chars():
    assert slugify("!!!") == ""
    assert slugify(" ... ") == ""


def test_slugify_empty_text():
    assert slugify("") == ""


def test_slugify_long_string_terminates_quickly():
    text = "!" * 10000
    start = time.perf_counter()
    result = slugify(text)
    elapsed = time.perf_counter() - start
    assert result == ""
    assert elapsed < 0.1
