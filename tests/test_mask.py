"""Tests für die Geheimnis-Maskierung."""

from validkit.mask import mask_secret


def test_mask_secret_keeps_last_four_characters():
    assert mask_secret("geheim1234", keep=4) == "******1234"


def test_mask_secret_default_keep_is_four():
    assert mask_secret("geheim1234") == "******1234"


def test_mask_secret_keep_zero_masks_fully():
    assert mask_secret("geheim1234", keep=0) == "**********"


def test_mask_secret_negative_keep_masks_fully():
    assert mask_secret("geheim1234", keep=-3) == "**********"


def test_mask_secret_keep_larger_than_length_returns_unchanged():
    text = "geheim1234"
    assert mask_secret(text, keep=20) == text
    assert mask_secret(text, keep=len(text)) == text


def test_mask_secret_empty_text():
    assert mask_secret("") == ""
    assert mask_secret("", keep=0) == ""


def test_mask_secret_long_secret():
    text = "a" * 500
    result = mask_secret(text, keep=4)
    assert result == "*" * 496 + "a" * 4
    assert len(result) == len(text)


def test_mask_secret_never_reveals_more_than_keep():
    text = "abcdefgh"
    for keep in range(len(text) + 1):
        result = mask_secret(text, keep=keep)
        assert len(result) == len(text)
        if keep == 0:
            assert result == "*" * len(text)
        else:
            assert result[-keep:] == text[-keep:]
            assert result[:-keep] == "*" * (len(text) - keep)


def test_mask_secret_keep_one_reveals_only_last_character():
    assert mask_secret("secret", keep=1) == "*****t"
