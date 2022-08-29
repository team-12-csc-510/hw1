from code.main import add
from unittest.mock import Mock, patch


@patch("code.main.add")
def test_add(adder: Mock):
    adder.return_value = 5
    assert adder.return_value == add(2, 3)
