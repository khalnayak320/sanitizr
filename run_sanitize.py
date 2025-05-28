#!/usr/bin/env python3
"""
Convenience script to run the URL sanitizer directly from the source tree.

This script can be used to test the URL sanitizer without installing the package.
"""

import sys
from sanitizr.cleanurl.cli.__main__ import main

if __name__ == "__main__":
    sys.exit(main())
