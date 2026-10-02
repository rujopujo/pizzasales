"""Shared display and domain constants for the pizza intelligence app.

Backward-compatibility shim re-exporting from src.config.
"""

from src.config.settings import (
    ACCENT_AMBER,
    ACCENT_CYAN,
    ACCENT_GREEN,
    ACCENT_ORANGE,
    ACCENT_RED,
    ACCENT_ROSE,
    ACCENT_YELLOW,
    BG,
    BORDER,
    CARD_BG,
    CATEGORIES,
    CHART_FONT,
    CHART_GRID,
    CHART_PAPER_BG,
    CHART_PLOT_BG,
    MUTED_TEXT,
    PIZZA_COLORSCALE,
    PIZZA_NAMES,
    SIZE_UPLIFTS,
    SIZES,
    TEXT,
)

__all__ = [
    "BG",
    "CARD_BG",
    "BORDER",
    "TEXT",
    "MUTED_TEXT",
    "ACCENT_RED",
    "ACCENT_ORANGE",
    "ACCENT_YELLOW",
    "ACCENT_AMBER",
    "ACCENT_GREEN",
    "ACCENT_CYAN",
    "ACCENT_ROSE",
    "CATEGORIES",
    "SIZES",
    "SIZE_UPLIFTS",
    "PIZZA_NAMES",
    "CHART_FONT",
    "CHART_GRID",
    "CHART_PAPER_BG",
    "CHART_PLOT_BG",
    "PIZZA_COLORSCALE",
]
