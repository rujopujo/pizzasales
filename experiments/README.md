# DWM Lab Practicals & Experiments

This directory contains standalone, reproducible practical experiments for the **Data Warehousing and Data Mining (DWM)** curriculum. Each experiment can be executed independently from the command line or inspected in detail.

---

## Experiment Index

| Experiment | Title | Core Concepts | Script |
|---|---|---|---|
| **Exp 1** | [Star Schema & Multidimensional Modeling](./exp1_star_schema/) | Fact Table, Dimension Tables, Surrogate Keys, Data Grain, Normalization vs Denormalization | `python experiments/exp1_star_schema/run_experiment.py` |
| **Exp 2** | [OLAP Operations & Multidimensional Aggregation](./exp2_olap_operations/) | Roll-up, Drill-down, Slice, Dice, Time Hierarchy, Pareto Analysis | `python experiments/exp2_olap_operations/run_experiment.py` |
| **Exp 3** | [Predictive Analytics: Regression Modeling](./exp3_price_regression/) | OLS Linear Regression, Ridge, Random Forest Regressor, $R^2$, RMSE, MAE, Residual Diagnostics | `python experiments/exp3_price_regression/run_experiment.py` |
| **Exp 4** | [Supervised Learning: Decision Tree Classification](./exp4_decision_tree_classification/) | Information Gain, Gini Impurity, Decision Trees, Mutual Information, ROC/AUC, Confusion Matrix | `python experiments/exp4_decision_tree_classification/run_experiment.py` |

---

## How to Run the Experiments

Make sure dependencies are installed:
```powershell
python -m pip install -r requirements.txt
```

Run any experiment from the repository root:
```powershell
# Experiment 1: Star Schema & Data Warehouse Modeling
python experiments/exp1_star_schema/run_experiment.py

# Experiment 2: OLAP Operations (Roll-up, Slice, Dice)
python experiments/exp2_olap_operations/run_experiment.py

# Experiment 3: Price Regression Lab
python experiments/exp3_price_regression/run_experiment.py

# Experiment 4: Decision Tree Classification & Attribute Relevance
python experiments/exp4_decision_tree_classification/run_experiment.py
```
