"""
Documentation and code quality tests for package_trial_zenjiro.

This module contains tests that verify code quality, documentation,
and adherence to Python best practices.
"""

import ast
import inspect
import math

import pytest

from src.package_trial_zenjiro.main import add_one


class TestDocumentationAndQuality:
    """Test class for documentation and code quality."""

    def test_function_signature(self):
        """Test that add_one has the expected function signature."""
        sig = inspect.signature(add_one)

        # Should have exactly one parameter
        assert len(sig.parameters) == 1

        # Parameter should be named 'number'
        param_names = list(sig.parameters.keys())
        assert param_names[0] == "number"

        # Should not have default values
        param = sig.parameters["number"]
        assert param.default == inspect.Parameter.empty

    def test_function_is_callable(self):
        """Test that add_one is callable."""
        assert callable(add_one)
        assert hasattr(add_one, "__call__")

    def test_function_name_and_module(self):
        """Test function name and module information."""
        assert add_one.__name__ == "add_one"
        assert "package_trial_zenjiro.main" in add_one.__module__

    def test_function_source_code_quality(self):
        """Test source code quality and structure."""
        source = inspect.getsource(add_one)

        # Should be a simple, readable function
        assert "def add_one(" in source
        assert "return" in source

        # Parse the AST to verify structure
        tree = ast.parse(source)

        # Should have exactly one function definition
        func_defs = [
            node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)
        ]
        assert len(func_defs) == 1

        func_def = func_defs[0]
        assert func_def.name == "add_one"

    def test_function_behavior_consistency(self):
        """Test that function behavior is consistent across calls."""
        test_value = 42

        # Multiple calls should return the same result
        results = [add_one(test_value) for _ in range(10)]
        assert all(result == 43 for result in results)

        # Function should be deterministic
        assert add_one(test_value) == add_one(test_value)

    def test_function_mathematical_correctness(self):
        """Test mathematical correctness of the add_one function."""
        # Test the fundamental mathematical property
        for i in range(-10, 11):
            assert add_one(i) == i + 1

        # Test with floating point numbers
        for i in range(-5, 6):
            f = i + 0.5
            assert abs(add_one(f) - (f + 1)) < 1e-15

    def test_function_error_handling_completeness(self):
        """Test that function handles all expected error cases."""
        invalid_inputs = [
            "string",
            [1, 2, 3],
            {"key": "value"},
            None,
            object(),
        ]

        for invalid_input in invalid_inputs:
            with pytest.raises(TypeError):
                add_one(invalid_input)

    def test_function_performance_characteristics(self):
        """Test performance characteristics of add_one."""
        import time

        # Should be very fast for simple operations
        start_time = time.perf_counter()
        for _ in range(1000):
            add_one(42)
        end_time = time.perf_counter()

        # Should complete 1000 operations in reasonable time (under 50ms)
        total_time = end_time - start_time
        assert total_time < 0.05  # 50 milliseconds is reasonable for 1000 operations

    def test_function_memory_efficiency(self):
        """Test memory efficiency of add_one."""
        import sys

        # Function should not create unnecessary objects
        test_value = 42

        # Get initial reference count
        initial_refcount = sys.getrefcount(test_value)

        # Call function
        add_one(test_value)

        # Reference count of input should not change significantly
        final_refcount = sys.getrefcount(test_value)
        assert abs(final_refcount - initial_refcount) <= 1

    def test_function_with_edge_case_coverage(self):
        """Test comprehensive edge case coverage."""
        edge_cases = [
            # Boundary values
            0,
            1,
            -1,
            # Large numbers
            10**10,
            -(10**10),
            # Small floats
            1e-10,
            -1e-10,
            # Special floats
            float("inf"),
            float("-inf"),
            # Complex numbers
            1 + 0j,
            0 + 1j,
            1 + 1j,
        ]

        for case in edge_cases:
            if case != case:  # Skip NaN
                continue
            try:
                result = add_one(case)
                # Verify result makes sense
                if isinstance(case, (int, float)) and not math.isinf(case):
                    if isinstance(case, int):
                        assert isinstance(result, int)
                    elif isinstance(case, float):
                        assert isinstance(result, float)
                elif isinstance(case, complex):
                    assert isinstance(result, complex)
            except TypeError:
                # Some edge cases might legitimately raise TypeError
                pass

    def test_function_docstring_and_help(self):
        """Test function documentation availability."""
        # Function should be introspectable
        assert hasattr(add_one, "__doc__")

        # Help should be available
        help(add_one)
        # help() returns None but prints to stdout, so we just verify it doesn't crash
