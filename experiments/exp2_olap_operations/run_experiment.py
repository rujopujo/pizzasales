"""Experiment 2: OLAP Operations & Multidimensional Aggregation.

Demonstrates:
- Slice: Filtering on a single dimension (e.g., Weekend sales)
- Dice: Filtering on multiple dimensions simultaneously (e.g., Supreme pizzas during Dinner rush)
- Roll-up: Aggregating facts up along the Time hierarchy (Day -> Week -> Month -> Quarter)
- Drill-down: Decomposing high-level measures into dimensional grain
- Pareto Analysis (80/20 law on revenue contribution)
"""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.warehouse import joined_sales, roll_up, slice_dice


def main():
    print("=" * 70)
    print(" DWM LAB EXPERIMENT 2: OLAP OPERATIONS (ROLL-UP, SLICE & DICE)")
    print("=" * 70)

    sales = joined_sales()
    print(f"\n[Dataset] Total Joined Warehouse Records: {len(sales):,}")

    # 1. OLAP Slice: Filtering Weekend-only transactions
    print("\n[Operation 1] SLICE: Filtering on Time Dimension (Weekend only)...")
    weekend_slice = slice_dice(sales, weekend_only=True)
    print(f"  -> Rows after Slice: {len(weekend_slice):,} of {len(sales):,}")
    print(f"  -> Weekend Revenue: ${weekend_slice['total_price'].sum():,.2f}")
    print(f"  -> Days Present: {sorted(weekend_slice['day_of_week'].unique())}")

    # 2. OLAP Dice: Multi-dimensional Subcube Selection
    print("\n[Operation 2] DICE: Categories = ['Classic', 'Supreme'] AND Peak Hours = True...")
    diced = slice_dice(
        sales,
        categories=["Classic", "Supreme"],
        peak_only=True,
    )
    print(f"  -> Rows after Dice: {len(diced):,}")
    print(f"  -> Diced Revenue: ${diced['total_price'].sum():,.2f}")
    print(f"  -> Categories: {sorted(diced['pizza_category'].unique())}")
    print(f"  -> Peak Periods: {sorted(diced['peak_period'].unique())}")

    # 3. OLAP Roll-Up: Time Hierarchy Aggregations
    print("\n[Operation 3] ROLL-UP: Multi-grain Time Hierarchy Aggregation...")
    for grain in ["Quarter", "Month", "Week"]:
        cube = roll_up(sales, grain=grain, dimensions=["pizza_category"])
        print(f"\n  • Grain: {grain} by Pizza Category (Top 4 rows):")
        print(cube[["period", "pizza_category", "revenue", "pizzas_sold", "orders", "margin_pct"]].head(4).to_string(index=False))

    # 4. Pareto Analysis (80/20 rule)
    print("\n[Operation 4] PARETO ANALYSIS: 80/20 Law on Item Revenue...")
    ranked = sales.groupby("pizza_name")["total_price"].sum().sort_values(ascending=False)
    cumulative_pct = (ranked.cumsum() / ranked.sum()) * 100
    pareto_df = ranked.to_frame(name="Revenue").assign(Cumulative_Pct=cumulative_pct.round(1))
    print(pareto_df.head(6).to_string())

    top_80_items = pareto_df[pareto_df["Cumulative_Pct"] <= 80]
    print(f"\n  -> Items generating up to ~80% of revenue: {len(top_80_items)} items out of {len(ranked)} total items.")

    print("\n" + "=" * 70)
    print(" Experiment 2 Completed Successfully.")
    print("=" * 70)


if __name__ == "__main__":
    main()
