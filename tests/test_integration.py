"""
Integration tests for package_trial_zenjiro.

This module contains integration tests that verify the package
works correctly as a whole and can be imported and used properly.
"""

import pytest
import importlib
import sys
from pathlib import Path


class TestIntegration:
    """Test class for integration scenarios."""

    def test_package_import(self):
        """Test that the package can be imported correctly."""
        # Test importing the main module
        from src.package_trial_zenjiro import main
        assert hasattr(main, 'add_one')
        
        # Test importing the function directly
        from src.package_trial_zenjiro.main import add_one
        assert callable(add_one)

    def test_package_structure(self):
        """Test that the package structure is correct."""
        # Check that __init__.py exists
        init_file = Path("src/package_trial_zenjiro/__init__.py")
        assert init_file.exists()
        
        # Check that main.py exists
        main_file = Path("src/package_trial_zenjiro/main.py")
        assert main_file.exists()

    def test_function_accessibility(self):
        """Test that functions are accessible through different import methods."""
        # Method 1: Import module and access function
        from src.package_trial_zenjiro import main
        result1 = main.add_one(5)
        assert result1 == 6
        
        # Method 2: Import function directly
        from src.package_trial_zenjiro.main import add_one
        result2 = add_one(5)
        assert result2 == 6
        
        # Both methods should give same result
        assert result1 == result2

    def test_module_reloading(self):
        """Test that the module can be reloaded without issues."""
        # Import the module
        from src.package_trial_zenjiro import main
        
        # Use the function
        result1 = main.add_one(10)
        
        # Reload the module
        importlib.reload(main)
        
        # Use the function again
        result2 = main.add_one(10)
        
        # Results should be the same
        assert result1 == result2 == 11

    def test_function_in_different_contexts(self):
        """Test add_one function in various usage contexts."""
        from src.package_trial_zenjiro.main import add_one
        
        # Test in list comprehension
        numbers = [1, 2, 3, 4, 5]
        results = [add_one(x) for x in numbers]
        assert results == [2, 3, 4, 5, 6]
        
        # Test with map function
        mapped_results = list(map(add_one, numbers))
        assert mapped_results == [2, 3, 4, 5, 6]
        
        # Test in generator expression
        gen_results = list(add_one(x) for x in numbers)
        assert gen_results == [2, 3, 4, 5, 6]

    def test_function_as_parameter(self):
        """Test passing add_one as a parameter to other functions."""
        from src.package_trial_zenjiro.main import add_one
        
        def apply_function(func, value):
            return func(value)
        
        result = apply_function(add_one, 42)
        assert result == 43

    def test_function_documentation(self):
        """Test that function has proper documentation."""
        from src.package_trial_zenjiro.main import add_one
        
        # Function should exist and be callable
        assert callable(add_one)
        
        # Function should have a name
        assert add_one.__name__ == 'add_one'

    def test_package_in_sys_modules(self):
        """Test that package modules are properly registered in sys.modules."""
        # Import the package
        from src.package_trial_zenjiro import main
        
        # Check if module is in sys.modules
        module_names = [name for name in sys.modules.keys() 
                       if 'package_trial_zenjiro' in name]
        
        assert len(module_names) > 0
        assert any('main' in name for name in module_names)

    def test_cross_module_consistency(self):
        """Test consistency when importing from different modules."""
        # Import the same function through different paths
        from src.package_trial_zenjiro.main import add_one as add_one_1
        
        # Re-import
        import src.package_trial_zenjiro.main as main_module
        add_one_2 = main_module.add_one
        
        # Both should be the same function object
        assert add_one_1 is add_one_2
        
        # Both should produce the same results
        test_value = 99
        assert add_one_1(test_value) == add_one_2(test_value) == 100