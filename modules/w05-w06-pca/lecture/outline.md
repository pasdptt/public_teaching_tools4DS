# Lecture outline — Principal Component Analysis (weeks 5–6)

Every number in this outline was computed by code and is identical under both CI environments: pinned local and Colab-proxy (see [`../EXECUTION-REPORT.md`](../EXECUTION-REPORT.md)). Reference keys such as [JC16] point to [`../references.md`](../references.md).

---

## Week 5 — PCA I: what PCA computes, and why

### 5.1 Setting and notation

* **Data matrix** $X \in \mathbb{R}^{n\times p}$, with rows $x_i^\top$ (observations) and columns as variables.
* **Mean vector:** $\bar x = \frac1n \sum_i x_i$.
* **Centred data:** $X_c = X - \mathbf 1 \bar x^\top$.
* **Sample covariance:** $S = \frac{1}{n-1} X_c^\top X_c$. It is symmetric and positive semi-definite, since $v^\top S v = \|X_c v\|^2/(n-1) \ge 0$.
* **Correlation matrix:** $R = D^{-1/2} S D^{-1/2}$ with $D = \operatorname{diag}(S)$. It is the covariance of the standardised variables.

PCA looks for new variables $z = X_c v$ that are linear combinations of the centred variables. It was introduced geometrically as "lines and planes of closest fit" [Pea01] and statistically as "principal components" [Hot33].

### 5.2 Derivation 1: maximum variance

The sample variance of $z = X_c v$ is $v^\top S v$. It can be made arbitrarily large by rescaling $v$, so we constrain $v^\top v = 1$:

$$\max_{v}\; v^\top S v \quad \text{subject to} \quad v^\top v = 1 .$$

The Lagrangian is $\mathcal L(v,\lambda) = v^\top S v - \lambda (v^\top v - 1)$. Setting $\partial \mathcal L / \partial v = 2Sv - 2\lambda v = 0$ gives

$$S v = \lambda v ,$$

so every stationary point is an eigenvector of $S$. At such a point the objective equals $v^\top S v = \lambda v^\top v = \lambda$, so the maximum is attained at the eigenvector $v_1$ with the **largest** eigenvalue $\lambda_1$.

**The second component** maximises $v^\top S v$ subject to $v^\top v = 1$ and $v^\top v_1 = 0$. With multipliers $\lambda$ and $\mu$:

$$2Sv - 2\lambda v - \mu v_1 = 0 .$$

Pre-multiplying by $v_1^\top$ and using $v_1^\top S v = \lambda_1 v_1^\top v = 0$ gives $\mu = 0$. Hence $Sv = \lambda v$ again, and the maximum is $\lambda_2$. By induction, the $j$-th principal component direction is the $j$-th eigenvector.

**Spectral theorem.** $S = V \Lambda V^\top$, where $V$ is orthogonal and $\lambda_1 \ge \dots \ge \lambda_p \ge 0$.

### 5.3 Consequences

| Quantity | Formula | Meaning |
|---|---|---|
| Scores | $Z = X_c V$ | Coordinates of each observation on the components |
| Covariance of scores | $\operatorname{Cov}(Z) = V^\top S V = \Lambda$ | Scores are **uncorrelated**; variance of component $j$ is $\lambda_j$ |
| Total variance | $\operatorname{tr}(S) = \sum_j \lambda_j$ | Rotation preserves total variance |
| Explained-variance ratio | $\lambda_j / \sum_k \lambda_k$ | Share of total variance on component $j$ |
| Loadings and correlations | $\operatorname{corr}(x_k, z_j) = v_{kj}\sqrt{\lambda_j}/s_k$ | Coefficients and correlations differ unless variables are standardised [CJ95] |

### 5.4 Derivation 2: minimum reconstruction error

Project each centred observation onto a $k$-dimensional subspace with orthonormal basis $W \in \mathbb{R}^{p\times k}$: $\hat x_i - \bar x = W W^\top (x_i - \bar x)$. By Pythagoras,

$$\|x_i-\bar x\|^2 = \|WW^\top(x_i-\bar x)\|^2 + \|(I-WW^\top)(x_i-\bar x)\|^2 .$$

The left-hand side does not depend on $W$, so **minimising the residual sum of squares is the same as maximising the projected variance**. The optimum is $W = V_k$, the first $k$ eigenvectors, with minimum value

$$\frac{1}{n-1}\sum_{i=1}^n \|x_i - \hat x_i\|^2 = \sum_{j>k} \lambda_j .$$

In matrix form this is the Eckart–Young theorem: truncated SVD gives the best rank-$k$ approximation in Frobenius norm [EY36].

### 5.5 Derivation 3: the SVD route (how software actually computes PCA)

Write $X_c = U \Sigma V^\top$, with $U$ having orthonormal columns and singular values $\sigma_1 \ge \sigma_2 \ge \dots$. Then

$$S = \frac{1}{n-1} V \Sigma^2 V^\top \;\Rightarrow\; \lambda_j = \frac{\sigma_j^2}{n-1}, \qquad Z = X_c V = U\Sigma .$$

**Numerical advice.**

* Prefer the SVD of $X_c$, or `numpy.linalg.eigh` on $S$, to `numpy.linalg.eig`. `eig` does not assume symmetry and does not sort its output. In the audit environment (numpy 2.5.4) it returned **complex** values for the Wine correlation matrix; under numpy 2.2.6 it returned real values. Its output is unsorted in both versions.
* Forming $X_c^\top X_c$ squares the condition number; the SVD avoids that.

### 5.6 Indeterminacy

* **Sign.** If $v$ solves $Sv = \lambda v$, so does $-v$. Different libraries return different signs; for Wine, PC1 from scikit-learn and from a raw SVD differ in sign. *Interpret patterns of signs within a component, never the overall sign.*
* **Rotation.** If $\lambda_j = \lambda_{j+1}$, only the subspace is identified, not the individual axes.

### 5.7 Covariance PCA or correlation PCA?

PCA is **not scale-invariant**. If variables have different units, covariance PCA is dominated by the variable with the largest numerical variance.

**Worked example B (Wine, 178 × 13).**

* The sample variances are: proline 99,166.72; magnesium 203.99; alcalinity of ash 11.15.
* **Covariance PCA:** PC1 explains **99.81%** of the variance, and its coefficient on proline is 0.9998. "PC1" is simply proline measured in mg/L.
* **Correlation PCA** (standardised variables): the explained-variance ratios are 0.362, 0.192, 0.111, 0.071 and 0.066, with cumulative 0.362, 0.554, 0.665, 0.736 and 0.802.
* The largest |coefficients| on PC1 are flavanoids 0.423, total phenols 0.395, OD280/OD315 0.376 and proanthocyanins 0.313: a "phenolic content" contrast. On PC2 they are colour intensity 0.530, alcohol 0.484, proline 0.365 and ash 0.316.

**Rule [R]:** use correlation PCA when variables are in different units or their variances are not comparable on substantive grounds. Use covariance PCA when the units are common and the size of the variance is meaningful, for example pixel intensities or repeated measurements of one quantity.

### 5.8 Assumptions and limitations

1. **Linear** structure: PCA finds linear subspaces. Curved manifolds belong to week 8.
2. **Variance is treated as importance.** Large-variance directions need not be the interesting or predictive ones (week 6, §6.4).
3. **Second-order statistics only.** Components are uncorrelated, not independent. Independence is the subject of ICA (week 7).
4. **Sensitivity to outliers** (week 6, §6.5).
5. **Centring is part of the method.** "PCA" on uncentred data finds the direction of the mean. For Wine, the first right singular vector of the uncentred matrix has cosine 0.99984 with the mean vector.
6. Plain PCA is a descriptive decomposition, not a probabilistic model: there are no standard errors here. Probabilistic PCA and inference are outside the course scope.

### 5.9 Worked example A — by hand (also lab task T1)

The data, five observations:

| obs | $x_1$ | $x_2$ |
|---|---|---|
| 1 | 6 | 6 |
| 2 | 2 | 5 |
| 3 | 0 | 2 |
| 4 | 0 | 6 |
| 5 | 2 | 6 |

1. **Means.** $\bar x = (2, 5)$. The centred rows are $(4,1), (0,0), (-2,-3), (-2,1), (0,1)$.
2. **Covariance.** $\sum x_1^2 = 24$, $\sum x_2^2 = 12$ and $\sum x_1x_2 = 8$ (centred). Dividing by $n-1 = 4$ gives

   $$S = \begin{pmatrix} 6 & 2\\ 2 & 3\end{pmatrix}.$$

3. **Eigenvalues.** $\det(S-\lambda I) = \lambda^2 - 9\lambda + 14 = (\lambda-7)(\lambda-2)$, so $\lambda_1 = 7$ and $\lambda_2 = 2$.
4. **Eigenvectors.** For $\lambda_1 = 7$: $(S-7I)v = 0$ means $-v_1 + 2v_2 = 0$, so $v_1 = (2,1)^\top/\sqrt5$. Orthogonal to it is $v_2 = (1,-2)^\top/\sqrt5$.
5. **Scores.** $z_{i1} = (2x_{i1}^c + x_{i2}^c)/\sqrt5 = (9, 0, -7, -3, 1)/\sqrt5$, and $\operatorname{Var}(z_1) = \frac{140/5}{4} = 7 = \lambda_1$. ✓
6. **Explained variance.** PC1 explains $7/9 = 0.778$.
7. **Rank-1 reconstruction error.** Dividing the residual sum of squares by $n-1$ gives $\lambda_2 = 2$. ✓
8. **SVD check.** $\sigma_1 = \sqrt{7\cdot 4} = 5.2915$ and $\sigma_2 = \sqrt{2\cdot4} = 2.8284$.

`numpy.linalg.eigh` returns $v_1 = (-0.894, -0.447)$, the same direction with the opposite sign (§5.6).

### 5.10 In-lecture misconception checks (week 5)

These are MC1–MC4 in [`../exercises/misconception-checks.md`](../exercises/misconception-checks.md). They cover centring, unit dominance, sign interpretation, and uncorrelated vs independent.

---

## Week 6 — PCA II: PCA in practice

### 6.1 Choosing the number of components $k$: depends on the purpose

| Purpose | Criterion |
|---|---|
| Description / visualisation | Scree plot elbow; cumulative explained variance (e.g. 80%) |
| "Signal vs noise" in correlation PCA | Eigenvalue above 1 (Kaiser rule; crude) or **Horn's parallel analysis** [Hor65] |
| Prediction | **Inner cross-validation of the downstream model** (nested CV) |

**Wine, correlation PCA:**

* Eigenvalues: 4.732, 2.511, 1.454, 0.924, 0.858.
* The eigenvalue-above-one rule keeps $k = 3$.
* Cumulative explained variance reaches 80% at $k = 5$ (0.802).
* **Parallel analysis** with 200 column-permuted copies gives 95th-percentile null eigenvalues 1.581, 1.423, 1.317, 1.239 and 1.164, so it keeps $k = 3$.

**Parallel analysis procedure.**

1. Permute each column independently. This destroys correlation and keeps the marginal distributions.
2. Recompute the eigenvalues of the permuted data's correlation matrix.
3. Repeat $B$ times.
4. Keep the components whose observed eigenvalue exceeds the chosen quantile of the null eigenvalues at the same rank.

**Why naive hold-out reconstruction error cannot choose $k$.** Projecting a new observation onto a larger subspace can never increase its residual. The hold-out error is therefore non-increasing in $k$ and always selects $k = p$. Proper cross-validation of component models needs special schemes [Wol78; BKSK08].

### 6.2 PCA inside the validation boundary

PCA is a **fitted** transformation (mean, scaling, rotation), so it belongs inside `Pipeline(StandardScaler(), PCA(k), model)`. Choose $k$ by an *inner* CV and estimate performance by an *outer* CV (nested CV).

**Worked example C (digits, 1,797 × 64; 5-fold stratified CV, course seed):**

| Model | CV accuracy, mean ± sd |
|---|---|
| Majority class | 0.101 |
| Standardise + logistic regression, all 64 pixels (**baseline**) | **0.969 ± 0.012** |
| Standardise + PCA(10) + logistic regression | 0.884 ± 0.016 |
| Standardise + PCA(20) + logistic regression | 0.947 ± 0.014 |
| Standardise + PCA(30) + logistic regression | 0.957 ± 0.016 |
| Standardise + PCA(40) + logistic regression | 0.964 ± 0.017 |
| Nested CV, $k \in \{5,10,20,30,40\}$ chosen in inner CV | 0.964 ± 0.017 (refitting the grid search on all rows selects $k = 40$) |

**Conclusion to teach:** on these data, PCA does **not** improve predictive accuracy over the raw-feature baseline, and model selection pushes $k$ to the top of the grid. PCA can still be worth using to reduce storage, computation or collinearity, but that is a different claim and must be stated as such. *Always compare with a baseline.*

### 6.3 How large is leakage from fitting PCA before splitting?

A noise experiment: $n = 60$ observations, $p = 2000$ noise features and random labels, so the true accuracy is 0.5. Each figure below is the mean of 20 repetitions of 5-fold CV.

| Fitted step | Fitted on all rows, then CV | Inside the pipeline |
|---|---|---|
| PCA(10, `random_state` fixed) (does **not** use $y$) | 0.485 | 0.561 |
| SelectKBest(10) (**uses** $y$) | **0.909** | 0.523 |

Fitting PCA before the split did not inflate accuracy in this experiment: both settings are near chance, and the gap between them is noise. Supervised feature selection before the split inflated accuracy from about 0.52 to **0.91**.

Reproducibility note: for wide data ($p \gg n$), scikit-learn's `PCA` switches automatically to a **randomised** SVD solver. Without `random_state`, results then change from run to run; an earlier unseeded run of this experiment gave 0.488 instead of 0.485.

**Rule (absolute):** every fitted step goes inside the validation boundary. The *size* of the bias depends on whether the step uses $y$ [KN23]. Unsupervised leakage can still matter, for example under distribution shift or with very small $n$, so the rule does not have exceptions.

### 6.4 Variance is not relevance; visualisation is not prediction

**Worked example D (synthetic, $n = 400$, course seed).**

* $x_1 \sim N(0, 5^2)$ carries no class information.
* $x_2 = \pm 1.2 + N(0, 0.5^2)$ carries it.
* The sample variances are 26.57 and 1.69, so PC1 is essentially $x_1$.

| Model (5-fold CV) | Accuracy |
|---|---|
| PCA(1) + logistic regression | 0.54 |
| LDA(1) + logistic regression | 0.997 |
| Logistic regression on both variables | 0.997 |

PCA is unsupervised: it ranks directions by variance, not by relevance to $y$. LDA, a supervised projection, is covered in week 7 [Fis36].

**Digits.**

| Representation | Classifier | Accuracy |
|---|---|---|
| 2 principal components (what a 2-D scatter plot shows) | Logistic regression | 0.545 |
| 2 principal components | k-NN | 0.545 |
| 30 principal components | k-NN | 0.974 |
| All pixels | k-NN | 0.978 |

A 2-D PCA picture can look disappointing while the data remain highly predictable, and the reverse can also happen. *A good-looking plot and a useful feature set are different claims, and each needs its own evidence.*

### 6.5 Outliers and robustness

Wine, standardised. Moving **one** observation of 178 by 15 units along the PC2 direction rotates PC1 by **19.2°**. Diagnose outliers with score distances and orthogonal distances; robust alternatives include ROBPCA [HRV05]. Report sensitivity instead of silently deleting points.

### 6.6 Special data types

* **Compositional data** (shares that sum to a constant, e.g. budget or revenue composition): the closure constraint induces spurious negative correlations. Apply a log-ratio transform, such as the centred log-ratio, before PCA [Ait83]. This is relevant to the Thai local-government revenue extension case.
* **Large $n$ or $p$:** randomised SVD [HMT11] and `IncrementalPCA`, covered in week 13 (HPC).

### 6.7 In-lecture misconception checks (week 6)

These are MC5–MC8: choosing $k$ on the test set, "more variance means more predictive", "PCA before the split is always harmless", and "a 2-D plot shows whether classes are separable".

---

### Summary table for students

| Concept | Key statement |
|---|---|
| Objective | $\max v^\top S v$ subject to $\|v\| = 1$ ⇒ $Sv = \lambda v$ |
| Equivalent objective | Minimum reconstruction error; error $= \sum_{j>k}\lambda_j$ |
| Computation | SVD of $X_c$: $\lambda_j = \sigma_j^2/(n-1)$; scores $= U\Sigma$ |
| Identifiability | Sign always; rotation when eigenvalues are equal |
| Scaling | Covariance PCA if units are comparable; otherwise correlation PCA |
| Choosing $k$ | Purpose-dependent; parallel analysis; nested CV for prediction |
| Validity | Fit inside the validation boundary; compare with a baseline |
| Limits | Linear; variance ≠ relevance; outliers; uncorrelated ≠ independent |
