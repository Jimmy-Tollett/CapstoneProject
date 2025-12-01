#!/bin/bash
# Build setup script for packaging the Electron app

echo "Setting up build environment..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed"
    exit 1
fi

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "Error: Node.js is not installed"
    exit 1
fi

# Install Python dependencies if needed
if [ ! -d "venv" ]; then
    echo "Creating Python virtual environment..."
    python3 -m venv venv
fi

echo "Activating virtual environment..."
if [ -d "venv/Scripts" ]; then
    source venv/Scripts/activate # Appropriate path for Windows
else
    source venv/bin/activate # Appropriate path for Mac (barf) and Linux
fi

echo "Installing Python dependencies..."
pip install -r requirements.txt

echo "Installing Node.js dependencies..."
npm install

echo "Build setup complete!"
echo ""
echo "To run the app in development mode:"
echo "  npm run dev"
echo ""
echo "To build for production:"
echo "  npm run build:linux    (builds both RPM and AppImage)"
echo "  npm run build:rpm      (builds RPM only)"
echo "  npm run build:appimage (builds AppImage only)"