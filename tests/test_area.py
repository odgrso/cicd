import pytest
from src.area import calculate_area_square

@pytest.mark.parametrize("value,expected", [
    (2, 4),
    (2.5, 6.25),
])
def test_calculate_area_square_valid(value, expected):
    assert calculate_area_square(value) == expected

@pytest.mark.parametrize("bad", [-1, 0, "3", [3]])
def test_calculate_area_square_invalid(bad):
    with pytest.raises(TypeError):
        calculate_area_square(bad)
