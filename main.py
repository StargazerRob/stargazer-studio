#!/usr/bin/env python3
"""
Timelapse Creator - A simple GUI app to create timelapses from still images
Requirements: pip install PyQt5 opencv-python-headless pillow
Also needs FFmpeg installed on the system
"""
import sys
import os

from PyQt5.QtWidgets import QApplication
from gui import TimelapseGUI

def main():
    app = QApplication(sys.argv)
    window = TimelapseGUI()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
