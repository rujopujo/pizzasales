"""Authentication module for Pizza MDW: Login, session verification, and logout."""

from __future__ import annotations

import streamlit as st

from src.ui.theme import render_theme_switcher

# Demo credentials
DEMO_CREDENTIALS = {
    "admin": "password",
    "analyst": "pizza123",
}


def is_authenticated() -> bool:
    """Check if the user is currently authenticated."""
    return bool(st.session_state.get("authenticated", False))


def login(username: str) -> None:
    """Set authentication session state."""
    st.session_state.authenticated = True
    st.session_state.username = username


def logout() -> None:
    """Clear authentication session state."""
    st.session_state.authenticated = False
    st.session_state.username = None
    st.rerun()


def render_user_profile() -> None:
    """Render authenticated user badge and logout button in the sidebar."""
    if not is_authenticated():
        return

    username = st.session_state.get("username", "admin")
    st.sidebar.markdown(
        f"""
        <div style="
            display: flex;
            align-items: center;
            justify-content: space-between;
            background: rgba(247, 127, 0, 0.08);
            border: 1px solid rgba(247, 127, 0, 0.2);
            border-radius: 12px;
            padding: 0.5rem 0.8rem;
            margin-bottom: 0.8rem;
        ">
            <div style="display: flex; align-items: center; gap: 0.5rem;">
                <span style="font-size: 1.2rem;">👤</span>
                <div>
                    <div style="font-size: 0.85rem; font-weight: 700;">{username.title()}</div>
                    <div style="font-size: 0.7rem; opacity: 0.7;">Online · Verified</div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if st.sidebar.button("🚪 Sign Out", key="sidebar_logout_btn", width="stretch"):
        logout()


def render_login_page() -> None:
    """Render the glassmorphic login interface."""
    # Hide sidebar during login
    st.markdown(
        """
        <style>
        section[data-testid="stSidebar"] {
            display: none !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Top bar with theme toggle
    header_col, theme_col = st.columns([3, 1.8], vertical_alignment="center")
    with header_col:
        st.markdown(
            '<div class="hero-badge">🔒 SECURE ENTERPRISE PORTAL</div>',
            unsafe_allow_html=True,
        )
    with theme_col:
        render_theme_switcher("header")

    st.markdown("<div style='height: 1.5rem;'></div>", unsafe_allow_html=True)

    # Centered card layout
    _, center_col, _ = st.columns([1, 1.6, 1])

    with center_col:
        st.markdown(
            """
            <div style="text-align: center; margin-bottom: 1.5rem;">
                <div style="font-size: 3.2rem; line-height: 1; margin-bottom: 0.5rem;">🍕</div>
                <h2 style="margin: 0; font-size: 1.75rem; font-weight: 800;">Pizza MDW Intelligence</h2>
                <p style="margin: 0.35rem 0 0; font-size: 0.9rem; opacity: 0.75;">
                    Sign in to access sales analytics, star schema OLAP, and ML models
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        with st.container(border=True):
            # Quick fill demo button
            fill_col1, fill_col2 = st.columns([1, 1])
            with fill_col1:
                if st.button("⚡ Fill Admin", width="stretch", key="fill_admin_btn"):
                    st.session_state["login_user_input"] = "admin"
                    st.session_state["login_pass_input"] = "password"
            with fill_col2:
                if st.button("🍕 Fill Analyst", width="stretch", key="fill_analyst_btn"):
                    st.session_state["login_user_input"] = "analyst"
                    st.session_state["login_pass_input"] = "pizza123"

            with st.form("login_form", clear_on_submit=False):
                username_val = st.session_state.get("login_user_input", "")
                password_val = st.session_state.get("login_pass_input", "")

                username = st.text_input(
                    "Username",
                    value=username_val,
                    placeholder="Enter username (e.g. admin)",
                    key="input_username",
                )
                password = st.text_input(
                    "Password",
                    value=password_val,
                    type="password",
                    placeholder="Enter password (e.g. password)",
                    key="input_password",
                )

                st.markdown("<div style='height: 0.5rem;'></div>", unsafe_allow_html=True)
                submitted = st.form_submit_button("🚀 Sign In", width="stretch")

                if submitted:
                    uname = username.strip().lower()
                    pwd = password.strip()
                    if uname in DEMO_CREDENTIALS and DEMO_CREDENTIALS[uname] == pwd:
                        login(uname)
                        st.toast(f"Welcome back, {uname.title()}! 🍕", icon="✅")
                        st.rerun()
                    elif not uname or not pwd:
                        st.warning("Please enter both username and password.")
                    else:
                        st.error("Invalid credentials. Please use demo credentials below.")

        # Demo Credentials Reference Box
        st.markdown(
            """
            <div style="
                margin-top: 1rem;
                padding: 0.75rem 1rem;
                border-radius: 12px;
                background: rgba(247, 127, 0, 0.06);
                border: 1px dashed rgba(247, 127, 0, 0.3);
                font-size: 0.82rem;
            ">
                <div style="font-weight: 700; margin-bottom: 0.25rem; display: flex; align-items: center; gap: 0.4rem;">
                    <span>🔑</span><span>Demo Credentials</span>
                </div>
                <div style="display: flex; justify-content: space-between; opacity: 0.85;">
                    <span>Admin: <code>admin</code> / <code>password</code></span>
                    <span>Analyst: <code>analyst</code> / <code>pizza123</code></span>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
