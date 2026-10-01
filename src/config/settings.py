"""Shared display and domain constants for the pizza intelligence app."""

# Light mode warm pizza palette
BG = "#FFFBF5"
CARD_BG = "#FFFFFF"
BORDER = "#FED7AA"
TEXT = "#1C1917"
MUTED_TEXT = "#78716C"

# Core Theme: Red, Orange, Yellow
ACCENT_RED = "#DC2626"
ACCENT_ORANGE = "#EA580C"
ACCENT_YELLOW = "#EAB308"
ACCENT_AMBER = "#D97706"

# Compatibility aliases mapped to the warm palette
ACCENT_GREEN = "#D97706"
ACCENT_CYAN = "#EA580C"
ACCENT_ROSE = "#DC2626"

CATEGORIES = ["Classic", "Veggie", "Supreme", "Chicken"]
SIZES = ["S", "M", "L", "XL", "XXL"]
SIZE_UPLIFTS = {"S": 0.0, "M": 2.0, "L": 4.0, "XL": 6.0, "XXL": 8.0}

PIZZA_NAMES = {
    "Classic": ["Margherita", "Pepperoni", "Four Cheese", "Hawaiian"],
    "Veggie": ["Garden Fresh", "Mushroom Medley", "Spinach Feta", "Mediterranean"],
    "Supreme": ["The Works", "Deluxe Supreme", "Firehouse", "BBQ Supreme"],
    "Chicken": ["BBQ Chicken", "Buffalo Chicken", "Chicken Pesto", "Tandoori Chicken"],
}
