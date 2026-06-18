"""
Configuration module for the Currency Converter application.
Centralizes all settings and constants for easy maintenance.
"""

# Application metadata
APP_NAME = "Currency Converter"
APP_VERSION = "2.0.0"
APP_AUTHOR = "shree-aru"

# Supported currencies and their full names
CURRENCY_NAMES = {
    "USD": "United States Dollar",
    "EUR": "Euro",
    "GBP": "British Pound Sterling",
    "JPY": "Japanese Yen",
    "INR": "Indian Rupee",
    "AUD": "Australian Dollar",
    "CAD": "Canadian Dollar",
}

# Currency symbols for display
CURRENCY_SYMBOLS = {
    "USD": "$",
    "EUR": "€",
    "GBP": "£",
    "JPY": "¥",
    "INR": "₹",
    "AUD": "A$",
    "CAD": "C$",
}

# API Configuration
API_BASE_URL = "https://api.exchangerate-api.com/v4/latest/"
API_TIMEOUT_SECONDS = 10

# History settings
MAX_HISTORY_RECORDS = 100
HISTORY_FILE = "conversion_history.json"

# GUI settings
WINDOW_WIDTH = 450
WINDOW_HEIGHT = 350
THEME = "tokyonight"

def get_currency_display(code):
    """Return formatted currency display string."""
    name = CURRENCY_NAMES.get(code, "Unknown")
    symbol = CURRENCY_SYMBOLS.get(code, "")
    return f"{code} ({symbol}) - {name}"
