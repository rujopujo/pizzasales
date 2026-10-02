"""Shared display and domain constants for the pizza intelligence app.

Warm pizzeria palette: brick oven darks, tomato reds, mozzarella creams,
basil greens, and golden crust ambers.
"""

# --- Deep Pizzeria Palette ---
BG = "#1A0F0A"                  # Dark walnut / brick oven interior
CARD_BG = "rgba(42, 28, 18, 0.85)"  # Smoky card glass
BORDER = "rgba(212, 136, 46, 0.25)"  # Warm crust glow border
TEXT = "#FFF5E6"                # Mozzarella cream text
MUTED_TEXT = "#C4A882"          # Aged parmesan muted

# Core accent colors — the pizza ingredient palette
ACCENT_RED = "#E63946"          # Tomato sauce / pepperoni red
ACCENT_ORANGE = "#F77F00"       # Brick oven flame orange
ACCENT_YELLOW = "#FCBF49"      # Golden crust / melted cheese
ACCENT_AMBER = "#D4882E"       # Baked cheese / crust amber

# Extended palette
ACCENT_GREEN = "#4A9E5C"       # Fresh basil green
ACCENT_CYAN = "#5EAAA8"        # Mediterranean olive teal
ACCENT_ROSE = "#C1446A"        # Sun-dried tomato rose

CATEGORIES = ["Classic", "Veggie", "Supreme", "Chicken"]
SIZES = ["S", "M", "L", "XL", "XXL"]
SIZE_UPLIFTS = {"S": 0.0, "M": 2.0, "L": 4.0, "XL": 6.0, "XXL": 8.0}

PIZZA_NAMES = {
    "Classic": ["Margherita", "Pepperoni", "Four Cheese", "Hawaiian"],
    "Veggie": ["Garden Fresh", "Mushroom Medley", "Spinach Feta", "Mediterranean"],
    "Supreme": ["The Works", "Deluxe Supreme", "Firehouse", "BBQ Supreme"],
    "Chicken": ["BBQ Chicken", "Buffalo Chicken", "Chicken Pesto", "Tandoori Chicken"],
}

# Plotly chart template settings
CHART_FONT = "Plus Jakarta Sans, sans-serif"
CHART_GRID = "rgba(255, 245, 230, 0.08)"
CHART_PAPER_BG = "rgba(0,0,0,0)"
CHART_PLOT_BG = "rgba(0,0,0,0)"

# Pizza-themed colorscale for heatmaps (cream → gold → orange → red → dark)
PIZZA_COLORSCALE = [
    [0.0, "#FFF5E6"],
    [0.25, "#FCBF49"],
    [0.5, "#F77F00"],
    [0.75, "#E63946"],
    [1.0, "#7A1F2E"],
]
