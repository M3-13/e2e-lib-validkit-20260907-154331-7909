"""E-Mail-Prüfung."""

import re

# Die Zeichenklassen sind jeweils atomar (eine Klasse pro Quantor) und werden
# über ``fullmatch`` mit dem kompletten String verglichen. Es gibt keine
# verschachtelten Quantoren über derselben Zeichenmenge, daher ist kein
# katastrophales Backtracking möglich; lange, nicht passende Strings werden
# linear abgearbeitet.
_EMAIL_RE = re.compile(
    r"[A-Za-z0-9.!#$%&'*+/=?^_`{|}~-]+"
    r"@"
    r"[A-Za-z0-9](?:[A-Za-z0-9.-]*[A-Za-z0-9])?"
    r"\."
    r"[A-Za-z]{2,}"
)


def is_valid_email(text: str) -> bool:
    """Prüft grundlegende E-Mail-Gültigkeit.

    Akzeptiert einen nicht-leeren lokalen Teil, genau ein ``@`` und eine
    Domain mit mindestens einem Punkt und plausiblen Zeichen. Leerer Text,
    fehlendes ``@`` oder ein ungültiges Format liefern ``False`` (kein
    ``ValueError`` für Formatfehler).
    """
    return _EMAIL_RE.fullmatch(text) is not None
