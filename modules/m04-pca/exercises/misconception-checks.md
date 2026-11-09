# Misconception checks — PCA (formative, in lecture)

Use these with show of hands or a polling tool. Students answer individually, discuss in pairs for one minute, then re-vote. Each item names the misconception it targets. Answers and discussion notes are kept with the instructor material.

## Part I (first PCA week)

**MC1 — Centring.** A student computes `U, s, Vt = np.linalg.svd(X)` on raw (uncentred) data and reports `Vt[0]` as PC1. For data whose variables all have large positive means, `Vt[0]` will most likely point:
A. along the direction of largest variance · B. along the mean vector · C. in a random direction · D. along the variable with the smallest variance

**MC2 — Units.** Variables: annual income (Thai baht) and age (years). Covariance PCA puts 99.9% of the variance on PC1. True or false: *"Income and age are almost perfectly redundant."* Explain your answer in one sentence.

**MC3 — Signs.** Two software packages return PC1 coefficients $(0.6, 0.8)$ and $(-0.6, -0.8)$ for the same data. Which statement is correct?
A. One package has a bug · B. Both are correct; only the relative signs within the component are interpretable · C. The data must contain outliers · D. The eigenvalues must also differ in sign

**MC4 — Uncorrelated vs independent.** True or false: *"Because principal component scores are uncorrelated, they are statistically independent."* Give a condition under which the statement *is* true.

## Part II (second PCA week)

**MC5 — Choosing k with the test set.** A team tries $k = 1, \dots, 30$ and reports the test accuracy of the best $k$. What is wrong, and what should they do instead?

**MC6 — Variance and prediction.** True or false: *"The first principal component is always the most useful single feature for predicting the class."* Sketch a two-variable counterexample.

**MC7 — Leakage size.** Rank from largest to smallest the optimistic bias usually caused by fitting each step on all rows before cross-validation: (i) `StandardScaler`, (ii) `PCA`, (iii) `SelectKBest(f_classif)`, (iv) `SMOTE`. Explain what drives the ranking. Then explain why *all four* must still be fitted inside the folds.

**MC8 — Pictures.** True or false: *"If the classes overlap in the PC1–PC2 scatter plot, no classifier can separate them well."* Support your answer with a number from Lab 4B.
