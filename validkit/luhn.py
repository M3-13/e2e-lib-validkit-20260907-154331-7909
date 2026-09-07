"""Luhn-Prüfung."""


def luhn_check(digits: str | int) -> bool:
    """Prüft eine Ziffernfolge mit dem Luhn-Algorithmus.

    ``digits`` kann ein ``str`` oder ein ``int`` sein. Nicht-Ziffern oder eine
    leere Eingabe führen zu einem ``ValueError``, dessen Meldung ausschließlich
    die Fehlerart nennt und niemals den übergebenen Eingabewert.
    """
    if isinstance(digits, int):
        text = str(digits)
    elif isinstance(digits, str):
        text = digits
    else:
        raise ValueError("enthält Nicht-Ziffern")

    if not text:
        raise ValueError("leere Eingabe")

    if not text.isdigit():
        raise ValueError("enthält Nicht-Ziffern")

    total = 0
    for index, char in enumerate(reversed(text)):
        digit = int(char)
        if index % 2 == 1:
            digit *= 2
            if digit > 9:
                digit -= 9
        total += digit

    return total % 10 == 0
