from unittest.mock import Mock, patch

from app import add


@patch("app.add")
def test_add(adder: Mock):
    adder.return_value = 5
    assert adder.return_value == add(2, 3)
