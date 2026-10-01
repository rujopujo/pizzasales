"""Experiment 4: Supervised Learning - Decision Tree Classification & Feature Selection.

Demonstrates:
- Feature Relevance Ranking using Mutual Information and Random Forest Gini Importance
- Discretizing continuous order value into spend tiers (Budget < $20, Standard $20-$50, Premium > $50)
- Training Decision Tree Classifiers using Gini Impurity and Information Gain (Entropy)
- Comprehensive evaluation: Precision, Recall, F1-score, Support, Confusion Matrix, and ROC/AUC
- Live classification inference of new order queries with class probability distributions
"""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.mining import (
    attribute_relevance,
    classify_order,
    order_tiers,
    train_decision_tree,
)
from src.warehouse import joined_sales


def main():
    print("=" * 70)
    print(" DWM LAB EXPERIMENT 4: DECISION TREE CLASSIFICATION & FEATURE MINING")
    print("=" * 70)

    sales = joined_sales()
    print(f"\n[Step 1] Loading Dataset for Classification... ({len(sales):,} records)")

    # 1. Target Tier Distribution
    tiers = order_tiers(sales)
    print("\n[Step 2] Order Tier Target Distribution:")
    print("  • Budget (< $20):     ", (tiers == "Budget").sum())
    print("  • Standard ($20-$50): ", (tiers == "Standard").sum())
    print("  • Premium (> $50):    ", (tiers == "Premium").sum())

    # 2. Attribute Relevance & Feature Ranking
    print("\n[Step 3] Computing Feature Relevance (Mutual Information & RF Importance)...")
    relevance = attribute_relevance(sales)
    print(relevance.to_string(index=False))

    # 3. Train Decision Tree Classifier
    print("\n[Step 4] Training Decision Tree Classifier (Criterion: Gini, Max Depth: 5)...")
    tree_result = train_decision_tree(sales, max_depth=5, min_samples_split=8, criterion="gini")

    print("\n  • Classification Performance Report (Test Set):")
    print(tree_result.report.to_string(index=False))

    print("\n  • One-vs-Rest AUC per Class:")
    for tier, auc_val in tree_result.auc.items():
        print(f"    - {tier:<10} AUC: {auc_val:.4f}")

    print("\n  • Normalized Confusion Matrix:")
    print("    Classes:", tree_result.classes.tolist())
    print(tree_result.confusion.round(3))

    # 4. Interactive Order Tier Inference
    print("\n[Step 5] Live Order Tier Inference Sandbox:")
    samples = [
        {"desc": "Order A: 1 Small Classic pizza @ $11.00 at 2 PM", "qty": 1, "price": 11.0, "hour": 14, "size": "S", "cat": "Classic"},
        {"desc": "Order B: 2 Medium Veggie pizzas @ $15.50 at 8 PM", "qty": 2, "price": 15.5, "hour": 20, "size": "M", "cat": "Veggie"},
        {"desc": "Order C: 4 XXL Supreme pizzas @ $24.50 at 9 PM", "qty": 4, "price": 24.5, "hour": 21, "size": "XXL", "cat": "Supreme"},
    ]

    for item in samples:
        print(f"\n  • Scenario: {item['desc']}")
        pred = classify_order(
            tree_result.model,
            quantity=item["qty"],
            unit_price=item["price"],
            order_hour=item["hour"],
            pizza_size=item["size"],
            pizza_category=item["cat"],
        )
        print(f"    - Basket Value: ${pred['basket_total']:.2f}")
        print(f"    - Classified Tier: >> {pred['tier']} <<")
        print("    - Class Probabilities:")
        for tier, prob in pred["probabilities"].items():
            print(f"      * {tier:<10}: {prob * 100:.1f}%")

    print("\n" + "=" * 70)
    print(" Experiment 4 Completed Successfully.")
    print("=" * 70)


if __name__ == "__main__":
    main()
