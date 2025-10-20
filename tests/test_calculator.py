import pytest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from calculator import add, subtract, multiply, divide, power


class TestCalculator:

    def test_add(self):
        assert add(2, 3) == 5
        assert add(-1, 1) == 0
        assert add(0, 0) == 0

    def test_subtract(self):
        assert subtract(5, 3) == 2
        assert subtract(0, 5) == -5
        assert subtract(10, 10) == 0

    def test_multiply(self):
        assert multiply(3, 4) == 12
        assert multiply(0, 5) == 0
        assert multiply(-2, 3) == -6

    def test_divide(self):
        assert divide(10, 2) == 5
        assert divide(5, 2) == 2.5
        assert divide(0, 5) == 0

    def test_divide_by_zero(self):
        with pytest.raises(ValueError, match="Cannot divide by zero!"):
            divide(10, 0)

    def test_power(self):
        assert power(2, 3) == 8
        assert power(5, 0) == 1
        assert power(4, 0.5) == 2.0