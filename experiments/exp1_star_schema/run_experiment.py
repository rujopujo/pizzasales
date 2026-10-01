"""Experiment 1: Star Schema & Multidimensional Data Modeling.

Demonstrates:
- Loading raw transaction logs
- Constructing Dimension Tables (Dim_Pizza, Dim_Time, Dim_Date) with surrogate keys
- Constructing Fact Table (Fact_Sales) at transaction line item grain
- Validating referential integrity and key constraints
"""

import sys
from pathlib import Path

# Ensure project root is in sys.path
PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.warehouse import build_star_schema, joined_sales, load_sales_data


def main():
    print("=" * 70)
    print(" DWM LAB EXPERIMENT 1: STAR SCHEMA & DATA WAREHOUSE MODELING")
    print("=" * 70)

    # 1. Load Source Data
    print("\n[Step 1] Loading Raw Sales Data...")
    raw_sales = load_sales_data()
    print(f"  -> Total Raw Records: {len(raw_sales):,} rows")
    print(f"  -> Columns: {', '.join(raw_sales.columns)}")
    print("\n  Sample Raw Record:")
    print(raw_sales.head(2).to_string(index=False))

    # 2. Build Star Schema
    print("\n[Step 2] Constructing Star Schema Dimension and Fact Tables...")
    schema = build_star_schema()

    for table_name, df in schema.items():
        print(f"\n  • Table: {table_name}")
        print(f"    - Dimensions / Rows: {len(df):,} records, {df.shape[1]} attributes")
        print(f"    - Attributes: {', '.join(df.columns)}")
        print("    - Preview (top 2 rows):")
        print(df.head(2).to_string(index=False))

    # 3. Referential Integrity Check
    print("\n[Step 3] Referential Integrity & Grain Validation...")
    fact = schema["Fact_Sales"]
    dim_pizza = schema["Dim_Pizza"]
    dim_time = schema["Dim_Time"]
    dim_date = schema["Dim_Date"]

    pizza_keys_valid = fact["pizza_key"].isin(dim_pizza["pizza_key"]).all()
    time_keys_valid = fact["time_key"].isin(dim_time["time_key"]).all()
    date_keys_valid = fact["date_key"].isin(dim_date["date_key"]).all()

    print(f"  -> Foreign Key Check (fact.pizza_key in dim_pizza): {pizza_keys_valid}")
    print(f"  -> Foreign Key Check (fact.time_key in dim_time):   {time_keys_valid}")
    print(f"  -> Foreign Key Check (fact.date_key in dim_date):   {date_keys_valid}")

    total_revenue = (fact["quantity"] * fact["unit_price"]).sum()
    print(f"  -> Fact Table Total Revenue: ${total_revenue:,.2f}")
    print(f"  -> Average Margin Rate: {fact['margin_rate'].mean() * 100:.2f}%")

    print("\n" + "=" * 70)
    print(" Experiment 1 Completed Successfully.")
    print("=" * 70)


if __name__ == "__main__":
    main()
