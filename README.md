# Pizza Modern Data Warehouse & Predictive Intelligence

A modern decision support platform and Data Warehousing & Mining (DWM) lab suite for pizza sales analytics. It creates a 2025 synthetic sales dataset, builds a Star Schema data warehouse, supports OLAP multidimensional analysis (Slice, Dice, Roll-up, Drill-down), and trains regression and decision tree models for interactive pricing and tier prediction.

---

## Folder Organization

The repository is organized into modular packages, practical lab experiments, automated scripts, and documentation:

```
├── app.py                           # Central Streamlit decision support dashboard
├── config.py                        # Root configuration backward-compatibility shim
├── requirements.txt                 # Project dependencies
├── README.md                        # Master repository documentation
│
├── data/                            # Warehouse raw and extracted datasets
│   └── pizza_sales.csv              # 3,000 synthetic 2025 sales transaction line items
│
├── src/                             # Core modular application packages
│   ├── config/                      # UI constants, color palettes, and menu settings
│   │   ├── __init__.py
│   │   └── settings.py
│   ├── warehouse/                   # Star schema creation, ETL, and OLAP query engine
│   │   ├── __init__.py
│   │   └── warehouse_engine.py
│   ├── mining/                      # Machine learning regression & classification engines
│   │   ├── __init__.py
│   │   ├── classification_engine.py
│   │   └── regression_engine.py
│   ├── analytics/                   # Executive KPIs, waterfall, heatmaps, and Pareto analysis
│   │   ├── __init__.py
│   │   └── analytics.py
│   └── ui/                          # Streamlit styling, CSS injection, and glass cards
│       ├── __init__.py
│       └── components.py
│
├── experiments/                     # Academic DWM practical lab experiments
│   ├── README.md                    # Experiments guide & index
│   ├── exp1_star_schema/            # Experiment 1: Star Schema & Dimension Tables
│   │   ├── README.md
│   │   └── run_experiment.py
│   ├── exp2_olap_operations/        # Experiment 2: Roll-up, Drill-down, Slice & Dice
│   │   ├── README.md
│   │   └── run_experiment.py
│   ├── exp3_price_regression/       # Experiment 3: Predictive Regression Modeling
│   │   ├── README.md
│   │   └── run_experiment.py
│   └── exp4_decision_tree_classification/ # Experiment 4: Decision Tree & Feature Selection
│       ├── README.md
│       └── run_experiment.py
│
├── docs/                            # In-depth architectural and laboratory guides
│   ├── ARCHITECTURE.md              # Technical design and data flow architecture
│   ├── DATA_DICTIONARY.md           # Attribute data types, grain, and key constraints
│   └── DWM_LAB_MANUAL.md            # University-standard practical laboratory manual
│
├── scripts/                         # Automation & maintenance utility scripts
│   ├── setup.ps1                    # One-click virtual environment and dependency setup
│   ├── run_app.ps1                  # Launch Streamlit app
│   ├── run_tests.ps1                # Run automated smoke test suite
│   └── generate_dataset.py          # Standalone dataset generator
│
└── tests/                           # Unit and smoke test suite
    └── test_smoke.py                # End-to-end warehouse and inference checks
```

---

## Quick Start

### 1. Requirements
- Python 3.10 or newer
- Windows PowerShell, macOS Terminal, or Linux shell

### 2. Automated Setup (Windows PowerShell)
```powershell
.\scripts\setup.ps1
```

### 3. Manual Setup

#### Windows PowerShell
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
streamlit run app.py
```

#### macOS / Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
streamlit run app.py
```

Open `http://localhost:8501` in your browser.

---

## Running the Academic Lab Experiments

Each experiment can be run independently from the command line:

```powershell
# Experiment 1: Star Schema Data Warehouse Modeling
python experiments/exp1_star_schema/run_experiment.py

# Experiment 2: OLAP Multidimensional Operations (Roll-up, Slice, Dice)
python experiments/exp2_olap_operations/run_experiment.py

# Experiment 3: Price Regression Modeling & Diagnostics
python experiments/exp3_price_regression/run_experiment.py

# Experiment 4: Decision Tree Classification & Feature Relevance
python experiments/exp4_decision_tree_classification/run_experiment.py
```

---

## Smoke Tests

Run smoke checks across the warehouse and machine learning models:
```powershell
python -m unittest discover -s tests -v
```
or via the script:
```powershell
.\scripts\run_tests.ps1
```

---

## Features & Modules

1. **Executive Overview**: High-level KPIs (Gross Revenue, Total Pizzas, Unique Orders, Average Order Value, Average Margin %), Category Waterfall chart, and 24-hour weekday heatmaps.
2. **OLAP & Data Warehouse**: Interactive star schema inspector (`Fact_Sales`, `Dim_Pizza`, `Dim_Time`, `Dim_Date`), roll-ups across multiple time hierarchies (Day, Week, Month, Quarter), slicing/dicing filters, and Pareto 80/20 revenue analysis.
3. **Price Regression Lab**: Benchmark comparison between OLS Linear Regression, Ridge Regression, and Random Forest Regressor ($R^2$, Adj $R^2$, MAE, RMSE, MAPE), residual plots, Q-Q plots, and an interactive basket calculator with size uplift and surge multiplier.
4. **Tree Classification & Mining**: Mutual Information and Random Forest feature relevance ranking, Decision Tree classification (CART with Gini/Entropy), normalized confusion matrix, One-vs-Rest ROC/AUC curves, and a live order tier classifier (Budget, Standard, Premium).
