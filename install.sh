#!/bin/sh
set -e

REPO="https://github.com/Shishir-Kc/Elysium"
INSTALL_DIR="$HOME/.Elysium"

echo "Installing Elysium..."

if [ -d "$INSTALL_DIR" ]; then
    echo "Elysium is already installed at $INSTALL_DIR"
    exit 1
fi

git clone "$REPO" "$INSTALL_DIR"

echo "Elysium installed to $INSTALL_DIR"
