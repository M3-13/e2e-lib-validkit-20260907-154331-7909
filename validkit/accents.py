"""Akzent-Entfernung."""

import unicodedata


def strip_accents(text: str) -> str:
    """Entfernt Akzente und diakritische Zeichen aus ``text``.

    Der Text wird zuerst mit Unicode-Normalisierung NFD in Grundzeichen und
    Kombinationszeichen zerlegt; anschließend werden alle Kombinationszeichen
    der Kategorie ``Mn`` entfernt. Zeichen ohne Akzent bleiben unverändert.
    """
    normalized = unicodedata.normalize("NFD", text)
    return "".join(char for char in normalized if unicodedata.category(char) != "Mn")
