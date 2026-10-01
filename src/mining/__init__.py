"""Data Mining package: Price regression, decision trees, feature relevance, and inference."""

from src.mining.classification_engine import (
    COLORS,
    TIERS,
    ClassificationResult,
    attribute_relevance,
    classify_order,
    confusion_chart,
    order_tiers,
    relevance_chart,
    roc_chart,
    train_decision_tree,
)
from src.mining.regression_engine import (
    CATEGORICAL,
    FEATURES,
    NUMERIC,
    RegressionResult,
    feature_frame,
    predict_basket_price,
    qq_plot,
    residual_plot,
    train_regressors,
)

__all__ = [
    # Classification
    "COLORS",
    "TIERS",
    "ClassificationResult",
    "attribute_relevance",
    "classify_order",
    "confusion_chart",
    "order_tiers",
    "relevance_chart",
    "roc_chart",
    "train_decision_tree",
    # Regression
    "CATEGORICAL",
    "FEATURES",
    "NUMERIC",
    "RegressionResult",
    "feature_frame",
    "predict_basket_price",
    "qq_plot",
    "residual_plot",
    "train_regressors",
]
