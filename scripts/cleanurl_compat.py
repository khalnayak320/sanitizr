#!/usr/bin/env python3
"""
Backward compatibility script for the old 'cleanurl' command.

This script exists to maintain compatibility with users who might still use
the old 'cleanurl' command. It simply redirects to the new 'sanitize' command.
"""

import sys
import warnings
from sanitizr.cleanurl.cli.__main__ import main

def main():
    """Display a deprecation warning and run the main CLI function."""
    warnings.warn(
        "The 'cleanurl' command is deprecated and will be removed in a future version. "
        "Please use 'sanitize' instead.",
        DeprecationWarning,
        stacklevel=2
    )
    from sanitizr.cleanurl.cli.__main__ import main as sanitize_main
    return sanitize_main()

if __name__ == "__main__":
    sys.exit(main())
