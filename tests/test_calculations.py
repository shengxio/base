"""Unit tests for calculation functions."""
import pytest
from src.app import calculate_sum

class TestCalculateSum:
    """Tests for the calculate_sum function."""

    @pytest.mark.parametrize("a, b, expected", [
        (1, 2, 3),            # Positive numbers
        (-1, 1, 0),           # Mixed positive and negative
        (0, 0, 0),            # Zeros
        (-5, -3, -8),         # Negative numbers
        (999, 1, 1000),       # Large numbers
        (2**30, 2**30, 2**31) # Very large numbers
    ])
    def test_calculate_sum_valid(self, a, b, expected):
        """Test calculate_sum with valid inputs."""
        assert calculate_sum(a, b) == expected

    def test_calculate_sum_type_error(self):
        """Test calculate_sum with invalid input types."""
        with pytest.raises(TypeError):
            calculate_sum("1", 2)
        with pytest.raises(TypeError):
            calculate_sum(1, "2")
        with pytest.raises(TypeError):
            calculate_sum(None, 2)
        with pytest.raises(TypeError):
            calculate_sum(1, None)

    @pytest.mark.regression
    def test_calculate_sum_regression(self):
        """Regression tests for previously fixed issues."""
        # Example regression tests - add actual cases here when bugs are fixed
        assert calculate_sum(0, -0) == 0  # Handling of negative zero
        assert calculate_sum(2**31 - 1, 1) > 0  # Overflow handling

    @pytest.mark.parametrize("a, b", [
        (2**31, 1),       # Number too large for 32-bit int
        (-2**31 - 1, 0),  # Number too small for 32-bit int
    ])
    def test_calculate_sum_large_numbers(self, a, b):
        """Test calculate_sum with numbers at the edges of integer range."""
        result = calculate_sum(a, b)
        assert isinstance(result, int)

    def test_calculate_sum_identity(self):
        """Test mathematical properties of addition."""
        # Identity property: a + 0 = a
        assert calculate_sum(5, 0) == 5
        assert calculate_sum(0, 5) == 5

        # Commutative property: a + b = b + a
        a, b = 5, 3
        assert calculate_sum(a, b) == calculate_sum(b, a)

    @pytest.mark.benchmark
    def test_calculate_sum_performance(self, benchmark):
        """Test performance of calculate_sum function."""
        def run_calculation():
            for _ in range(1000):
                calculate_sum(42, 58)
        
        # Run the benchmark
        benchmark(run_calculation) 