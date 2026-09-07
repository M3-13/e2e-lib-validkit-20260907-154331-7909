"""Wert-Begrenzung."""


def clamp(value: float, low: float, high: float) -> float:
    """Begrenzt ``value`` auf das Intervall ``[low, high]``.

    Liegt ``value`` außerhalb des Intervalls, wird die jeweils nähere Grenze
    zurückgegeben. Liegt ``value`` innerhalb, bleibt der Wert unverändert.
    Bei ``low > high`` wird ein :class:`ValueError` ausgelöst.
    """
    if low > high:
        raise ValueError("untere Grenze darf nicht größer als obere Grenze sein")
    return max(low, min(value, high))
