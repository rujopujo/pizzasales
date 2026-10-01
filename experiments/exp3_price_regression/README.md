# Experiment 3: Predictive Analytics - Regression Modeling

## 1. Aim
To construct, train, and evaluate linear and non-linear regression models (OLS, Ridge, Random Forest) for price estimation and examine goodness-of-fit metrics.

## 2. Theory
Regression in data mining is a supervised learning technique that models the relationship between a continuous dependent numerical target ($y$) and one or more independent predictor features ($X$).

### Mathematical Formulations:
- **Ordinary Least Squares (OLS) Linear Regression**:
  $$\min_w ||Xw - y||_2^2$$
- **Ridge Regression (L2 Regularization)**:
  $$\min_w ||Xw - y||_2^2 + \alpha ||w||_2^2$$
- **Random Forest Regressor**:
  An ensemble meta-estimator that fits multiple classifying decision trees on sub-samples of the dataset and uses averaging to improve predictive accuracy and control over-fitting.

### Evaluation Metrics:
- **$R^2$ Score**: Proportion of variance in target explained by input predictors.
- **Adjusted $R^2$**: Penalizes addition of non-informative variables:
  $$1 - (1 - R^2)\frac{n-1}{n-p-1}$$
- **Mean Absolute Error (MAE)**: Average magnitude of absolute prediction errors.
- **Root Mean Squared Error (RMSE)**: Penalizes large outlier deviations heavily.
- **Mean Absolute Percentage Error (MAPE)**: Relative percentage error.

## 3. How to Run
```powershell
python experiments/exp3_price_regression/run_experiment.py
```
