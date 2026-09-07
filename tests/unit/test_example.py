from src.example import square
import pytest


@pytest.mark.unit
def test_square():
    # Arrange
    test_data = 10
    expected = 100

    # Act
    actual = square(test_data)

    # Assert
    assert actual == expected
