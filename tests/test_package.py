"""Paketstruktur- und öffentliche API-Tests.

Prüft, dass alle neun Funktionen über ``validkit`` importierbar sind und
``validkit.__version__`` vorhanden ist. Die Funktionen selbst werden von den
jeweiligen Feature-Tickets getestet.
"""

import validkit


def test_version_is_available():
    assert hasattr(validkit, "__version__")
    assert isinstance(validkit.__version__, str)
    assert validkit.__version__


def test_all_nine_names_are_importable():
    names = [
        "is_valid_email",
        "luhn_check",
        "is_valid_iban",
        "is_valid_isbn13",
        "normalize_phone",
        "strip_accents",
        "mask_secret",
        "slugify",
        "clamp",
    ]
    for name in names:
        assert hasattr(validkit, name), f"{name} fehlt im Export"
        assert name in validkit.__all__
