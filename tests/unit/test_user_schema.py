import pytest
from pydantic import ValidationError

from app.schemas.user import UserRegistration



@pytest.mark.parametrize(
    "username, password, expected_username",
    [
        ("alice", "password123", "alice"),
        (" ALICE ", "password123", "alice"),
        ("abc", "password123", "abc"),
        ("a"*50, "password123", "a"*50),
    ]
)
def test_username_valid(username, password, expected_username):
    user=UserRegistration(username=username, password=password)

    assert user.username == expected_username


@pytest.mark.parametrize(
    "username, password",
    [
    ("", "password123"),
    ("  ", "password123"),
    ("ab", "password123"),
    ("a"*51, "password123"),
    ("ali ce", "password123"),
    ("ali\tce", "password123"),
    ("ali\nce", "password123"),
    ]
)
def test_username_invalid(username, password):
    with pytest.raises(ValidationError):
        UserRegistration(username=username, password=password)


@pytest.mark.parametrize(
        "password, should_fail",
        [
            ("1234567", True),
            ("12345678", False),
        ]
)
def test_password_length_boundary(password, should_fail):
    if should_fail:
        with pytest.raises(ValidationError):
            UserRegistration(username="alice", password=password)
    else:
        user=UserRegistration(username="alice", password=password)
        assert user.password == password
