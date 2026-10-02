"""Reusable Streamlit presentation elements in immersive pizzeria dark theme."""

from __future__ import annotations

from html import escape

import streamlit as st

from src.config.settings import (
    ACCENT_AMBER,
    ACCENT_GREEN,
    ACCENT_ORANGE,
    ACCENT_RED,
    ACCENT_YELLOW,
    BG,
    BORDER,
    CARD_BG,
    MUTED_TEXT,
    TEXT,
)


def inject_css() -> None:
    st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;800;900&display=swap');

    html, body, [class*="css"] {{
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    }}

    /* ── Dark Brick Oven Background with Warm Glow ── */
    .stApp {{
        background-color: {BG};
        background-image:
            radial-gradient(ellipse at 10% 0%, rgba(231, 57, 70, 0.12) 0%, transparent 50%),
            radial-gradient(ellipse at 90% 0%, rgba(247, 127, 0, 0.10) 0%, transparent 45%),
            radial-gradient(ellipse at 50% 100%, rgba(252, 191, 73, 0.06) 0%, transparent 55%),
            radial-gradient(circle at 50% 50%, rgba(42, 28, 18, 0.4) 0%, transparent 70%);
        color: {TEXT};
    }}

    .block-container {{
        padding-top: 1.25rem;
        padding-bottom: 2.5rem;
        max-width: 1550px;
    }}

    /* ── Sidebar — Dark Wood Panel ── */
    section[data-testid="stSidebar"] {{
        background: linear-gradient(180deg, #211410 0%, #1A0F0A 40%, #2A1C12 100%);
        border-right: 1px solid {BORDER};
        box-shadow: 3px 0 24px rgba(0, 0, 0, 0.4);
    }}
    section[data-testid="stSidebar"] .block-container {{
        padding-top: 1.5rem;
    }}
    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3 {{
        color: {ACCENT_YELLOW};
        font-weight: 700;
    }}
    section[data-testid="stSidebar"] p,
    section[data-testid="stSidebar"] label,
    section[data-testid="stSidebar"] span {{
        color: {MUTED_TEXT};
    }}

    /* ── Headings — Fiery Gradient ── */
    h1 {{
        font-family: 'Playfair Display', 'Georgia', serif;
        background: linear-gradient(135deg, {ACCENT_YELLOW} 0%, {ACCENT_ORANGE} 40%, {ACCENT_RED} 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 900;
        letter-spacing: -0.03em;
    }}
    h2, h3 {{
        color: {ACCENT_YELLOW};
        font-weight: 700;
        letter-spacing: -0.015em;
    }}
    h4 {{
        color: {ACCENT_ORANGE};
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
        background: {CARD_BG};
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid {BORDER};
        border-radius: 16px;
        padding: 1.2rem 1.3rem;
        box-shadow:
            0 4px 24px -4px rgba(0, 0, 0, 0.35),
            0 0 0 1px rgba(212, 136, 46, 0.05),
            inset 0 1px 0 rgba(255, 245, 230, 0.04);
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
        opacity: 0;
        transition: opacity 0.25s ease;
    }}
    .porcelain-card:hover {{
        transform: translateY(-4px);
        box-shadow:
            0 16px 40px -8px rgba(247, 127, 0, 0.18),
            0 8px 16px rgba(0, 0, 0, 0.25);
        border-color: rgba(247, 127, 0, 0.45);
    }}
    .porcelain-card:hover::before {{
        opacity: 1;
    }}

    .kpi-label {{
        color: {MUTED_TEXT};
        font-size: 0.8rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.06em;
        line-height: 1.3;
    }}
    .kpi-value {{
        color: {TEXT};
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
        background: rgba(42, 28, 18, 0.65);
        backdrop-filter: blur(12px);
        padding: 0.4rem;
        border-radius: 14px;
        gap: 0.35rem;
        border: 1px solid {BORDER};
        margin-bottom: 1.2rem;
    }}
    button[data-baseweb="tab"] {{
        border-radius: 10px;
        padding: 0.6rem 1.2rem;
        font-weight: 600;
        font-size: 0.92rem;
        color: {MUTED_TEXT} !important;
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
        box-shadow: 0 4px 18px rgba(247, 127, 0, 0.35), 0 0 0 1px rgba(247, 127, 0, 0.2);
    }}
    div[data-baseweb="tab-highlight"] {{
        display: none !important;
    }}

    /* ── Buttons — Oven Flame Gradient ── */
    div.stButton > button {{
        background: linear-gradient(135deg, {ACCENT_ORANGE} 0%, {ACCENT_RED} 100%);
        color: #FFFFFF !important;
        font-weight: 600;
        border-radius: 11px;
        border: none;
        padding: 0.6rem 1.3rem;
        box-shadow: 0 4px 16px rgba(247, 127, 0, 0.25);
        transition: all 0.2s ease;
    }}
    div.stButton > button:hover {{
        background: linear-gradient(135deg, #FF8C1A 0%, #FF4757 100%);
        box-shadow: 0 8px 24px rgba(247, 127, 0, 0.40);
        transform: translateY(-2px);
        color: #FFFFFF !important;
    }}

    /* ── Form Submit Button ── */
    button[kind="primaryFormSubmit"] {{
        background: linear-gradient(135deg, {ACCENT_ORANGE} 0%, {ACCENT_RED} 100%) !important;
        color: #FFFFFF !important;
        font-weight: 600 !important;
        border-radius: 11px !important;
        border: none !important;
        box-shadow: 0 4px 16px rgba(247, 127, 0, 0.25) !important;
    }}

    /* ── Dataframes & Expanders — Dark Glass ── */
    div[data-testid="stDataFrame"] {{
        background: rgba(42, 28, 18, 0.6);
        border: 1px solid {BORDER};
        border-radius: 14px;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2);
    }}
    div[data-testid="stExpander"] {{
        background: rgba(42, 28, 18, 0.5);
        border: 1px solid {BORDER};
        border-radius: 14px;
    }}
    div[data-testid="stExpander"] summary {{
        color: {ACCENT_YELLOW};
        font-weight: 600;
    }}

    /* ── Inputs, Selects, Number Inputs ── */
    div[data-baseweb="select"] > div {{
        background: rgba(42, 28, 18, 0.7) !important;
        border-color: {BORDER} !important;
        border-radius: 10px;
        color: {TEXT};
    }}
    div[data-baseweb="input"] {{
        background: rgba(42, 28, 18, 0.7) !important;
        border-color: {BORDER} !important;
        border-radius: 10px;
    }}
    div[data-baseweb="input"] input {{
        color: {TEXT} !important;
    }}

    /* ── Sliders ── */
    div[data-testid="stSlider"] {{
        color: {ACCENT_ORANGE};
    }}

    /* ── Hero Banner Badge ── */
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

    /* ── Section Divider ── */
    .pizza-divider {{
        text-align: center;
        margin: 1.5rem 0 1rem;
        color: {MUTED_TEXT};
        font-size: 1.2rem;
        letter-spacing: 0.5em;
        opacity: 0.5;
    }}

    /* ── Info, Warning, Success boxes ── */
    div[data-testid="stAlert"] {{
        border-radius: 12px;
    }}

    /* ── Streamlit metric overrides ── */
    div[data-testid="stMetric"] {{
        background: {CARD_BG};
        backdrop-filter: blur(12px);
        border: 1px solid {BORDER};
        border-radius: 14px;
        padding: 1rem;
    }}
    div[data-testid="stMetric"] label {{
        color: {MUTED_TEXT} !important;
    }}
    [data-testid="stMetricValue"] {{
        color: {TEXT} !important;
    }}

    /* ── Plotly chart container ── */
    div[data-testid="stPlotlyChart"] {{
        border-radius: 14px;
        overflow: hidden;
    }}

    /* ── Caption text ── */
    .stCaption, div[data-testid="stCaptionContainer"] {{
        color: {MUTED_TEXT} !important;
        opacity: 0.85;
    }}

    /* ── Forms ── */
    div[data-testid="stForm"] {{
        background: rgba(42, 28, 18, 0.45);
        border: 1px solid {BORDER};
        border-radius: 14px;
        padding: 1rem;
    }}

    /* ── Scrollbar styling ── */
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

    @media (max-width: 600px) {{
        .block-container h1 {{
            font-size: 1.8rem;
        }}
    }}
    </style>
    """, unsafe_allow_html=True)


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
