from unittest.mock import patch
from code.main import add


@patch("code.main.add")
def test_add(adder):
    adder.return_value = 5
    assert adder.return_value == add(2, 3)
