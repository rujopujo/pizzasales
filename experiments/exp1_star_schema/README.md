# Experiment 1: Star Schema & Multidimensional Data Modeling

## 1. Aim
To design, implement, and validate a multidimensional Star Schema data warehouse for a retail sales transaction domain.

## 2. Theory
A **Data Warehouse** is a subject-oriented, integrated, time-variant, and non-volatile collection of data in support of management's decision-making process.

### Star Schema Architecture
In a Star Schema:
- **Fact Table** sits at the center containing numerical measurements (metrics) and foreign keys referencing dimension tables.
- **Dimension Tables** surround the fact table and contain contextual descriptive attributes used for slicing, dicing, and grouping.

### Schema Design for Pizza Sales
- **Fact Table: `Fact_Sales`**
  - Primary Key: `sale_id` (surrogate key)
  - Foreign Keys: `date_key`, `time_key`, `pizza_key`, `order_id`
  - Measures: `quantity`, `unit_price`, `total_price`, `margin_rate`
- **Dimension 1: `Dim_Pizza`**
  - Primary Key: `pizza_key`
  - Attributes: `pizza_name`, `pizza_category`, `pizza_size`
- **Dimension 2: `Dim_Time`**
  - Primary Key: `time_key`
  - Attributes: `order_time`, `hour`, `peak_period` (Lunch, Dinner, Off-Peak)
- **Dimension 3: `Dim_Date`**
  - Primary Key: `date_key`
  - Attributes: `date`, `day_of_week`, `is_weekend`, `month_name`, `quarter`

## 3. How to Run
```powershell
python experiments/exp1_star_schema/run_experiment.py
```
