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
    MUTED_TEXT,
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
]
