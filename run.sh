#!/bin/bash
# This script robustly sets the necessary environment variables and runs the Timelapse GUI.

# Unset any conflicting plugin paths that might be set in the environment.
unset QT_QPA_PLATFORM_PLUGIN_PATH

# If the current session is Wayland, explicitly set the Qt platform to wayland.
# This is the recommended way to fix the "Ignoring XDG_SESSION_TYPE" warning.
if [ "$XDG_SESSION_TYPE" = "wayland" ]; then
  export QT_QPA_PLATFORM=wayland
fi

# Run the Python application
source venv/bin/activate
python3 main.py