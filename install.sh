#!/bin/sh
set -e

REPO="https://github.com/Shishir-Kc/Elysium"
INSTALL_DIR="$HOME/.Elysium"
CONFIG_DIR="$HOME/.config/Elysium"
echo "Installing Elysium..."

if [ -d "$INSTALL_DIR" ]; then
    echo "Elysium is already installed at $INSTALL_DIR"
    exit 1
fi

git clone "$REPO" "$INSTALL_DIR"

echo "Installing E.L.Y.S.I.U.M "
echo "Almost there . . .  . "
if [-d "$CONFIG_DIR"]; then
  exit 1
fi
echo "Creating configs "
mkdir -p $CONFIG_DIR

