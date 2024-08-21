from datetime import datetime

# ANSI escape codes for text formatting
BOLD = '\033[1m'
RED = '\033[31m'
GREEN = '\033[32m'
BLUE = '\033[34m'
RESET = '\033[0m'

def format_timestamp(timestamp_ms: int) -> str:
    """
    Format a Unix timestamp in milliseconds to a human-readable time.
    """
    local_time = datetime.fromtimestamp(timestamp_ms / 1000)
    return local_time.strftime('%I:%M:%S %p')

def bold(text: str) -> str:
    """
    Return the text in bold.
    """
    return f"{BOLD}{text}{RESET}"

def green(text: str) -> str:
    """
    Return the text in green.
    """
    return f"{GREEN}{text}{RESET}"

def blue(text: str) -> str:
    """
    Return the text in blue.
    """
    return f"{BLUE}{text}{RESET}"

def red(text: str) -> str:
    """
    Return the text in red.
    """
    return f"{RED}{text}{RESET}"