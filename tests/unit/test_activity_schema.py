import pytest 
from pydantic import ValidationError

from app.schemas.activity import ActivityCreate


@pytest.mark.parametrize(
        "name, expected",
        [
            ("Reading", "Reading"),
            (" Reading ", "Reading"),
            ("A", "A"),
            ("A"*200, "A"*200),
        ],
)
def test_activity_name_valid(name, expected):
    activity = ActivityCreate(name=name)

    assert activity.name == expected


@pytest.mark.parametrize("name", ["", " ", "A"*201])
def test_activity_name_invalid(name):
    with pytest.raises(ValidationError):
        ActivityCreate(name=name)
