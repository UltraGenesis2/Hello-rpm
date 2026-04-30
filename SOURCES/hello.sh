#!/bin/bash
CONFIG_FILE="/etc/hello.conf"

# Set a default greeting
PREFIX="Hello"

# Load custom config if it exists
if [ -f "$CONFIG_FILE" ]; then
    source "$CONFIG_FILE"
fi

echo "$PREFIX! You have successfully installed the simple RPM package (Version 2.0)."
