"""
Tests for package imports and initialization.
"""
import pytest
import importlib


def test_package_imports():
    """Test importing the main package."""
    import sanitizr
    assert hasattr(sanitizr, "__version__")
    
    # Check that the main modules can be imported
    from sanitizr import cleanurl
    assert cleanurl is not None
    
    # Check that submodules can be imported
    from sanitizr.cleanurl import core, config, cli
    assert core is not None
    assert config is not None
    assert cli is not None
    
    # Check specific components
    from sanitizr.cleanurl.core import cleaner
    assert hasattr(cleaner, "URLCleaner")
    
    from sanitizr.cleanurl.config import config
    assert hasattr(config, "ConfigManager")


def test_cli_entrypoint():
    """Test that the CLI entrypoint is properly registered."""
    # This test verifies that the CLI entrypoint defined in pyproject.toml works
    import pkg_resources
    
    # Get all entrypoints for the 'console_scripts' group
    entry_points = list(pkg_resources.iter_entry_points(group='console_scripts'))
    
    # Find the 'cleanurl' entrypoint
    cleanurl_entry = next((ep for ep in entry_points if ep.name == 'cleanurl'), None)
    
    # Verify that the 'cleanurl' entrypoint exists
    assert cleanurl_entry is not None
    
    # Verify that the entrypoint points to the correct function
    assert cleanurl_entry.module_name == 'sanitizr.cleanurl.cli.__main__'
    assert cleanurl_entry.attrs == ['main']


def test_version_consistency():
    """Test that version is consistent across the package."""
    import sanitizr
    
    # Get version from module
    module_version = sanitizr.__version__
    
    # Try to get version from package metadata
    try:
        import importlib.metadata
        metadata_version = importlib.metadata.version('sanitizr')
        # Check that versions match
        assert module_version == metadata_version
    except (ImportError, importlib.metadata.PackageNotFoundError):
        # Skip this check if we can't get metadata version
        pass
