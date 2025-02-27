# Screen Clear Function

# A function to clear the screen on any operating system

import platform
import os

def clearScreen():
    """
    Clears the screen regardless of the operating system.
    """
    # Detect the operating system
    system = platform.system()
    
    # Use os.name to detect the operating system
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Linux, macOS, etc.
        os.system('clear')