"""Geheimnis-Maskierung."""


def mask_secret(text: str, keep: int = 4) -> str:
    """Maskiert ``text`` und lässt höchstens die letzten ``keep`` Zeichen sichtbar.

    ``keep <= 0`` maskiert vollständig; ``keep >= len(text)`` lässt den Text
    unverändert. Es werden niemals mehr als die letzten ``keep`` Zeichen
    preisgegeben.
    """
    length = len(text)
    if keep <= 0:
        return "*" * length
    if keep >= length:
        return text
    return "*" * (length - keep) + text[length - keep :]
