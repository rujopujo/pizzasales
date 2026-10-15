"""Small end-to-end checks for the warehouse and model contracts."""

import unittest

import numpy as np

from src.analytics import executive_kpis
from src.classification_engine import classify_order, train_decision_tree
from src.regression_engine import predict_basket_price, train_regressors
from src.warehouse_engine import build_star_schema, joined_sales, roll_up, slice_dice


class PlatformSmokeTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sales = joined_sales()

    def test_warehouse_totals_and_filters(self):
        schema = build_star_schema()
        self.assertEqual(len(self.sales), 3000)
        self.assertEqual(len(schema["Fact_Sales"]), len(self.sales))
        self.assertTrue(np.allclose(self.sales["total_price"], self.sales["quantity"] * self.sales["unit_price"]))
        monthly = roll_up(self.sales, "Month", ["pizza_category"])
        self.assertAlmostEqual(monthly["revenue"].sum(), executive_kpis(self.sales)["Gross Revenue"])
        rush = slice_dice(self.sales, weekend_only=True, peak_only=True)
        self.assertTrue(rush["is_weekend"].all())
        self.assertTrue(rush["peak_period"].isin(["Lunch", "Dinner"]).all())

    def test_model_inference(self):
        regression = train_regressors(self.sales)
        self.assertEqual(len(regression.metrics), 3)
        basket = predict_basket_price(regression.models["Random Forest Regressor"], 2, 12, 2, 1, "M", "Classic", 19)
        self.assertAlmostEqual(basket["arithmetic_total"], 28)
        self.assertGreater(basket["model_prediction"], 0)
        tree = train_decision_tree(self.sales)
        order = classify_order(tree.model, 2, 15, 19, "M", "Classic")
        self.assertIn(order["tier"], {"Budget", "Standard", "Premium"})
        self.assertAlmostEqual(sum(order["probabilities"].values()), 1)

    def test_theme_system(self):
        from src.ui.theme import (
            DEFAULT_THEME, THEME_LEGACY, THEME_LIGHT,
            THEME_OPTIONS, get_chart_theme, get_theme_css, normalize_theme,
        )
        self.assertIn("Light", DEFAULT_THEME)
        self.assertEqual(len(THEME_OPTIONS), 2)
        self.assertEqual(normalize_theme(THEME_LIGHT), "light")
        self.assertEqual(normalize_theme(THEME_LEGACY), "legacy")

        light_cfg = get_chart_theme("light")
        self.assertEqual(light_cfg["template"], "plotly_white")
        self.assertEqual(light_cfg["font_color"], "#0F172A")

        legacy_cfg = get_chart_theme("legacy")
        self.assertEqual(legacy_cfg["template"], "plotly_dark")
        self.assertEqual(legacy_cfg["font_color"], "#FFF5E6")

        self.assertIn("#F8FAFC", get_theme_css("light"))
        self.assertIn("#1A0F0A", get_theme_css("legacy"))

    def test_auth_system(self):
        from src.ui.auth import DEMO_CREDENTIALS, is_authenticated, login, logout
        import streamlit as st

        # Initial state should be unauthenticated
        st.session_state.clear()
        self.assertFalse(is_authenticated())

        # Demo credentials exist
        self.assertIn("admin", DEMO_CREDENTIALS)
        self.assertEqual(DEMO_CREDENTIALS["admin"], "password")

        # Test login
        login("admin")
        self.assertTrue(is_authenticated())
        self.assertEqual(st.session_state.get("username"), "admin")


if __name__ == "__main__":
    unittest.main()
