# tests/test_validator.py
import pytest

from ip_validator import is_valid_ip



# ---------- Тесты через фикстуры из conftest.py ----------
def test_all_valid_fixture_ips(valid_ips):
    for ip in valid_ips:
        assert is_valid_ip(ip) is True, f"должен быть валидным: r{ip!r}"


def test_all_invalid_fixture_ips(invalid_ips):
    for ip in invalid_ips:
        assert is_valid_ip(ip) is False, f"должен быть невалидным: {ip!r}"


