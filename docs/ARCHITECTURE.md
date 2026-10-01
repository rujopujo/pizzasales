# System Architecture & Technical Design

This document details the architecture, design patterns, and package layout of the **Pizza Modern Data Warehouse (MDW) & Predictive Intelligence Platform**.

---

## 1. Architectural Overview

The platform unites modern data warehousing, OLAP multi-dimensional querying, machine learning regression, and decision tree mining into a single streamlined workspace.

```
                          ┌───────────────────────────┐
                          │    Raw Transaction CSV    │
                          │   (data/pizza_sales.csv)  │
                          └─────────────┬─────────────┘
                                        │
                                        ▼
                          ┌───────────────────────────┐
                          │    Warehouse ETL Engine   │
                          │      (src/warehouse)      │
                          └──────┬─────────────┬──────┘
                                 │             │
                ┌────────────────┴────┐   ┌────┴────────────────┐
                ▼                     ▼   ▼                     ▼
      ┌──────────────────┐    ┌──────────────────┐    ┌──────────────────┐
      │    Dim Tables    │    │    Fact Table    │    │  Joined Star DB  │
      │ Pizza, Time, Date│    │    Fact_Sales    │    │  In-Memory Cube  │
      └─────────┬────────┘    └────────┬─────────┘    └────────┬─────────┘
                │                      │                       │
                └───────────────┬──────┴───────────────────────┘
                                │
        ┌───────────────────────┼───────────────────────┐
        ▼                       ▼                       ▼
┌───────────────┐       ┌───────────────┐       ┌───────────────┐
│ OLAP Engine   │       │ Mining Engine │       │ Visual Engine │
│ Slice / Dice  │       │ Regress / Tree│       │ Plotly Charts │
│ (src/warehouse│       │ (src/mining)  │       │(src/analytics)│
└───────┬───────┘       └───────┬───────┘       └───────┬───────┘
        │                       │                       │
        └───────────────────────┼───────────────────────┘
                                │
                                ▼
                    ┌───────────────────────┐
                    │  Streamlit Dashboard  │
                    │       (app.py)        │
                    └───────────────────────┘
```

---

## 2. Directory Structure

```
├── .streamlit/
│   └── config.toml                  # Streamlit dark theme settings
├── config.py                        # Root backward-compatibility configuration shim
├── app.py                           # Multi-tab Streamlit dashboard application
├── requirements.txt                 # Python package dependencies
├── README.md                        # Master project documentation
│
├── data/
│   └── pizza_sales.csv              # Synthetic 2025 sales transaction dataset
│
├── src/                             # Core modular package
│   ├── __init__.py                  # Master package init
│   ├── config/                      # Application constants and colors
│   │   ├── __init__.py
│   │   └── settings.py
│   ├── warehouse/                   # Data warehousing, Star Schema, and OLAP
│   │   ├── __init__.py
│   │   └── warehouse_engine.py
│   ├── mining/                      # Machine learning regression & classification
│   │   ├── __init__.py
│   │   ├── classification_engine.py
│   │   └── regression_engine.py
│   ├── analytics/                   # KPIs, waterfall charts, heatmaps, Pareto
│   │   ├── __init__.py
│   │   └── analytics.py
│   └── ui/                          # UI styles, CSS injection, metric cards
│       ├── __init__.py
│       └── components.py
│
├── experiments/                     # Academic practical experiments
│   ├── README.md                    # Experiment catalog & execution guide
│   ├── exp1_star_schema/            # Experiment 1: Star Schema modeling
│   │   ├── README.md
│   │   └── run_experiment.py
│   ├── exp2_olap_operations/        # Experiment 2: Roll-up, Slice, Dice
│   │   ├── README.md
│   │   └── run_experiment.py
│   ├── exp3_price_regression/       # Experiment 3: Price regression & inference
│   │   ├── README.md
│   │   └── run_experiment.py
│   └── exp4_decision_tree_classification/ # Experiment 4: Decision tree mining
│       ├── README.md
│       └── run_experiment.py
│
├── docs/                            # Comprehensive documentation
│   ├── ARCHITECTURE.md              # Technical architecture (this file)
│   ├── DATA_DICTIONARY.md           # Schema definitions and data dictionary
│   └── DWM_LAB_MANUAL.md            # University-level DWM Lab Manual
│
├── scripts/                         # Automation & run scripts
│   ├── setup.ps1                    # Environment creation & package install
│   ├── run_app.ps1                  # Launch Streamlit app
│   ├── run_tests.ps1                # Run automated smoke tests
│   └── generate_dataset.py          # Data generation utility
│
└── tests/
    └── test_smoke.py                # End-to-end regression & warehouse tests
```

---

## 3. Modular Package Breakdown

### `src.warehouse`
- **Synthetic Data Generation**: Reproduces 3,000 transactions across 2025 with realistic hourly distributions, Friday/Saturday/Sunday uplifts, and lunch/dinner rush hours.
- **Star Schema Construction**: Normalizes flat transaction streams into dimension tables (`Dim_Pizza`, `Dim_Time`, `Dim_Date`) with integer surrogate keys.
- **OLAP Engine**: Implements slicing, dicing, and roll-ups along customizable grains (Day, Week, Month, Quarter) and arbitrary dimensional combinations.

### `src.mining`
- **Regression Engine**:
  - Scikit-learn preprocessing pipeline with one-hot encoding for categorical variables (`pizza_size`, `pizza_category`) and pass-through numeric features.
  - Multi-model evaluation: Ordinary Least Squares (OLS), Ridge Regression, and Random Forest Regressor.
  - Diagnostic charts: Residual plots and Normal Q-Q probability plots.
- **Classification Engine**:
  - Mutual Information and Random Forest Gini feature relevance ranking.
  - Decision Tree induction with tunable maximum depth, minimum sample splits, and Gini / Entropy criteria.
  - One-vs-Rest ROC curve and normalized Confusion Matrix generation.

### `src.analytics`
- Aggregates high-level executive KPIs (Gross Revenue, Total Pizzas, Unique Orders, Average Order Value, Average Margin %).
- Interactive Plotly waterfall, weekday-hour heatmaps, and Pareto cumulative revenue curves.

### `src.ui`
- Consistent modern dark-mode aesthetic with custom glassmorphic cards and typography.
