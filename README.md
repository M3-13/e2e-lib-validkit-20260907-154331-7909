# validkit

`validkit` ist eine kleine, eigenständige Python-Bibliothek mit neun
unabhängigen, reinen Prüf- und Normalisierungsfunktionen. Jede Funktion ist
sauber typannotiert und nutzt ausschließlich die Python-Standardbibliothek.

## Tech-Stack

- **Sprache**: Python 3.11+
- **Verpackung**: pyproject.toml
- **Tests**: pytest
- **Abhängigkeiten**: nur Standardbibliothek (`re`, `unicodedata` u. a.)

## Installation

```bash
pip install -e .
```

## Tests

```bash
pytest
```

## Verwendung

```python
from validkit import (
    is_valid_email,
    luhn_check,
    is_valid_iban,
    is_valid_isbn13,
    normalize_phone,
    strip_accents,
    mask_secret,
    slugify,
    clamp,
)
```

Für jede Funktion genau ein kurzes, ausführbares Beispiel:

```python
>>> is_valid_email("person@example.com")
True
```

```python
>>> luhn_check("79927398713")
True
```

```python
>>> is_valid_iban("DE89370400440532013000")
True
```

```python
>>> is_valid_isbn13("9780306406157")
True
```

```python
>>> normalize_phone("0170 1234567", "49")
'+491701234567'
```

```python
>>> strip_accents("München café naïve")
'Munchen cafe naive'
```

```python
>>> mask_secret("geheim1234", keep=4)
'******1234'
```

```python
>>> slugify("Héllo Wörld! 123")
'hello-world-123'
```

```python
>>> clamp(5, 0, 10)
5
```

> **Hinweis:** Alle Beispieldaten in dieser README sind fiktiv und dienen
> ausschließlich der Veranschaulichung. E-Mail-Adressen verwenden die
> reservierte Domain `example.com`.

## Lizenz

MIT. Siehe auch die SPDX-Deklaration `MIT` in `pyproject.toml`.
