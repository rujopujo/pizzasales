# Data Warehousing & Mining (DWM) Laboratory Manual

This manual provides the theoretical background, algorithms, design specifications, and experimental procedures for all four laboratory practicals in the **Pizza Modern Data Warehouse & Mining** project.

---

## Table of Contents
1. [Experiment 1: Star Schema & Multidimensional Modeling](#experiment-1)
2. [Experiment 2: OLAP Operations & Multidimensional Aggregation](#experiment-2)
3. [Experiment 3: Price Regression & Predictive Analytics](#experiment-3)
4. [Experiment 4: Decision Tree Classification & Feature Selection](#experiment-4)

---

<a name="experiment-1"></a>
## Experiment 1: Star Schema & Multidimensional Modeling

### Aim:
To design, implement, and validate a multidimensional Star Schema database for transactional retail data, mapping dimension hierarchies and establishing surrogate keys.

### Theory:
Data warehouse architectures rely on dimensional modeling techniques to optimize complex analytical queries:
- **Fact Table**: The center of the star containing additive/semi-additive numerical measures (`quantity`, `unit_price`, `total_price`, `margin_rate`) and foreign keys referencing dimensions.
- **Dimension Tables**: Contextual entities (`Dim_Pizza`, `Dim_Time`, `Dim_Date`) containing descriptive attributes used to constrain and group queries.
- **Surrogate Keys**: System-generated integer primary keys independent of natural business keys, providing isolation from source system changes and faster join execution.

### Verification Criteria:
1. Every fact record references valid primary keys in all three dimension tables (referential integrity).
2. Additive measures satisfy $total\_price = quantity \times unit\_price$.
3. Time and Date tables contain proper hierarchy levels (e.g., hour $\rightarrow$ peak period; date $\rightarrow$ month $\rightarrow$ quarter).

---

<a name="experiment-2"></a>
## Experiment 2: OLAP Operations & Multidimensional Aggregation

### Aim:
To implement and execute Online Analytical Processing (OLAP) operations including Roll-up, Drill-down, Slice, Dice, and Pareto analysis over a multidimensional sales dataset.

### Theory:
OLAP facilitates fast multidimensional analysis:
- **Slice**: Performs a selection on a single dimension of the data cube (e.g., `is_weekend == True`).
- **Dice**: Performs a selection across multiple dimensions simultaneously (e.g., `category in ['Classic', 'Supreme']` and `peak_period == 'Dinner'`).
- **Roll-up**: Aggregates factual data up the dimensional hierarchy (from Day $\rightarrow$ Week $\rightarrow$ Month $\rightarrow$ Quarter).
- **Drill-down**: Disaggregates higher-level summaries down to granular attributes.
- **Pareto Principle (80/20 Rule)**: Assesses cumulative revenue distribution to distinguish the vital few from the trivial many.

---

<a name="experiment-3"></a>
## Experiment 3: Price Regression & Predictive Analytics

### Aim:
To design, train, and evaluate linear and non-linear regression models for transaction price estimation, and evaluate goodness-of-fit through diagnostic plots and error metrics.

### Models Implemented:
1. **Ordinary Least Squares (OLS)**: Minimizes residual sum of squares without regularization penalty.
2. **Ridge Regression (L2)**: Adds penalty $\alpha ||w||_2^2$ to stabilize coefficient estimates under multicollinearity.
3. **Random Forest Regressor**: Non-linear ensemble model averaging predictions over 120 decision tree estimators.

### Evaluation Metrics:
- **$R^2$ & Adjusted $R^2$**: Goodness of fit and explained variance.
- **Mean Absolute Error (MAE)**: Average absolute residual.
- **Root Mean Squared Error (RMSE)**: Penalizes larger outliers heavily.
- **MAPE (%)**: Mean Absolute Percentage Error.

---

<a name="experiment-4"></a>
## Experiment 4: Decision Tree Classification & Feature Selection

### Aim:
To analyze attribute relevance using Mutual Information and Random Forest feature importance, train a Decision Tree Classifier to categorize transaction orders into spend tiers, and evaluate performance using confusion matrices and ROC curves.

### Methodology:
1. **Target Discretization**:
   - `Budget`: Order total $< \$20$
   - `Standard`: Order total between $\$20$ and $\$50$
   - `Premium`: Order total $> \$50$
2. **Feature Relevance Analysis**:
   - Computes Mutual Information scores: $I(X; Y) = \sum_{x, y} p(x, y) \log \frac{p(x, y)}{p(x)p(y)}$
   - Evaluates Random Forest feature importance based on mean impurity decrease.
3. **Decision Tree Induction**:
   - CART algorithm with tunable max depth and minimum samples to split.
   - Evaluated via Gini Impurity and Entropy (Information Gain).
4. **Model Validation**:
   - Stratified $75\% / 25\%$ train/test split.
   - Per-class Precision, Recall, F1-Score, Normalized Confusion Matrix, and One-vs-Rest ROC/AUC curves.
