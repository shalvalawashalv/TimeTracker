import pytest

from app.core.security import hash_password, verify_password



def test_hash_password_differs_from_password():
    password = "password"
    password_hash = hash_password(password)

    assert password != password_hash


def test_verify_password_correct():
    password = "password"
    password_hash = hash_password(password)

    assert verify_password(password, password_hash) is True


def test_verify_password_incorrect():
    password = "password"
    password_hash = hash_password(password)
    
    assert verify_password("wrong_password", password_hash) is False
