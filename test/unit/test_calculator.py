from unittest.mock import Mock, patch

from src.app import add


@patch("src.app.add")
def test_add(adder: Mock):
    adder.return_value = 5
    assert adder.return_value == add(2, 3)
