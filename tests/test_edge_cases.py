"""
Edge case tests for package_trial_zenjiro.
This module focuses on testing edge cases, boundary conditions,
and error scenarios that might not be covered in the main test suite.
"""

import math
import sys
import pytest
from src.package_trial_zenjiro.main import add_one


class TestEdgeCases:
    """Test class for edge cases and boundary conditions."""

    def test_add_one_with_very_large_integers(self):
        """Test add_one with extremely large integers."""
        # Python can handle arbitrarily large integers
        huge_number = 10**100
        result = add_one(huge_number)
        assert result == huge_number + 1
        assert isinstance(result, int)

    def test_add_one_with_very_small_floats(self):
        """Test add_one with very small floating point numbers."""
        tiny_number = 1e-300
        result = add_one(tiny_number)
        assert result == 1.0 + tiny_number
        # Test with smallest positive float
        smallest_float = sys.float_info.min
        result = add_one(smallest_float)
        assert result == 1.0 + smallest_float

    def test_add_one_precision_limits(self):
        """Test add_one at the limits of floating point precision."""
        # Test near machine epsilon
        epsilon = sys.float_info.epsilon
        result = add_one(epsilon)
        assert result == 1.0 + epsilon
        # Test with number smaller than epsilon
        tiny = epsilon / 2
        result = add_one(tiny)
        # Due to floating point precision, this might be exactly 1.0
        assert result >= 1.0

    def test_add_one_with_infinity(self, special_float_values):
        """Test add_one with infinite values."""
        # Positive infinity
        result = add_one(special_float_values["positive_infinity"])
        assert math.isinf(result) and result > 0
        # Negative infinity
        result = add_one(special_float_values["negative_infinity"])
        assert math.isinf(result) and result < 0

    def test_add_one_with_nan(self, special_float_values):
        """Test add_one with NaN (Not a Number)."""
        result = add_one(special_float_values["nan"])
        assert math.isnan(result)

    def test_add_one_boundary_integers(self):
        """Test add_one with boundary integer values."""
        # Test with maximum and minimum values that can be represented
        # For very large integers (Python handles these gracefully)
        max_int_like = 2**63 - 1  # Similar to C long long max
        result = add_one(max_int_like)
        assert result == max_int_like + 1

    def test_add_one_floating_point_edge_cases(self):
        """Test add_one with various floating point edge cases."""
        # Test with -0.0 (negative zero)
        neg_zero = -0.0
        result = add_one(neg_zero)
        assert result == 1.0
        # Test with very close to 1.0
        almost_one = 1.0 - sys.float_info.epsilon
        result = add_one(almost_one)
        assert result == 2.0 - sys.float_info.epsilon

    def test_add_one_type_consistency(self, sample_numbers):
        """Test that add_one maintains type consistency."""
        # Integer inputs should return integers
        for num in sample_numbers["positive_integers"]:
            result = add_one(num)
            assert isinstance(result, int)
        # Float inputs should return floats
        for num in sample_numbers["floats"]:
            result = add_one(num)
            assert isinstance(result, float)

    def test_add_one_mathematical_properties(self):
        """Test mathematical properties of add_one function."""
        # Test commutativity-like property: add_one(x) - 1 == x
        test_values = [0, 1, -1, 5, -5, 1.5, -2.7]
        for x in test_values:
            result = add_one(x)
            assert result - 1 == x

    def test_add_one_repeated_application(self):
        """Test repeated application of add_one."""
        start_value = 0
        current = start_value
        # Apply add_one multiple times
        for i in range(10):
            current = add_one(current)
            assert current == start_value + i + 1

    @pytest.mark.parametrize("decimal_places", [1, 2, 5, 10])
    def test_add_one_decimal_precision(self, decimal_places):
        """Test add_one with various decimal precisions."""
        # Create a number with specific decimal places
        factor = 10**decimal_places
        test_num = 1.0 / factor  # e.g., 0.1, 0.01, 0.00001, etc.
        result = add_one(test_num)
        expected = 1.0 + test_num
        # Use appropriate tolerance for comparison
        tolerance = 1e-15
        assert abs(result - expected) < tolerance
