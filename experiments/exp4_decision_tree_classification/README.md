# Experiment 4: Supervised Learning - Decision Tree Classification

## 1. Aim
To apply feature relevance mining and decision tree induction algorithms (CART/ID3 using Gini and Information Gain) for order categorization, and assess classification accuracy with ROC curves and confusion matrices.

## 2. Theory
Classification is a two-step process in data mining:
1. **Model Construction**: Analyzing training data described by attributes to produce a classification mapping.
2. **Model Usage**: Estimating the accuracy of the model on unseen test samples and predicting class labels for new instances.

### Splitting Criteria:
- **Gini Impurity**:
  $$\text{Gini}(D) = 1 - \sum_{i=1}^m p_i^2$$
- **Entropy (Information Gain)**:
  $$\text{Info}(D) = -\sum_{i=1}^m p_i \log_2(p_i)$$

### Attribute Relevance Analysis:
Before classification, attribute relevance ranking reduces feature space dimensionality by identifying attributes with high correlation to the target class:
- **Mutual Information**: Quantifies non-linear dependency between variables.
- **Random Forest Feature Importance**: Gini decrease aggregated over an ensemble of decision trees.

### Evaluation Metrics:
- **Precision**: $\frac{TP}{TP + FP}$
- **Recall**: $\frac{TP}{TP + FN}$
- **F1-Score**: Harmonic mean of Precision and Recall.
- **Receiver Operating Characteristic (ROC)**: True Positive Rate vs False Positive Rate across all probability thresholds.

## 3. How to Run
```powershell
python experiments/exp4_decision_tree_classification/run_experiment.py
```
