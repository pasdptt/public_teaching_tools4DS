# Problem set — PCA (weeks 5–6)

**Independent work:** P1–P4 after week 5 (about 2 h); P5–P8 after week 6 (about 2 h). Hand problems are done on paper first; check them with code afterwards. Answer keys are released after the submission deadline.

## Week 5 (hand and derivation)

**P1 — Full hand computation (objective PCA-O2).** Five observations:

| obs | $x_1$ | $x_2$ |
|---|---|---|
| 1 | 6 | 0 |
| 2 | 6 | 2 |
| 3 | 5 | 2 |
| 4 | 6 | 6 |
| 5 | 2 | 0 |

(a) Compute $\bar x$, the centred data and $S$ (divisor $n-1$).
(b) Find the eigenvalues and unit eigenvectors of $S$.
(c) Compute the five PC1 scores and verify that their variance equals $\lambda_1$.
(d) Give the explained-variance ratio of PC1.
(e) Reconstruct observation 4 from PC1 only, in the original units, and give its squared residual. Check that the residual sum of squares divided by $n-1$ equals $\lambda_2$.
(f) Compute the correlation matrix $R$ and its first eigenvector. Does correlation PCA give the same PC1 *direction* as covariance PCA? Explain why or why not.

**P2 — Derivation (PCA-O1).** Starting from $\max_v v^\top S v$ subject to $v^\top v = 1$ and $v^\top v_1 = 0$, show that the solution is the eigenvector with the second-largest eigenvalue. State clearly where you use the symmetry of $S$.

**P3 — Properties (PCA-O1, PCA-O3).**
(a) Show that $\operatorname{Var}(X_c v)=v^\top S v$ and that the scores $Z=X_cV$ have covariance matrix $\Lambda$.
(b) Show that $\operatorname{tr}(S)=\sum_j\lambda_j$.
(c) Using $X_c = U\Sigma V^\top$, derive $\lambda_j=\sigma_j^2/(n-1)$ and $Z=U\Sigma$.

**P4 — Indeterminacy (PCA-O4).**
(a) For $S=\operatorname{diag}(4,1,1)$, describe *all* valid second principal component directions. What does this imply for interpreting PC2 and PC3?
(b) For $S=\begin{pmatrix}4&-2\\-2&1\end{pmatrix}$, find the eigenvalues. What does $\lambda_2$ tell you about the two variables? Give an example of data that would produce this $S$.

## Week 6 (practice; use Colab)

**P5 — Choosing k on another dataset (PCA-O5).** Run your `parallel_analysis` from Lab 06 on standardised Iris (`tsds.data.load("iris")`, 4 variables, $B=200$, course seed). Report the eigenvalues, the thresholds, and the k chosen by parallel analysis, by the eigenvalue-above-one rule and by 80% cumulative variance. Comment on any disagreement.

**P6 — Baseline first (PCA-O6).** On Wine with the course 5-fold split:
(a) Compare the majority class, standardise + logistic regression, and standardise + PCA(2) + logistic regression.
(b) Run nested CV over $k\in\{1,2,3,5,8,13\}$.
(c) Repeat (a) with PCA(2) **without** standardising.
Report mean ± sd and explain what each comparison shows.

**P7 — Compositional data (PCA-O8, conceptual).** A municipality's revenue is split into three shares that always sum to 1.
(a) Explain why the shares must be negatively correlated even if the underlying amounts are independent.
(b) State the centred log-ratio transform and why PCA is applied after it (Aitchison 1983).
(c) Name one practical problem caused by zero shares.

**P8 — Critique a claim (PCA-O4, PCA-O7).** A report states: *"PCA of the 13 wine measurements shows that PC1 explains 99.8% of the variance, so wine chemistry is essentially one-dimensional, and the PC1 scatter plot shows the cultivars are hard to separate."* Write a 150-word critique that identifies **every** methodological error, and say what analysis should have been done instead.
