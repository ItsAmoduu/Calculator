import os
import sys
import time
import platform
from colorama import Fore, Style, init

# Initialize colorama
init()

def center_text(text, width):
    """Center text in a specified width."""
    lines = text.split('\n')
    centered_lines = [line.center(width) for line in lines]
    return '\n'.join(centered_lines)

def show_admin_error():
    """Displays an error message and exits the program if not run as admin."""
    # Define the ASCII art in red
    ascii_art = f"""
{Fore.RED}
███████╗██████╗ ██████╗  ██████╗ ██████╗
██╔════╝██╔══██╗██╔══██╗██╔═══██╗██╔══██╗
█████╗  ██████╔╝██████╔╝██║   ██║██████╔╝
██╔══╝  ██╔══██╗██╔══██╗██║   ██║██╔══██╗
███████╗██║  ██║██║  ██║╚██████╔╝██║  ██║
╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝
{Style.RESET_ALL}
"""

    # Error message with red color
    error_message = f"""
{Fore.RED}
==============================
[♯] Error, please run the tool as Administrator. (!) ({{}})
==============================
{Style.RESET_ALL}
"""

    # Calculate terminal width
    try:
        terminal_width = os.get_terminal_size().columns
    except AttributeError:
        terminal_width = 80  # Default width if unable to get terminal size

    # Center the ASCII art and error message
    centered_art = center_text(ascii_art, terminal_width)

    for i in range(5, 0, -1):
        # Clear the console and print the centered ASCII art and error message
        os.system('cls' if platform.system() == 'Windows' else 'clear')
        print(centered_art)
        print(center_text(error_message.format(i), terminal_width))  # Update countdown
        time.sleep(1)

    # Exit the program
    sys.exit(1)

def is_admin():
    """Check if the script is run with admin privileges."""
    if platform.system() == 'Windows':
        import ctypes
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    else:
        try:
            return os.getuid() == 0
        except AttributeError:
            return False

# Run the admin check
if not is_admin():
    show_admin_error()
