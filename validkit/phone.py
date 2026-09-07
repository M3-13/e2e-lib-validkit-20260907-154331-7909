"""Telefonnummer-Normalisierung."""

import re


def normalize_phone(text: str, country_code: str) -> str:
    """Normalisiert eine Telefonnummer in internationales Format.

    Entfernt alle Nicht-Ziffern aus ``text``, ersetzt eine führende ``0`` durch
    die Ziffernfolge von ``country_code`` (ohne ``+``) und liefert das Ergebnis
    als ``+<land><nummer>`` zurück. Enthält die Nummer bereits die
    Landeskennzahl, bleibt sie unverändert (nur das ``+`` wird vorangestellt).

    Wirft ``ValueError``, wenn die Eingabe keine Ziffern enthält oder nicht
    normalisiert werden kann. Die Fehlermeldung nennt ausschließlich die
    Fehlerart und keinen Eingabewert.
    """
    digits = re.sub(r"\D", "", text)
    cc = re.sub(r"\D", "", country_code)

    if not cc:
        raise ValueError("Landeskennzahl enthält keine Ziffern")
    if not digits:
        raise ValueError("enthält keine Ziffern")

    if digits.startswith(cc):
        number = digits
    elif digits.startswith("0"):
        number = cc + digits[1:]
    else:
        number = cc + digits

    if not number:
        raise ValueError("nicht normalisierbar")

    return "+" + number
