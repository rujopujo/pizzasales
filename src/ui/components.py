"""Reusable Streamlit presentation elements in immersive pizzeria dark theme."""

from __future__ import annotations

from html import escape

import streamlit as st

from src.config.settings import (
    ACCENT_AMBER, ACCENT_GREEN, ACCENT_ORANGE, ACCENT_RED, ACCENT_YELLOW,
    BG, BORDER, CARD_BG, MUTED_TEXT, TEXT,
    # UI/Theme Constants
    TRANSITION_FAST, TRANSITION_NORMAL, TRANSITION_SLOW,
    BLUR_SMALL, BLUR_MEDIUM, BLUR_LARGE, BLUR_XLARGE,
    SHADOW_SUBTLE, SHADOW_NORMAL, SHADOW_HOVER, SHADOW_INSET,
    BORDER_RADIUS_SM, BORDER_RADIUS_MD, BORDER_RADIUS_LG, BORDER_RADIUS_XL, BORDER_RADIUS_PILL,
    SPACING_XS, SPACING_SM, SPACING_MD, SPACING_LG, SPACING_XL,
    CATEGORIES, CHART_FONT, CHART_GRID, SIZES,
)


from src.ui.theme import get_theme_css


def inject_css(theme_name: str | None = None) -> None:
    """Inject dynamic CSS styling based on the active theme."""
    st.markdown(get_theme_css(theme_name), unsafe_allow_html=True)


def metric_card(label: str, value: str, accent: str = ACCENT_ORANGE, icon: str = "") -> str:
    icon_html = f'<div class="kpi-icon">{icon}</div>' if icon else ''
    return (
        '<div class="porcelain-card">'
        f'{icon_html}'
        f'<div class="kpi-label">{escape(label)}</div>'
        f'<div class="kpi-value">{escape(value)}</div>'
        f'<div class="kpi-accent-pill" style="background:linear-gradient(90deg, {escape(accent)}, {escape(ACCENT_YELLOW)});"></div>'
        '</div>'
    )


def section_divider() -> str:
    return '<div class="pizza-divider">🍕 · 🍕 · 🍕</div>'
