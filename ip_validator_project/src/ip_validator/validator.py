# src/ip_validator/validator.py
"""Валидация ip-адресов."""

import re


_IP_RE = re.compile(
    r"^((25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\.){3}(25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)$"
)

#   ^(?P<local>[A-Za-z0-9._%+\-]+)@(?P<domain>[A-Za-z0-9.\-]+)\.(?P<tld>[A-Za-z]{2,})$



def is_valid_ip(ip: str) -> bool:
    """Проверяет, является ли строка синтаксически корректным ip.

    Args:
        ip: строка для проверки.

    Returns:
        True, если ip похож на корректный, иначе False.

    Examples:
        >>> is_valid_ip("192.0.0.1")
        True
        >>> is_valid_ip("192001")
        False
    """
    if not isinstance(ip, str):
        return False
    if not ip or len(ip) > 15:   # RFC: max 15 символов
        return False
    return _IP_RE.match(ip) is not None
