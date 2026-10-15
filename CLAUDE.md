# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands for Development

**Environment Setup:**
- Windows PowerShell: `.\scripts\setup.ps1` (creates venv, activates, installs deps)
- Manual setup: `python -m venv .venv` → `.\.venv\Scripts\Activate.ps1` → `python -m pip install -r requirements.txt`
- Launch app: `streamlit run app.py` or `.\scripts\run_app.ps1`

**Testing:**
- Run all smoke tests: `python -m unittest discover -s tests -v` or `.\scripts\run_tests.ps1`
- Run single test: `python -m unittest tests.test_smoke.TestSmoke.test_<method_name>`

**Experiments (run independently):**
- Exp 1 (Star Schema): `python experiments/exp1_star_schema/run_experiment.py`
- Exp 2 (OLAP Operations): `python experiments/exp2_olap_operations/run_experiment.py`
- Exp 3 (Price Regression): `python experiments/exp3_price_regression/run_experiment.py`
- Exp 4 (Decision Tree): `python experiments/exp4_decision_tree_classification/run_experiment.py`

**Data Regeneration:**
- Generate fresh dataset: `python scripts\generate_dataset.py`

## Code Architecture & Structure

**Core Modules (src/):**
- **warehouse/**: Star schema ETL and OLAP operations (`joined_sales()`, `build_star_schema()`, `slice_dice()`, `roll_up()`)
- **mining/**: ML regression (`train_regressors()`) and classification (`train_decision_tree()`) engines
- **analytics/**: KPI calculations, waterfall charts, heatmaps, Pareto analysis
- **ui/**: Streamlit styling, CSS injection, metric cards, section dividers
- **config/**: UI constants (palettes, categories, sizes, text labels)

**Data Flow:**
1. Source data loaded from `data/pizza_sales.csv` (auto-generated if missing)
2. Warehouse module builds star schema: Fact_Sales + Dim_Pizza/Dim_Time/Dim_Date
3. OLAP operations slice/dice/roll_up the joined fact table
4. ML modules train on filtered/full dataset for regression/price prediction and classification/tier prediction
5. Streamlit app (`app.py`) orchestrates tabs: Executive Overview, OLAP DW, Regression Lab, Classification Lab

**Key Patterns:**
- Heavy use of `@st.cache_data` and `@lru_cache` for performance
- Config-driven UI constants (colors, categories, sizes in src/config/)
- Experiments mirror core functionality with isolated implementations
- All data processing returns copies to prevent mutation of cached sources

**Important Files:**
- `app.py`: Main Streamlit entry point with tabbed interface
- `src/warehouse/warehouse_engine.py`: Core data warehouse and OLAP logic
- `src/mining/*_engine.py`: Regression and classification training/prediction
- `src/analytics.py`: KPI and visualization functions
- `docs/ARCHITECTURE.md`: Detailed technical design and data flow
- `docs/DWM_LAB_MANUAL.md`: University lab manual with experiment procedures