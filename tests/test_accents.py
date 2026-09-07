"""Tests für validkit.accents.strip_accents."""

import unicodedata

from validkit.accents import strip_accents


def test_strip_accents_removes_common_accents():
    assert strip_accents("München café naïve") == "Munchen cafe naive"


def test_strip_accents_leaves_text_without_accents_unchanged():
    assert strip_accents("Hallo Welt 123") == "Hallo Welt 123"


def test_strip_accents_handles_empty_string():
    assert strip_accents("") == ""


def test_strip_accents_handles_precomposed_and_combining_chars():
    precomposed = "caf\u00e9"  # "café"
    decomposed = "cafe\u0301"  # "cafe" + combining acute
    assert strip_accents(precomposed) == "cafe"
    assert strip_accents(decomposed) == "cafe"


def test_strip_accents_removes_various_marks():
    assert strip_accents("\u00e0\u00e8\u00ec\u00f2\u00f9") == "aeiou"
    assert strip_accents("\u00e4\u00f6\u00fc\u00df") == "aou\u00df"


def test_strip_accents_keeps_non_mn_characters():
    assert strip_accents("1234567890!?., ") == "1234567890!?., "


def test_strip_accents_matches_nfd_removal():
    text = "na\u00efve"
    assert strip_accents(text) == "naive"
    assert unicodedata.normalize("NFC", strip_accents(text)) == "naive"
