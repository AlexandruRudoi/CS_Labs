"""
Main entry point for the refactored Playfair cipher application
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.ui.interface import PlayfairUI

if __name__ == "__main__":
    app = PlayfairUI()
    app.run()