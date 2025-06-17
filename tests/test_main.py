"""
Tests for the main module of package_trial_zenjiro.

This module contains comprehensive tests for the add_one function,
including normal cases, edge cases, and error handling.
"""

import pytest
from src.package_trial_zenjiro.main import add_one


class TestAddOne:
    """Test class for the add_one function."""

    def test_add_one_positive_integer(self):
        """Test add_one with positive integers."""
        assert add_one(1) == 2
        assert add_one(5) == 6
        assert add_one(100) == 101

    def test_add_one_negative_integer(self):
        """Test add_one with negative integers."""
        assert add_one(-1) == 0
        assert add_one(-5) == -4
        assert add_one(-100) == -99

    def test_add_one_zero(self):
        """Test add_one with zero."""
        assert add_one(0) == 1

    def test_add_one_float(self):
        """Test add_one with floating point numbers."""
        assert add_one(1.5) == 2.5
        # Use approximate comparison for floating point precision
        assert abs(add_one(-2.7) - (-1.7)) < 1e-10
        assert add_one(0.0) == 1.0
        # Test with precision considerations
        result = add_one(0.1)
        assert abs(result - 1.1) < 1e-10

    def test_add_one_large_numbers(self):
        """Test add_one with very large numbers."""
        large_num = 10**15
        assert add_one(large_num) == large_num + 1
        
        # Test with maximum safe integer in Python
        max_safe_int = 2**53 - 1
        assert add_one(max_safe_int) == max_safe_int + 1

    def test_add_one_small_numbers(self):
        """Test add_one with very small numbers."""
        small_num = 1e-15
        result = add_one(small_num)
        assert abs(result - (1 + small_num)) < 1e-15

    def test_add_one_special_float_values(self):
        """Test add_one with special float values."""
        # Test with infinity
        assert add_one(float('inf')) == float('inf')
        assert add_one(float('-inf')) == float('-inf')
        
        # Test with NaN
        result = add_one(float('nan'))
        assert str(result) == 'nan'  # NaN comparison always returns False

    def test_add_one_type_errors(self):
        """Test add_one with invalid input types."""
        with pytest.raises(TypeError):
            add_one("string")
        
        with pytest.raises(TypeError):
            add_one([1, 2, 3])
        
        with pytest.raises(TypeError):
            add_one({"key": "value"})
        
        with pytest.raises(TypeError):
            add_one(None)

    def test_add_one_complex_numbers(self):
        """Test add_one with complex numbers."""
        # Python actually allows complex + int, so test the actual behavior
        result = add_one(1 + 2j)
        expected = (1 + 2j) + 1
        assert result == expected
        assert result == (2 + 2j)

    @pytest.mark.parametrize("input_val,expected", [
        (0, 1),
        (1, 2),
        (-1, 0),
        (10, 11),
        (-10, -9),
        (1.5, 2.5),
        (-1.5, -0.5),
    ])
    def test_add_one_parametrized(self, input_val, expected):
        """Parametrized test for add_one function."""
        assert add_one(input_val) == expected

    def test_add_one_return_type(self):
        """Test that add_one returns the correct type."""
        # Integer input should return integer
        result_int = add_one(5)
        assert isinstance(result_int, int)
        
        # Float input should return float
        result_float = add_one(5.0)
        assert isinstance(result_float, float)

    def test_add_one_immutability(self):
        """Test that add_one doesn't modify the input (for mutable types)."""
        # This is more relevant for mutable types, but good practice
        original_value = 42
        result = add_one(original_value)
        assert original_value == 42  # Original value unchanged
        assert result == 43