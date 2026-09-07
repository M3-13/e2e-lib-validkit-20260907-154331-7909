"""ISBN-13-Prüfung."""


def is_valid_isbn13(text: str) -> bool:
    """Prüft, ob *text* eine gültige ISBN-13 ist.

    Bindestriche und Leerzeichen werden entfernt, danach müssen genau 13
    Ziffern übrig bleiben. Die Prüfsumme wird mit alternierenden Gewichten
    1 und 3 (beginnend mit 1 von links) berechnet; gültig ist die Nummer,
    wenn die Summe durch 10 teilbar ist. Jede andere Länge oder ein
    Nicht-Ziffern-Zeichen ergibt ``False``.
    """
    digits = text.replace("-", "").replace(" ", "")
    if len(digits) != 13 or not digits.isascii() or not digits.isdigit():
        return False
    total = sum(int(digit) * (1 if index % 2 == 0 else 3) for index, digit in enumerate(digits))
    return total % 10 == 0
