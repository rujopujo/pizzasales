"""Reusable Streamlit presentation elements in warm pizza light mode."""

from __future__ import annotations

from html import escape

import streamlit as st

from src.config.settings import (
    ACCENT_AMBER,
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

    html, body, [class*="css"] {{
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    }}

    /* Light Mode Background with subtle warm gradient mesh */
    .stApp {{
        background-color: {BG};
        background-image: 
            radial-gradient(circle at 5% 0%, rgba(254, 215, 170, 0.35) 0%, transparent 40%),
            radial-gradient(circle at 95% 0%, rgba(254, 202, 202, 0.30) 0%, transparent 40%),
            radial-gradient(circle at 50% 100%, rgba(254, 240, 138, 0.15) 0%, transparent 50%);
        color: {TEXT};
    }}

    .block-container {{
        padding-top: 1.25rem;
        padding-bottom: 2.5rem;
        max-width: 1550px;
    }}

    /* Sidebar Styling - Warm Soft Cream */
    section[data-testid="stSidebar"] {{
        background: linear-gradient(180deg, #FFF7ED 0%, #FFEDD5 100%);
        border-right: 1px solid rgba(234, 88, 12, 0.15);
        box-shadow: 2px 0 16px rgba(234, 88, 12, 0.04);
    }}
    section[data-testid="stSidebar"] .block-container {{
        padding-top: 1.5rem;
    }}
    section[data-testid="stSidebar"] h1, 
    section[data-testid="stSidebar"] h2, 
    section[data-testid="stSidebar"] h3 {{
        color: #9A3412;
        font-weight: 700;
    }}

    /* Headings with Vibrant Pizza Gradient (Red to Orange to Amber) */
    h1 {{
        background: linear-gradient(135deg, {ACCENT_RED} 0%, {ACCENT_ORANGE} 50%, {ACCENT_AMBER} 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
        letter-spacing: -0.025em;
    }}
    h2, h3, h4 {{
        color: #7C2D12;
        font-weight: 700;
        letter-spacing: -0.015em;
    }}

    /* Metric Cards Grid */
    .kpi-grid {{
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 1rem;
        margin: 0.8rem 0 1.5rem;
    }}

    /* Porcelain KPI Card with Warm Border & Smooth Hover Lift */
    .porcelain-card {{
        background: {CARD_BG};
        border: 1px solid rgba(234, 88, 12, 0.18);
        border-radius: 14px;
        padding: 1.15rem 1.25rem;
        box-shadow: 0 4px 18px -2px rgba(234, 88, 12, 0.07), 0 1px 3px rgba(0, 0, 0, 0.03);
        transition: transform 0.22s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.22s ease, border-color 0.22s ease;
        position: relative;
        overflow: hidden;
    }}
    .porcelain-card:hover {{
        transform: translateY(-3px);
        box-shadow: 0 12px 28px -4px rgba(234, 88, 12, 0.14), 0 4px 8px rgba(0, 0, 0, 0.04);
        border-color: rgba(234, 88, 12, 0.40);
    }}

    .kpi-label {{
        color: {MUTED_TEXT};
        font-size: 0.82rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        line-height: 1.3;
    }}
    .kpi-value {{
        color: #1C1917;
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

    /* Streamlit Tabs - Pill Design with Radiant Active Orange */
    div[data-baseweb="tab-list"] {{
        background: rgba(254, 215, 170, 0.35);
        padding: 0.35rem;
        border-radius: 12px;
        gap: 0.35rem;
        border: 1px solid rgba(234, 88, 12, 0.12);
        margin-bottom: 1.2rem;
    }}
    button[data-baseweb="tab"] {{
        border-radius: 9px;
        padding: 0.55rem 1.15rem;
        font-weight: 600;
        font-size: 0.92rem;
        color: #78716C !important;
        border: none !important;
        background: transparent !important;
        transition: all 0.2s ease;
    }}
    button[data-baseweb="tab"]:hover {{
        color: #9A3412 !important;
        background: rgba(255, 255, 255, 0.6) !important;
    }}
    button[data-baseweb="tab"][aria-selected="true"] {{
        background: linear-gradient(135deg, {ACCENT_ORANGE} 0%, {ACCENT_RED} 100%) !important;
        color: #FFFFFF !important;
        box-shadow: 0 4px 14px rgba(234, 88, 12, 0.30);
    }}
    div[data-baseweb="tab-highlight"] {{
        display: none !important;
    }}

    /* Streamlit Buttons - Warm Red/Orange Gradient */
    div.stButton > button {{
        background: linear-gradient(135deg, {ACCENT_ORANGE} 0%, {ACCENT_RED} 100%);
        color: #FFFFFF !important;
        font-weight: 600;
        border-radius: 10px;
        border: none;
        padding: 0.55rem 1.25rem;
        box-shadow: 0 3px 12px rgba(234, 88, 12, 0.22);
        transition: all 0.2s ease;
    }}
    div.stButton > button:hover {{
        background: linear-gradient(135deg, #F97316 0%, #EF4444 100%);
        box-shadow: 0 6px 18px rgba(234, 88, 12, 0.35);
        transform: translateY(-1px);
        color: #FFFFFF !important;
    }}

    /* Dataframes & Expanders */
    div[data-testid="stDataFrame"] {{
        background: #FFFFFF;
        border: 1px solid rgba(234, 88, 12, 0.18);
        border-radius: 12px;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.02);
    }}
    div[data-testid="stExpander"] {{
        background: #FFFFFF;
        border: 1px solid rgba(234, 88, 12, 0.18);
        border-radius: 12px;
    }}

    /* Inputs, Selectboxes, Number Inputs */
    div[data-baseweb="select"] > div {{
        background: #FFFFFF;
        border-color: rgba(234, 88, 12, 0.25);
        border-radius: 9px;
    }}
    div[data-baseweb="input"] {{
        background: #FFFFFF;
        border-color: rgba(234, 88, 12, 0.25);
        border-radius: 9px;
    }}

    /* Sliders Accent */
    div[data-testid="stSlider"] {{
        color: {ACCENT_ORANGE};
    }}

    /* Hero Banner Badge */
    .hero-badge {{
        display: inline-flex;
        align-items: center;
        gap: 0.4rem;
        background: linear-gradient(135deg, #FEF3C7 0%, #FEE2E2 100%);
        color: #9A3412;
        padding: 0.28rem 0.75rem;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 700;
        letter-spacing: 0.03em;
        border: 1px solid rgba(234, 88, 12, 0.20);
        margin-bottom: 0.5rem;
    }}

    @media (max-width: 600px) {{
        .block-container h1 {{
            font-size: 1.8rem;
        }}
    }}
    </style>
    """, unsafe_allow_html=True)


def metric_card(label: str, value: str, accent: str = ACCENT_ORANGE) -> str:
    return (
        '<div class="porcelain-card">'
        f'<div class="kpi-label">{escape(label)}</div>'
        f'<div class="kpi-value">{escape(value)}</div>'
        f'<div class="kpi-accent-pill" style="background:{escape(accent)};"></div>'
        '</div>'
    )
