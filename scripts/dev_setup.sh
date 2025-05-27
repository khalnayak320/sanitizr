#!/bin/bash
# Development setup script for Sanitizr

# Check if Python is installed
if ! command -v python3 &>/dev/null; then
    echo "Python 3 is required but could not be found. Please install Python 3 and try again."
    exit 1
fi

# Check if pip is installed
if ! command -v pip3 &>/dev/null; then
    echo "pip3 is required but could not be found. Please install pip and try again."
    exit 1
fi

# Create a virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    source venv/bin/activate
    pip install --upgrade pip
else
    echo "Virtual environment already exists. Activating..."
    source venv/bin/activate
fi

# Install the package in development mode with all optional dependencies
echo "Installing Sanitizr in development mode with all dependencies..."
pip install -e ".[dev,docs,yaml]"

# Display success message
echo ""
echo "-------------------------------------"
echo "Sanitizr development setup complete!"
echo "-------------------------------------"
echo ""
echo "To activate the virtual environment, run:"
echo "  source venv/bin/activate"
echo ""
echo "To run tests:"
echo "  pytest"
echo ""
echo "To serve documentation locally:"
echo "  mkdocs serve"
echo ""
echo "To use the CLI tool:"
echo "  cleanurl --help"
echo ""
