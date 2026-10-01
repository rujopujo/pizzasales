"""Experiment 3: Predictive Analytics - Regression Modeling & Price Inference.

Demonstrates:
- Feature extraction & one-hot encoding for categorical attributes
- Model training: Ordinary Least Squares (OLS), Ridge Regularization, and Random Forest Regressor
- Benchmark comparison using statistical metrics: R², Adjusted R², MAE, RMSE, MAPE (%)
- Live basket price inference under dynamic conditions (size uplift, peak-time surge multiplier)
"""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.mining import predict_basket_price, train_regressors
from src.warehouse import joined_sales


def main():
    print("=" * 70)
    print(" DWM LAB EXPERIMENT 3: REGRESSION MODELING & PREDICTIVE ANALYTICS")
    print("=" * 70)

    sales = joined_sales()
    print(f"\n[Step 1] Loading Dataset for Regression... ({len(sales):,} records)")

    # 1. Train Regression Models
    print("\n[Step 2] Training Regressors (OLS Linear, Ridge, Random Forest)...")
    print("  -> Train/Test Split: 75% Training / 25% Held-out Evaluation")
    result = train_regressors(sales)

    # 2. Performance Evaluation Table
    print("\n[Step 3] Model Performance Comparison:")
    print(result.metrics.to_string(index=False))

    # 3. Best Model Selection & Inference Sandbox
    print("\n[Step 4] Predictive Price Inference Simulation:")
    test_cases = [
        {"desc": "Standard Order: 2 Medium Classic Pizzas at 7 PM", "qty": 2, "base": 12.0, "uplift": 2.0, "surge": 1.0, "size": "M", "cat": "Classic", "hour": 19},
        {"desc": "Large Family Order: 4 Large Supreme Pizzas at 8 PM (Weekend Surge 1.25x)", "qty": 4, "base": 14.5, "uplift": 4.5, "surge": 1.25, "size": "L", "cat": "Supreme", "hour": 20},
        {"desc": "Lunch Single Order: 1 Small Veggie Pizza at 1 PM (Off-Peak)", "qty": 1, "base": 11.5, "uplift": 0.0, "surge": 1.0, "size": "S", "cat": "Veggie", "hour": 13},
    ]

    rf_model = result.models["Random Forest Regressor"]

    for case in test_cases:
        print(f"\n  • Scenario: {case['desc']}")
        pred = predict_basket_price(
            rf_model,
            quantity=case["qty"],
            base_price=case["base"],
            size_uplift=case["uplift"],
            surge_multiplier=case["surge"],
            pizza_size=case["size"],
            pizza_category=case["cat"],
            order_hour=case["hour"],
        )
        print(f"    - Effective Unit Price: ${pred['effective_unit_price']:.2f}")
        print(f"    - Random Forest Predicted Total: ${pred['model_prediction']:.2f}")
        print(f"    - Arithmetic Ground Truth Total: ${pred['arithmetic_total']:.2f}")

    print("\n" + "=" * 70)
    print(" Experiment 3 Completed Successfully.")
    print("=" * 70)


if __name__ == "__main__":
    main()
