"""Utility script to regenerate the synthetic pizza sales dataset."""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.warehouse.warehouse_engine import DATA_FILE, generate_sales_data


def main():
    print(f"Generating 3,000 synthetic pizza sales transaction rows...")
    df = generate_sales_data(n_rows=3000, seed=42)
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(DATA_FILE, index=False)
    print(f"Successfully generated and wrote dataset to: {DATA_FILE}")
    print(f"Shape: {df.shape[0]} rows x {df.shape[1]} columns")


if __name__ == "__main__":
    main()
