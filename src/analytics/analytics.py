"""Executive measures and Plotly sales visualizations in immersive pizzeria dark theme."""

from __future__ import annotations

import numpy as np
import pandas as pd
import plotly.graph_objects as go

from src.config.settings import (
    ACCENT_AMBER,
    ACCENT_GREEN,
    ACCENT_ORANGE,
    ACCENT_RED,
    ACCENT_YELLOW,
    CATEGORIES,
    CHART_FONT,
    CHART_GRID,
    CHART_PAPER_BG,
    CHART_PLOT_BG,
    MUTED_TEXT,
    PIZZA_COLORSCALE,
    TEXT,
)

DAY_ORDER = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

_CATEGORY_COLORS = [ACCENT_RED, ACCENT_GREEN, ACCENT_ORANGE, ACCENT_YELLOW]


def _style(fig: go.Figure, height: int = 380) -> go.Figure:
    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor=CHART_PAPER_BG,
        plot_bgcolor=CHART_PLOT_BG,
        font=dict(color=TEXT, family=CHART_FONT),
        margin=dict(l=25, r=25, t=50, b=35),
        height=height,
        legend=dict(
            bgcolor="rgba(42, 28, 18, 0.6)",
            bordercolor="rgba(212, 136, 46, 0.2)",
            borderwidth=1,
            font=dict(color=TEXT),
        ),
    )
    fig.update_xaxes(showgrid=True, gridcolor=CHART_GRID, zeroline=False)
    fig.update_yaxes(showgrid=True, gridcolor=CHART_GRID, zeroline=False)
    return fig


def executive_kpis(frame: pd.DataFrame) -> dict[str, float | int]:
    revenue = float(frame["total_price"].sum())
    pizzas = int(frame["quantity"].sum())
    orders = int(frame["order_id"].nunique())
    profit = float((frame["total_price"] * frame["margin_rate"]).sum())
    return {
        "Gross Revenue": revenue,
        "Total Pizzas Sold": pizzas,
        "Total Unique Orders": orders,
        "Average Order Value": revenue / orders if orders else 0.0,
        "Average Margin %": 100 * profit / revenue if revenue else 0.0,
    }


def category_waterfall(frame: pd.DataFrame) -> go.Figure:
    values = frame.groupby("pizza_category")["total_price"].sum().reindex(CATEGORIES, fill_value=0)
    colors = _CATEGORY_COLORS[:len(values)]
    fig = go.Figure(go.Waterfall(
        x=[*values.index, "Total"],
        y=[*values.tolist(), 0],
        measure=["relative"] * len(values) + ["total"],
        connector={"line": {"color": "rgba(196, 168, 130, 0.25)", "width": 1.5}},
        increasing={"marker": {"color": ACCENT_ORANGE}},
        totals={"marker": {"color": ACCENT_RED}},
        text=[f"${value:,.0f}" for value in values] + [f"${values.sum():,.0f}"],
        textposition="outside",
        textfont=dict(color=TEXT),
        hovertemplate="%{x}<br>$%{y:,.2f}<extra></extra>",
    ))
    fig.update_layout(title="Revenue contribution by category", yaxis_title="Revenue ($)")
    return _style(fig)


def hourly_sales_heatmap(frame: pd.DataFrame) -> go.Figure:
    hours = list(range(10, 24))
    pivot = frame.pivot_table(index="day_of_week", columns="hour", values="total_price", aggfunc="sum", fill_value=0)
    pivot = pivot.reindex(index=DAY_ORDER, columns=hours, fill_value=0)
    fig = go.Figure(go.Heatmap(
        z=pivot.to_numpy(),
        x=hours,
        y=DAY_ORDER,
        colorscale=PIZZA_COLORSCALE,
        colorbar=dict(title="Revenue ($)", tickfont=dict(color=MUTED_TEXT), title_font=dict(color=TEXT)),
        hovertemplate="%{y}, %{x}:00<br>$%{z:,.2f}<extra></extra>",
    ))
    fig.update_layout(title="Revenue by weekday and hour", xaxis_title="Hour of day", yaxis_title="Day of week")
    fig.update_yaxes(autorange="reversed")
    return _style(fig)


def pareto_chart(frame: pd.DataFrame) -> go.Figure:
    ranked = frame.groupby("pizza_name")["total_price"].sum().sort_values(ascending=False)
    cumulative = ranked.cumsum() / ranked.sum() * 100 if ranked.sum() else ranked.astype(float)
    fig = go.Figure()
    fig.add_bar(
        x=ranked.index,
        y=ranked.values,
        name="Revenue",
        marker_color=ACCENT_ORANGE,
        marker_line=dict(color=ACCENT_AMBER, width=0.5),
        hovertemplate="%{x}<br>$%{y:,.2f}<extra></extra>",
    )
    fig.add_scatter(
        x=ranked.index,
        y=cumulative.values,
        name="Cumulative %",
        mode="lines+markers",
        yaxis="y2",
        line=dict(color=ACCENT_YELLOW, width=3),
        marker=dict(size=6, color=ACCENT_YELLOW, line=dict(color=ACCENT_RED, width=1.5)),
        hovertemplate="%{x}<br>%{y:.1f}% cumulative<extra></extra>",
    )
    fig.add_hline(
        y=80,
        yref="y2",
        line_dash="dash",
        line_color=ACCENT_RED,
        annotation_text="80% Cutoff",
        annotation_position="top left",
        annotation_font=dict(color=ACCENT_RED),
    )
    fig.update_layout(
        title="Pizza revenue Pareto (80/20 Law)",
        xaxis_title="Pizza",
        yaxis_title="Revenue ($)",
        yaxis2=dict(title="Cumulative revenue (%)", overlaying="y", side="right", range=[0, 105],
                    gridcolor=CHART_GRID, tickfont=dict(color=MUTED_TEXT)),
        legend=dict(orientation="h", y=1.12),
    )
    fig.update_xaxes(tickangle=-40)
    return _style(fig, 460)
