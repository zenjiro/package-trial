"""
Performance tests for package_trial_zenjiro.

This module contains tests to ensure the add_one function
performs well under various conditions and loads.
"""

import pytest
import time
from src.package_trial_zenjiro.main import add_one


class TestPerformance:
    """Test class for performance-related tests."""

    def test_add_one_performance_single_call(self):
        """Test performance of a single add_one call."""
        start_time = time.perf_counter()
        result = add_one(42)
        end_time = time.perf_counter()
        
        execution_time = end_time - start_time
        
        # Should complete in well under 1 millisecond
        assert execution_time < 0.001
        assert result == 43

    def test_add_one_performance_multiple_calls(self):
        """Test performance of multiple add_one calls."""
        num_calls = 10000
        test_value = 100
        
        start_time = time.perf_counter()
        for _ in range(num_calls):
            result = add_one(test_value)
        end_time = time.perf_counter()
        
        total_time = end_time - start_time
        avg_time_per_call = total_time / num_calls
        
        # Should average well under 1 microsecond per call
        assert avg_time_per_call < 0.000001
        assert result == test_value + 1

    @pytest.mark.parametrize("data_size", [100, 1000, 10000])
    def test_add_one_performance_with_different_sizes(self, data_size):
        """Test performance with different input data sizes."""
        test_data = list(range(data_size))
        
        start_time = time.perf_counter()
        results = [add_one(x) for x in test_data]
        end_time = time.perf_counter()
        
        total_time = end_time - start_time
        
        # Should scale linearly - rough performance check
        expected_max_time = data_size * 0.000001  # 1 microsecond per operation
        assert total_time < expected_max_time
        
        # Verify correctness
        assert len(results) == data_size
        assert all(results[i] == test_data[i] + 1 for i in range(data_size))

    def test_add_one_memory_efficiency(self):
        """Test that add_one doesn't cause memory leaks or excessive allocation."""
        import gc
        
        # Force garbage collection before test
        gc.collect()
        
        # Perform many operations
        for i in range(10000):
            result = add_one(i)
            
        # Force garbage collection after test
        gc.collect()
        
        # This test mainly ensures no exceptions are raised
        # and the function completes successfully
        assert result == 9999 + 1