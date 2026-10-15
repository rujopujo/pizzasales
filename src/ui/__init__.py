"""UI package: Streamlit components, CSS styling, metric cards, and theme manager."""

from src.ui.auth import is_authenticated, logout, render_login_page, render_user_profile
from src.ui.components import inject_css, metric_card, section_divider
from src.ui.theme import (
    DEFAULT_THEME, THEME_LEGACY, THEME_LIGHT, THEME_OPTIONS,
    get_chart_theme, get_current_theme_key, get_theme_css, render_theme_switcher,
    style_chart,
)

__all__ = [
    "inject_css", "metric_card", "section_divider",
    "render_theme_switcher", "get_chart_theme", "style_chart",
    "get_current_theme_key", "get_theme_css",
    "THEME_LIGHT", "THEME_LEGACY", "THEME_OPTIONS", "DEFAULT_THEME",
    "is_authenticated", "logout", "render_login_page", "render_user_profile",
]
