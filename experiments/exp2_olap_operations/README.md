# Experiment 2: OLAP Operations & Multidimensional Aggregation

## 1. Aim
To execute Online Analytical Processing (OLAP) operations including Slice, Dice, Roll-up, Drill-down, and Pareto analysis over a multidimensional sales dataset.

## 2. Theory
OLAP provides swift, consistent, interactive access to a wide variety of possible views of information that has been transformed from raw data to reflect the real dimensionality of the enterprise.

### Core OLAP Operations:
1. **Roll-up (Consolidation)**: Aggregates data along a dimension hierarchy (e.g., aggregating daily transactions into weekly, monthly, or quarterly summaries).
2. **Drill-down**: Reverses roll-up, revealing lower-level detail along a hierarchy.
3. **Slice**: Performs a selection on one dimension of the cube, yielding a subcube.
4. **Dice**: Defines a subcube by performing a selection across two or more dimensions.
5. **Pivot / Rotate**: Rotates data axes in view to provide an alternative presentation.
6. **Pareto Analysis**: Evaluates the cumulative contribution of items (80/20 rule) to discover disproportionately influential drivers of total revenue.

## 3. How to Run
```powershell
python experiments/exp2_olap_operations/run_experiment.py
```
