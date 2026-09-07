"""IBAN-Prüfung."""

_MIN_LENGTH = 15
_MAX_LENGTH = 34


def is_valid_iban(text: str) -> bool:
    """Prüft, ob *text* eine gültige IBAN ist (mod-97-Prüfung).

    Leerzeichen werden entfernt und Groß-/Kleinschreibung ist unerheblich.
    Ungültige Zeichen (weder Ziffer noch lateinischer Buchstabe) führen zu
    einem ``ValueError``, falsche Länge oder falsche Prüfziffer zu ``False``.
    """
    if not isinstance(text, str):
        return False

    normalized = text.upper().replace(" ", "")
    if not normalized:
        return False

    for char in normalized:
        if not ("A" <= char <= "Z" or "0" <= char <= "9"):
            raise ValueError("enthält ungültige Zeichen")

    if not (_MIN_LENGTH <= len(normalized) <= _MAX_LENGTH):
        return False

    rearranged = normalized[4:] + normalized[:4]

    digits: list[str] = []
    for char in rearranged:
        if "A" <= char <= "Z":
            digits.append(str(ord(char) - 55))
        else:
            digits.append(char)

    return int("".join(digits)) % 97 == 1
