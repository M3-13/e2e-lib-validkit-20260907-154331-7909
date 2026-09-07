"""Slug-Erzeugung."""

import re
import unicodedata

_NON_SLUG_CHARS = re.compile(r"[^a-z0-9]+")


def slugify(text: str) -> str:
    """Erzeugt aus ``text`` einen URL-tauglichen Slug.

    Akzente werden per NFD-Normalisierung und Entfernen der Combining-Marks
    beseitigt, der Text wird kleingeschrieben, alle Zeichen außer ``a-z`` und
    ``0-9`` werden durch ``-`` ersetzt, mehrfache Bindestriche zusammengeführt
    und führende/abschließende Bindestriche entfernt.

    Der reguläre Ausdruck ``[^a-z0-9]+`` ist eine negierte Zeichenklasse mit
    einem einzelnen Quantor und erlaubt daher kein katastrophales Backtracking.
    """
    decomposed = unicodedata.normalize("NFD", text)
    ascii_text = "".join(c for c in decomposed if not unicodedata.combining(c))
    slug = _NON_SLUG_CHARS.sub("-", ascii_text.lower())
    return slug.strip("-")
