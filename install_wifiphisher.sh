#!/bin/bash

# Run from outside sudo and ensure venv is active
if [ "$EUID" -eq 0 ]; then
  echo "Do not run this script with sudo. It uses a virtualenv."
  exit 1
fi

# Confirm venv is active
if [[ -z "$VIRTUAL_ENV" ]]; then
  echo "Please activate your Python virtual environment before running this script."
  exit 1
fi

INSTALL_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "[*] Installing system dependencies (requires sudo password)..."
sudo apt-get update
sudo apt-get install -y \
  libnl-3-dev \
  libnl-genl-3-dev \
  libssl-dev \
  dnsmasq \
  hostapd \
  aircrack-ng \
  iw \
  rfkill \
  python3.13-dev \
  build-essential \
  pkg-config \
  git

# Install roguehostapd from local directory (in-tree)
echo "[*] Installing roguehostapd into venv..."
cd roguehostapd || exit 1
pip install -e .
cd ..

# Install wifiphisher from local editable source
echo "[*] Installing wifiphisher into venv..."
pip install -e .

echo "[+] Done. Run Wifiphisher with: sudo $VIRTUAL_ENV/bin/wifiphisher"

echo "[+] Creating global symlink to Wifiphisher..."

sudo ln -sf "$INSTALL_DIR/.venv/bin/wifiphisher" /usr/local/bin/wifiphisher

echo "[+] You can now run it with: sudo wifiphisher"

echo "Patching pyric..."
sed -i 's/fout.write(rfke)/fout.write(rfke.decode())/' \
  "$VIRTUAL_ENV/lib/python*/site-packages/pyric/utils/rfkill.py"
