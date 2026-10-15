"""Theme system for Pizza MDW: Light Mode (default) and Legacy Pizzeria Dark."""

from __future__ import annotations

import streamlit as st
import plotly.graph_objects as go

from src.config.settings import (
    ACCENT_AMBER, ACCENT_GREEN, ACCENT_ORANGE, ACCENT_RED, ACCENT_YELLOW,
    CHART_FONT, PIZZA_COLORSCALE,
)

THEME_LIGHT = "☀️ Light Mode"
THEME_LEGACY = "🍕 Legacy"

THEME_OPTIONS = [THEME_LIGHT, THEME_LEGACY]
DEFAULT_THEME = THEME_LIGHT


def normalize_theme(name: str | None) -> str:
    """Normalize any theme label into 'light' or 'legacy'."""
    if not name:
        return "light"
    s = str(name).lower()
    if "legacy" in s or "dark" in s:
        return "legacy"
    return "light"


def get_current_theme_key() -> str:
    """Return the active theme key ('light' or 'legacy')."""
    try:
        current = st.session_state.get("theme", DEFAULT_THEME)
        return normalize_theme(current)
    except Exception:
        return "light"


def get_chart_theme(theme_name: str | None = None) -> dict:
    """Return Plotly visual styling parameters for the specified theme."""
    key = normalize_theme(theme_name) if theme_name else get_current_theme_key()
    if key == "light":
        return {
            "template": "plotly_white",
            "paper_bg": "rgba(0,0,0,0)",
            "plot_bg": "rgba(0,0,0,0)",
            "font_color": "#0F172A",
            "muted_color": "#64748B",
            "grid_color": "rgba(15, 23, 42, 0.08)",
            "legend_bg": "rgba(255, 255, 255, 0.92)",
            "legend_border": "rgba(226, 232, 240, 0.9)",
            "connector_color": "rgba(100, 116, 139, 0.35)",
            "heatmap_colorscale": [
                [0.0, "#FFF7ED"],
                [0.25, "#FED7AA"],
                [0.5, "#FB923C"],
                [0.75, "#EA580C"],
                [1.0, "#991B1B"],
            ],
        }
    # Legacy Pizzeria Dark
    return {
        "template": "plotly_dark",
        "paper_bg": "rgba(0,0,0,0)",
        "plot_bg": "rgba(0,0,0,0)",
        "font_color": "#FFF5E6",
        "muted_color": "#C4A882",
        "grid_color": "rgba(255, 245, 230, 0.08)",
        "legend_bg": "rgba(42, 28, 18, 0.6)",
        "legend_border": "rgba(212, 136, 46, 0.2)",
        "connector_color": "rgba(196, 168, 130, 0.25)",
        "heatmap_colorscale": PIZZA_COLORSCALE,
    }


def style_chart(fig: go.Figure, height: int = 380, theme_name: str | None = None) -> go.Figure:
    """Apply unified theme styling to a Plotly figure."""
    cfg = get_chart_theme(theme_name)
    fig.update_layout(
        template=cfg["template"],
        paper_bgcolor=cfg["paper_bg"],
        plot_bgcolor=cfg["plot_bg"],
        font=dict(color=cfg["font_color"], family=CHART_FONT),
        margin=dict(l=25, r=25, t=50, b=35),
        height=height,
        legend=dict(
            bgcolor=cfg["legend_bg"],
            bordercolor=cfg["legend_border"],
            borderwidth=1,
            font=dict(color=cfg["font_color"]),
        ),
    )
    fig.update_xaxes(showgrid=True, gridcolor=cfg["grid_color"], zeroline=False)
    fig.update_yaxes(showgrid=True, gridcolor=cfg["grid_color"], zeroline=False)
    return fig


def get_theme_css(theme_name: str | None = None) -> str:
    """Generate dynamic CSS corresponding to the selected theme."""
    key = normalize_theme(theme_name) if theme_name else get_current_theme_key()

    if key == "light":
        return """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;800;900&display=swap');

        :root {
            --bg-color: #F8FAFC;
            --card-bg: #FFFFFF;
            --border-color: #E2E8F0;
            --text-color: #0F172A;
            --muted-text: #64748B;
        }

        html, body, [class*="css"] {
            font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
            color: #0F172A;
        }

        /* ── Modern Porcelain Light Background with Warm Ambient Accents ── */
        .stApp {
            background-color: #F8FAFC;
            background-image:
                radial-gradient(ellipse at 12% 0%, rgba(247, 127, 0, 0.07) 0%, transparent 45%),
                radial-gradient(ellipse at 88% 0%, rgba(230, 57, 70, 0.05) 0%, transparent 40%),
                radial-gradient(ellipse at 50% 100%, rgba(252, 191, 73, 0.06) 0%, transparent 50%),
                radial-gradient(circle at 50% 50%, rgba(241, 245, 249, 0.5) 0%, transparent 70%);
            color: #0F172A;
        }

        .block-container {
            padding-top: 1.25rem;
            padding-bottom: 2.5rem;
            max-width: 1550px;
        }

        /* ── Sidebar — Crisp Modern Studio Panel ── */
        section[data-testid="stSidebar"] {
            background: linear-gradient(180deg, #FFFFFF 0%, #F8FAFC 50%, #F1F5F9 100%);
            border-right: 1px solid #E2E8F0;
            box-shadow: 3px 0 20px rgba(15, 23, 42, 0.04);
        }
        section[data-testid="stSidebar"] .block-container {
            padding-top: 1.5rem;
        }
        section[data-testid="stSidebar"] h1,
        section[data-testid="stSidebar"] h2,
        section[data-testid="stSidebar"] h3 {
            color: #C2410C;
            font-weight: 700;
        }
        section[data-testid="stSidebar"] p,
        section[data-testid="stSidebar"] label,
        section[data-testid="stSidebar"] span {
            color: #475569;
        }

        /* ── Headings — Vibrant Sunlit Artisan Gradient ── */
        h1 {
            font-family: 'Playfair Display', 'Georgia', serif;
            background: linear-gradient(135deg, #C2410C 0%, #EA580C 45%, #DC2626 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 900;
            letter-spacing: -0.03em;
        }
        h2, h3 {
            color: #C2410C;
            font-weight: 700;
            letter-spacing: -0.015em;
        }
        h4 {
            color: #EA580C;
            font-weight: 600;
        }

        /* ── KPI Metric Grid ── */
        .kpi-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1rem;
            margin: 0.8rem 0 1.5rem;
        }

        /* ── Porcelain Card — Crisp Light Surface ── */
        .porcelain-card {
            background: #FFFFFF;
            border: 1px solid #E2E8F0;
            border-radius: 16px;
            padding: 1.2rem 1.3rem;
            box-shadow:
                0 4px 20px -2px rgba(15, 23, 42, 0.05),
                0 2px 6px -1px rgba(15, 23, 42, 0.03),
                inset 0 1px 0 rgba(255, 255, 255, 1);
            transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1),
                        box-shadow 0.25s ease,
                        border-color 0.25s ease;
            position: relative;
            overflow: hidden;
        }
        .porcelain-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 3px;
            background: linear-gradient(90deg, #E63946, #F77F00, #FCBF49);
            opacity: 0.85;
            transition: opacity 0.25s ease;
        }
        .porcelain-card:hover {
            transform: translateY(-4px);
            box-shadow:
                0 16px 36px -6px rgba(247, 127, 0, 0.16),
                0 4px 12px rgba(15, 23, 42, 0.06);
            border-color: rgba(247, 127, 0, 0.45);
        }
        .porcelain-card:hover::before {
            opacity: 1;
        }

        .kpi-label {
            color: #64748B;
            font-size: 0.8rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.06em;
            line-height: 1.3;
        }
        .kpi-value {
            color: #0F172A;
            font-size: clamp(1.5rem, 2.2vw, 2.05rem);
            font-weight: 800;
            margin-top: 0.35rem;
            white-space: nowrap;
            font-variant-numeric: tabular-nums;
            letter-spacing: -0.02em;
        }
        .kpi-accent-pill {
            width: 38px;
            height: 4px;
            border-radius: 4px;
            margin-top: 0.85rem;
        }
        .kpi-icon {
            font-size: 1.6rem;
            margin-bottom: 0.3rem;
        }

        /* ── Tabs — Crisp Studio Pill Design ── */
        div[data-baseweb="tab-list"] {
            background: #F1F5F9;
            padding: 0.35rem;
            border-radius: 14px;
            gap: 0.35rem;
            border: 1px solid #E2E8F0;
            margin-bottom: 1.2rem;
        }
        button[data-baseweb="tab"] {
            border-radius: 10px;
            padding: 0.6rem 1.2rem;
            font-weight: 600;
            font-size: 0.92rem;
            color: #64748B !important;
            border: none !important;
            background: transparent !important;
            transition: all 0.2s ease;
        }
        button[data-baseweb="tab"]:hover {
            color: #C2410C !important;
            background: rgba(254, 215, 170, 0.3) !important;
        }
        button[data-baseweb="tab"][aria-selected="true"] {
            background: linear-gradient(135deg, #F97316 0%, #EA580C 100%) !important;
            color: #FFFFFF !important;
            box-shadow: 0 4px 14px rgba(234, 88, 12, 0.28);
        }
        div[data-baseweb="tab-highlight"] {
            display: none !important;
        }

        /* ── Buttons — Oven Flame Gradient ── */
        div.stButton > button {
            background: linear-gradient(135deg, #F97316 0%, #EA580C 100%);
            color: #FFFFFF !important;
            font-weight: 600;
            border-radius: 11px;
            border: none;
            padding: 0.6rem 1.3rem;
            box-shadow: 0 3px 12px rgba(234, 88, 12, 0.22);
            transition: all 0.2s ease;
        }
        div.stButton > button:hover {
            background: linear-gradient(135deg, #FB923C 0%, #F97316 100%);
            box-shadow: 0 6px 20px rgba(234, 88, 12, 0.35);
            transform: translateY(-2px);
            color: #FFFFFF !important;
        }

        button[kind="primaryFormSubmit"] {
            background: linear-gradient(135deg, #F97316 0%, #EA580C 100%) !important;
            color: #FFFFFF !important;
            font-weight: 600 !important;
            border-radius: 11px !important;
            border: none !important;
            box-shadow: 0 3px 12px rgba(234, 88, 12, 0.22) !important;
        }

        /* ── Dataframes & Expanders ── */
        div[data-testid="stDataFrame"] {
            background: #FFFFFF;
            border: 1px solid #E2E8F0;
            border-radius: 14px;
            box-shadow: 0 2px 10px rgba(15, 23, 42, 0.04);
        }
        div[data-testid="stExpander"] {
            background: #FFFFFF;
            border: 1px solid #E2E8F0;
            border-radius: 14px;
            box-shadow: 0 2px 8px rgba(15, 23, 42, 0.03);
        }
        div[data-testid="stExpander"] summary {
            color: #C2410C;
            font-weight: 600;
        }

        /* ── Inputs, Selects, Number Inputs ── */
        div[data-baseweb="select"] > div {
            background: #FFFFFF !important;
            border-color: #CBD5E1 !important;
            border-radius: 10px;
            color: #0F172A !important;
        }
        div[data-baseweb="input"] {
            background: #FFFFFF !important;
            border-color: #CBD5E1 !important;
            border-radius: 10px;
        }
        div[data-baseweb="input"] input {
            color: #0F172A !important;
        }

        /* ── Segmented Control / Pills Styling ── */
        div[data-testid="stSegmentedControl"] {
            background: #FFFFFF;
            border: 1px solid #E2E8F0;
            border-radius: 12px;
            padding: 3px;
            box-shadow: 0 1px 4px rgba(15, 23, 42, 0.04);
        }

        /* ── Hero Banner Badge ── */
        .hero-badge {
            display: inline-flex;
            align-items: center;
            gap: 0.45rem;
            background: linear-gradient(135deg, rgba(234, 88, 12, 0.12) 0%, rgba(247, 127, 0, 0.10) 50%, rgba(252, 191, 73, 0.15) 100%);
            color: #C2410C;
            padding: 0.3rem 0.85rem;
            border-radius: 24px;
            font-size: 0.78rem;
            font-weight: 700;
            letter-spacing: 0.05em;
            border: 1px solid rgba(234, 88, 12, 0.25);
            margin-bottom: 0.5rem;
            text-transform: uppercase;
        }

        .pizza-divider {
            text-align: center;
            margin: 1.5rem 0 1rem;
            color: #94A3B8;
            font-size: 1.2rem;
            letter-spacing: 0.5em;
            opacity: 0.7;
        }

        div[data-testid="stMetric"] {
            background: #FFFFFF;
            border: 1px solid #E2E8F0;
            border-radius: 14px;
            padding: 1rem;
            box-shadow: 0 2px 8px rgba(15, 23, 42, 0.03);
        }
        div[data-testid="stMetric"] label {
            color: #64748B !important;
        }
        [data-testid="stMetricValue"] {
            color: #0F172A !important;
        }

        div[data-testid="stPlotlyChart"] {
            background: #FFFFFF;
            border: 1px solid #E2E8F0;
            border-radius: 14px;
            padding: 0.4rem;
            box-shadow: 0 2px 10px rgba(15, 23, 42, 0.03);
        }

        .stCaption, div[data-testid="stCaptionContainer"] {
            color: #64748B !important;
            opacity: 0.95;
        }

        div[data-testid="stForm"] {
            background: #FFFFFF;
            border: 1px solid #E2E8F0;
            border-radius: 14px;
            padding: 1rem;
            box-shadow: 0 2px 8px rgba(15, 23, 42, 0.03);
        }

        .theme-pill-badge {
            display: inline-flex;
            align-items: center;
            gap: 0.4rem;
            font-size: 0.85rem;
            font-weight: 700;
            color: #C2410C;
            background: rgba(254, 215, 170, 0.35);
            border: 1px solid rgba(234, 88, 12, 0.25);
            border-radius: 20px;
            padding: 0.2rem 0.65rem;
            margin-bottom: 0.3rem;
        }

        ::-webkit-scrollbar {
            width: 8px;
            height: 8px;
        }
        ::-webkit-scrollbar-track {
            background: #F1F5F9;
        }
        ::-webkit-scrollbar-thumb {
            background: #CBD5E1;
            border-radius: 4px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: #94A3B8;
        }
        </style>
        """

    # Legacy Pizzeria Dark (the authentic original dark brick-oven theme)
    return f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;800;900&display=swap');

    html, body, [class*="css"] {{
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    }}

    /* ── Dark Brick Oven Background with Warm Glow ── */
    .stApp {{
        background-color: #1A0F0A !important;
        background-image:
            radial-gradient(ellipse at 10% 0%, rgba(231, 57, 70, 0.16) 0%, transparent 50%),
            radial-gradient(ellipse at 90% 0%, rgba(247, 127, 0, 0.14) 0%, transparent 45%),
            radial-gradient(ellipse at 50% 100%, rgba(252, 191, 73, 0.08) 0%, transparent 55%),
            radial-gradient(circle at 50% 50%, rgba(42, 28, 18, 0.6) 0%, transparent 70%) !important;
        color: #FFF5E6 !important;
    }}

    .stApp, .stApp p, .stApp span, .stApp label, .stApp div {{
        color: #FFF5E6;
    }}

    .block-container {{
        padding-top: 1.25rem;
        padding-bottom: 2.5rem;
        max-width: 1550px;
    }}

    /* ── Sidebar — Dark Wood Panel ── */
    section[data-testid="stSidebar"] {{
        background: linear-gradient(180deg, #211410 0%, #1A0F0A 40%, #2A1C12 100%) !important;
        border-right: 1px solid rgba(212, 136, 46, 0.25) !important;
        box-shadow: 3px 0 24px rgba(0, 0, 0, 0.4) !important;
    }}
    section[data-testid="stSidebar"] .block-container {{
        padding-top: 1.5rem;
    }}
    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3 {{
        color: {ACCENT_YELLOW} !important;
        font-weight: 700;
    }}
    section[data-testid="stSidebar"] p,
    section[data-testid="stSidebar"] label,
    section[data-testid="stSidebar"] span {{
        color: #C4A882 !important;
    }}

    /* ── Headings — Fiery Gradient ── */
    h1 {{
        font-family: 'Playfair Display', 'Georgia', serif;
        background: linear-gradient(135deg, {ACCENT_YELLOW} 0%, {ACCENT_ORANGE} 40%, {ACCENT_RED} 100%) !important;
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        font-weight: 900;
        letter-spacing: -0.03em;
    }}
    h2, h3 {{
        color: {ACCENT_YELLOW} !important;
        font-weight: 700;
        letter-spacing: -0.015em;
    }}
    h4 {{
        color: {ACCENT_ORANGE} !important;
        font-weight: 600;
    }}

    /* ── KPI Metric Grid ── */
    .kpi-grid {{
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 1rem;
        margin: 0.8rem 0 1.5rem;
    }}

    /* ── Glassmorphic KPI Card ── */
    .porcelain-card {{
        background: rgba(42, 28, 18, 0.85) !important;
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(212, 136, 46, 0.25) !important;
        border-radius: 16px;
        padding: 1.2rem 1.3rem;
        box-shadow:
            0 4px 24px -4px rgba(0, 0, 0, 0.35),
            0 0 0 1px rgba(212, 136, 46, 0.05),
            inset 0 1px 0 rgba(255, 245, 230, 0.04) !important;
        transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1),
                    box-shadow 0.25s ease,
                    border-color 0.25s ease;
        position: relative;
        overflow: hidden;
    }}
    .porcelain-card::before {{
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 3px;
        background: linear-gradient(90deg, {ACCENT_RED}, {ACCENT_ORANGE}, {ACCENT_YELLOW});
        opacity: 0.8;
        transition: opacity 0.25s ease;
    }}
    .porcelain-card:hover {{
        transform: translateY(-4px);
        box-shadow:
            0 16px 40px -8px rgba(247, 127, 0, 0.18),
            0 8px 16px rgba(0, 0, 0, 0.25) !important;
        border-color: rgba(247, 127, 0, 0.45) !important;
    }}
    .porcelain-card:hover::before {{
        opacity: 1;
    }}

    .kpi-label {{
        color: #C4A882 !important;
        font-size: 0.8rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.06em;
        line-height: 1.3;
    }}
    .kpi-value {{
        color: #FFF5E6 !important;
        font-size: clamp(1.5rem, 2.2vw, 2.05rem);
        font-weight: 800;
        margin-top: 0.35rem;
        white-space: nowrap;
        font-variant-numeric: tabular-nums;
        letter-spacing: -0.02em;
    }}
    .kpi-accent-pill {{
        width: 38px;
        height: 4px;
        border-radius: 4px;
        margin-top: 0.85rem;
    }}
    .kpi-icon {{
        font-size: 1.6rem;
        margin-bottom: 0.3rem;
    }}

    /* ── Tabs — Ember Pill Design ── */
    div[data-baseweb="tab-list"] {{
        background: rgba(42, 28, 18, 0.65) !important;
        backdrop-filter: blur(12px);
        padding: 0.4rem;
        border-radius: 14px;
        gap: 0.35rem;
        border: 1px solid rgba(212, 136, 46, 0.25) !important;
        margin-bottom: 1.2rem;
    }}
    button[data-baseweb="tab"] {{
        border-radius: 10px;
        padding: 0.6rem 1.2rem;
        font-weight: 600;
        font-size: 0.92rem;
        color: #C4A882 !important;
        border: none !important;
        background: transparent !important;
        transition: all 0.2s ease;
    }}
    button[data-baseweb="tab"]:hover {{
        color: {ACCENT_YELLOW} !important;
        background: rgba(252, 191, 73, 0.1) !important;
    }}
    button[data-baseweb="tab"][aria-selected="true"] {{
        background: linear-gradient(135deg, {ACCENT_ORANGE} 0%, {ACCENT_RED} 100%) !important;
        color: #FFFFFF !important;
        box-shadow: 0 4px 18px rgba(247, 127, 0, 0.35), 0 0 0 1px rgba(247, 127, 0, 0.2) !important;
    }}
    div[data-baseweb="tab-highlight"] {{
        display: none !important;
    }}

    /* ── Buttons — Oven Flame Gradient ── */
    div.stButton > button {{
        background: linear-gradient(135deg, {ACCENT_ORANGE} 0%, {ACCENT_RED} 100%) !important;
        color: #FFFFFF !important;
        font-weight: 600;
        border-radius: 11px;
        border: none;
        padding: 0.6rem 1.3rem;
        box-shadow: 0 4px 16px rgba(247, 127, 0, 0.25) !important;
        transition: all 0.2s ease;
    }}
    div.stButton > button:hover {{
        background: linear-gradient(135deg, #FF8C1A 0%, #FF4757 100%) !important;
        box-shadow: 0 8px 24px rgba(247, 127, 0, 0.40) !important;
        transform: translateY(-2px);
        color: #FFFFFF !important;
    }}

    button[kind="primaryFormSubmit"] {{
        background: linear-gradient(135deg, {ACCENT_ORANGE} 0%, {ACCENT_RED} 100%) !important;
        color: #FFFFFF !important;
        font-weight: 600 !important;
        border-radius: 11px !important;
        border: none !important;
        box-shadow: 0 4px 16px rgba(247, 127, 0, 0.25) !important;
    }}

    div[data-testid="stDataFrame"] {{
        background: rgba(42, 28, 18, 0.6) !important;
        border: 1px solid rgba(212, 136, 46, 0.25) !important;
        border-radius: 14px;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2) !important;
    }}
    div[data-testid="stExpander"] {{
        background: rgba(42, 28, 18, 0.5) !important;
        border: 1px solid rgba(212, 136, 46, 0.25) !important;
        border-radius: 14px;
    }}
    div[data-testid="stExpander"] summary {{
        color: {ACCENT_YELLOW} !important;
        font-weight: 600;
    }}

    div[data-baseweb="select"] > div {{
        background: rgba(42, 28, 18, 0.8) !important;
        border-color: rgba(212, 136, 46, 0.25) !important;
        border-radius: 10px;
        color: #FFF5E6 !important;
    }}
    div[data-baseweb="input"] {{
        background: rgba(42, 28, 18, 0.8) !important;
        border-color: rgba(212, 136, 46, 0.25) !important;
        border-radius: 10px;
    }}
    div[data-baseweb="input"] input {{
        color: #FFF5E6 !important;
    }}

    /* ── Segmented Control in Legacy ── */
    div[data-testid="stSegmentedControl"] {{
        background: rgba(42, 28, 18, 0.8) !important;
        border: 1px solid rgba(212, 136, 46, 0.25) !important;
        border-radius: 12px;
        padding: 3px;
    }}
    div[data-testid="stSegmentedControl"] button {{
        color: #C4A882 !important;
    }}
    div[data-testid="stSegmentedControl"] button[aria-selected="true"] {{
        background: linear-gradient(135deg, {ACCENT_ORANGE} 0%, {ACCENT_RED} 100%) !important;
        color: #FFFFFF !important;
    }}

    .hero-badge {{
        display: inline-flex;
        align-items: center;
        gap: 0.45rem;
        background: linear-gradient(135deg, rgba(230, 57, 70, 0.18) 0%, rgba(247, 127, 0, 0.15) 50%, rgba(252, 191, 73, 0.12) 100%);
        color: {ACCENT_YELLOW};
        padding: 0.3rem 0.85rem;
        border-radius: 24px;
        font-size: 0.78rem;
        font-weight: 700;
        letter-spacing: 0.05em;
        border: 1px solid rgba(252, 191, 73, 0.25);
        margin-bottom: 0.5rem;
        text-transform: uppercase;
    }}

    .pizza-divider {{
        text-align: center;
        margin: 1.5rem 0 1rem;
        color: #C4A882;
        font-size: 1.2rem;
        letter-spacing: 0.5em;
        opacity: 0.5;
    }}

    div[data-testid="stMetric"] {{
        background: rgba(42, 28, 18, 0.85) !important;
        backdrop-filter: blur(12px);
        border: 1px solid rgba(212, 136, 46, 0.25) !important;
        border-radius: 14px;
        padding: 1rem;
    }}
    div[data-testid="stMetric"] label {{
        color: #C4A882 !important;
    }}
    [data-testid="stMetricValue"] {{
        color: #FFF5E6 !important;
    }}

    div[data-testid="stPlotlyChart"] {{
        background: rgba(42, 28, 18, 0.6) !important;
        border: 1px solid rgba(212, 136, 46, 0.25) !important;
        border-radius: 14px;
        overflow: hidden;
    }}

    .stCaption, div[data-testid="stCaptionContainer"] {{
        color: #C4A882 !important;
        opacity: 0.85;
    }}

    div[data-testid="stForm"] {{
        background: rgba(42, 28, 18, 0.45) !important;
        border: 1px solid rgba(212, 136, 46, 0.25) !important;
        border-radius: 14px;
        padding: 1rem;
    }}

    div[data-testid="stVerticalBlockBorderWrapper"] > div {{
        background: rgba(42, 28, 18, 0.75) !important;
        border-color: rgba(212, 136, 46, 0.25) !important;
    }}

    .theme-pill-badge {{
        display: inline-flex;
        align-items: center;
        gap: 0.4rem;
        font-size: 0.85rem;
        font-weight: 700;
        color: {ACCENT_YELLOW};
        background: rgba(252, 191, 73, 0.15);
        border: 1px solid rgba(252, 191, 73, 0.25);
        border-radius: 20px;
        padding: 0.2rem 0.65rem;
        margin-bottom: 0.3rem;
    }}

    ::-webkit-scrollbar {{
        width: 8px;
        height: 8px;
    }}
    ::-webkit-scrollbar-track {{
        background: rgba(26, 15, 10, 0.5);
    }}
    ::-webkit-scrollbar-thumb {{
        background: rgba(212, 136, 46, 0.35);
        border-radius: 4px;
    }}
    ::-webkit-scrollbar-thumb:hover {{
        background: rgba(247, 127, 0, 0.5);
    }}
    </style>
    """


def on_theme_change() -> None:
    """Callback fired immediately when theme switcher value changes."""
    selected = st.session_state.get("theme_selector_header")
    if selected and selected in THEME_OPTIONS:
        st.session_state.theme = selected


def render_theme_switcher(location: str = "header") -> None:
    """Render the theme switcher control with its icon."""
    if "theme" not in st.session_state or st.session_state.theme not in THEME_OPTIONS:
        st.session_state.theme = DEFAULT_THEME

    current_theme = st.session_state.theme

    # Initialize widget state if missing
    if "theme_selector_header" not in st.session_state or st.session_state.theme_selector_header not in THEME_OPTIONS:
        st.session_state.theme_selector_header = current_theme

    st.markdown(
        '<div class="theme-pill-badge"><span>🎨</span><span>THEME</span></div>',
        unsafe_allow_html=True,
    )
    st.segmented_control(
        "Theme Selector",
        options=THEME_OPTIONS,
        key="theme_selector_header",
        on_change=on_theme_change,
        label_visibility="collapsed",
    )
