import pytest
from src.calculator import add

@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (5, 5, 10),
    (-1, -1, -2),
])
def test_add_multiple_cases(a, b, expected):
    assert add(a, b) == expected
