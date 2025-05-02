#!/bin/bash

# Check if running as root
if [ "$EUID" -ne 0 ]; then
  echo "Please run as root (sudo)"
  exit 1
fi

# Install system dependencies
echo "Installing system dependencies..."
apt-get update
apt-get install -y \
  libnl-3-dev \
  libnl-genl-3-dev \
  libssl-dev \
  dnsmasq \
  python3-dev \
  build-essential \
  pkg-config

# Install the patched roguehostapd
echo "Installing patched roguehostapd..."
cd roguehostapd
pip install -e .
cd ..

# Install wifiphisher
echo "Installing wifiphisher..."
pip install -e .

echo "Installation completed!"
echo "You can now run wifiphisher with: wifiphisher" 