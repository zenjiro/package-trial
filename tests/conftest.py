"""
Pytest configuration and shared fixtures for package_trial_zenjiro tests.

This file contains common test fixtures and configuration that can be
shared across all test modules.
"""

import sys
from pathlib import Path

import pytest

# Add src directory to Python path for imports
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))


@pytest.fixture
def sample_numbers():
    """Fixture providing a variety of test numbers."""
    return {
        "positive_integers": [1, 5, 10, 100, 1000],
        "negative_integers": [-1, -5, -10, -100, -1000],
        "zero": 0,
        "floats": [1.5, -2.7, 0.1, 3.14159, -0.5],
        "large_numbers": [10**10, 10**15, 2**53 - 1],
        "small_numbers": [1e-10, 1e-15, 1e-100],
    }


@pytest.fixture
def invalid_inputs():
    """Fixture providing invalid input types for testing error handling."""
    return [
        "string",
        [1, 2, 3],
        {"key": "value"},
        None,
        (1, 2),
        set([1, 2, 3]),
        1 + 2j,  # complex number
    ]


@pytest.fixture
def special_float_values():
    """Fixture providing special floating point values."""
    return {
        "positive_infinity": float("inf"),
        "negative_infinity": float("-inf"),
        "nan": float("nan"),
    }
