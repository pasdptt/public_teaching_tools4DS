# Weeks 5–6 — Principal Component Analysis (pilot module)

| Status | Backlog item | Course CLOs | Blueprint |
|---|---|---|---|
| **Pilot built**: awaiting lecturer review | B04 | CLO1, CLO2, CLO3 | [weekly plan](../../docs/blueprint/03-curriculum-blueprint.md#5-weekly-lecture-and-lab-plan-p) |

**Workspace:** Google Colab (open the labs with the badges below); a pinned local environment is the fallback.

| Material | Link |
|---|---|
| Lecture outline (equations, assumptions, worked examples, misconception checks) | [`lecture/outline.md`](lecture/outline.md) |
| Lab 05 — PCA I: from theory to code | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pasdptt/public_teaching_tools4DS/blob/main/modules/w05-w06-pca/lab/lab05_pca_theory.ipynb) [`lab/lab05_pca_theory.ipynb`](lab/lab05_pca_theory.ipynb) |
| Lab 06 — PCA II: PCA in practice | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pasdptt/public_teaching_tools4DS/blob/main/modules/w05-w06-pca/lab/lab06_pca_practice.ipynb) [`lab/lab06_pca_practice.ipynb`](lab/lab06_pca_practice.ipynb) |
| Problem set (hand and practical exercises) | [`exercises/problem-set.md`](exercises/problem-set.md) |
| Misconception checks (formative) | [`exercises/misconception-checks.md`](exercises/misconception-checks.md) |
| References (each verified against its Crossref DOI record) | [`references.md`](references.md) |
| Execution report | [`EXECUTION-REPORT.md`](EXECUTION-REPORT.md) |

Instructor solutions, answer keys and summative assessment items are kept in the private instructor material. They are not in this public repository.

> The Colab badges point to the `main` branch. They work once this module is merged into `main`.

## 1. Measurable objectives

By the end of week 6, a student can:

| ID | Objective (observable) | Course CLO | Evidence |
|---|---|---|---|
| PCA-O1 | **Derive** the first principal component as the solution of $\max_{v} v^\top S v$ subject to $v^\top v = 1$ using a Lagrange multiplier, and **state** why later components are the remaining eigenvectors in decreasing eigenvalue order. | CLO1 | Lecture check; midterm derivation item |
| PCA-O2 | **Compute by hand**, for a 2×2 covariance matrix: eigenvalues, unit eigenvectors, scores, explained-variance ratios and the rank-1 reconstruction error. | CLO1 | Lab 05 task T1; problem set P1–P2; midterm computation item |
| PCA-O3 | **Verify numerically** that the eigenvectors of $S$ equal the right singular vectors of the centred data, with $\lambda_j = \sigma_j^2/(n-1)$, and that the reconstruction error equals the sum of the discarded eigenvalues. | CLO1 | Lab 05 tasks T2–T3 |
| PCA-O4 | **Choose and justify** covariance or correlation PCA from the measurement units, and **interpret** loadings while allowing for sign indeterminacy. | CLO1, CLO3 | Lab 05 task T4 and answer Q2 |
| PCA-O5 | **Select** the number of components with a scree plot, cumulative explained variance, the eigenvalue-above-one rule and Horn's parallel analysis, and **justify** the choice for a stated purpose. | CLO3 | Lab 06 task T1 and answer Q1 |
| PCA-O6 | **Fit PCA inside the validation boundary** (`Pipeline` with nested cross-validation) and **compare** it with a raw-feature baseline, reporting uncertainty. | CLO2, CLO3 | Lab 06 tasks T2–T3 |
| PCA-O7 | **Explain**, using a counterexample, why high-variance directions need not be predictive, and **distinguish** visualisation quality from predictive usefulness. | CLO3 | Lab 06 task T4 and answer Q3; final item |
| PCA-O8 | **Diagnose** PCA failure modes: uncentred data, unit dominance, outliers, `eig` vs `eigh`, sign flips, and fitting before the split. | CLO2 | Failure-analysis sections of both labs |

## 2. Prerequisites (assumed; see blueprint §10.2)

* Matrix algebra: transpose, inverse, eigenvalues and eigenvectors of a symmetric matrix, orthogonal matrices.
* Statistics: sample mean, sample variance and covariance with divisor $n-1$, correlation.
* Course weeks 1–3: the Colab workflow, `Pipeline`, cross-validation and baselines.

## 3. Lesson plan

### Week 5 — PCA I: theory (2 h lecture + 3 h lab + 5 h independent)

| Time | Lecture activity | Objective |
|---|---|---|
| 0:00–0:10 | Retrieval quiz: eigen-decomposition of a 2×2 symmetric matrix (hand) | prerequisite |
| 0:10–0:45 | Motivation (Pearson 1901; Hotelling 1933). Variance maximisation, Lagrange derivation, spectral theorem | O1 |
| 0:45–0:55 | Break | |
| 0:55–1:25 | Minimum reconstruction error; Eckart–Young; SVD of the centred data matrix; scores and loadings | O3 |
| 1:25–1:50 | Worked example A (hand, 5 points); worked example B (Wine: covariance vs correlation PCA) | O2, O4 |
| 1:50–2:00 | Misconception checks MC1–MC4 (show of hands or polling), then lab preview | O1–O4 |

| Time | Lab 05 activity | Objective |
|---|---|---|
| 0:00–0:15 | Open the lab in Colab; run the setup cell; restart and run all | workflow |
| 0:15–0:50 | Part 1: the hand example, checked in code (T1) | O2 |
| 0:50–1:30 | Part 2: PCA via SVD from scratch vs scikit-learn (T2) | O3 |
| 1:30–1:45 | Break | |
| 1:45–2:15 | Part 3: reconstruction error identity (T3) | O3 |
| 2:15–2:40 | Part 4: covariance vs correlation PCA on Wine (T4) and interpretation (Q2) | O4 |
| 2:40–3:00 | Part 5: failure analysis (Q3); AI-use log; submit | O8 |

**Independent work (5 h):** problem set P1–P4 (2 h); reading — Jolliffe & Cadima (2016), sections 1–2 (1.5 h); finish the lab (1.5 h).

### Week 6 — PCA II: practice (2 h lecture + 3 h lab + 5 h independent)

| Time | Lecture activity | Objective |
|---|---|---|
| 0:00–0:10 | Retrieval: reconstruction-error identity; covariance vs correlation | O3, O4 |
| 0:10–0:40 | Choosing k: scree, cumulative explained variance, the eigenvalue-above-one rule, Horn's parallel analysis; why naive hold-out reconstruction error cannot choose k | O5 |
| 0:40–0:50 | Break | |
| 0:50–1:20 | PCA for prediction: pipelines, nested CV, baselines; leakage magnitudes (unsupervised vs supervised steps) | O6 |
| 1:20–1:45 | Visualisation vs prediction; a low-variance but discriminative direction (PCA vs LDA preview); outliers and robust PCA; compositional data | O7, O8 |
| 1:45–2:00 | Misconception checks MC5–MC8; project link (milestone M2 due in week 7) | O5–O8 |

| Time | Lab 06 activity | Objective |
|---|---|---|
| 0:00–0:40 | Part 1: choosing k on Wine, including parallel analysis (T1, Q1) | O5 |
| 0:40–1:30 | Part 2: digits — baseline vs PCA pipeline with nested CV (T2) | O6 |
| 1:30–1:45 | Break | |
| 1:45–2:10 | Part 3: leakage magnitudes (T3) | O6 |
| 2:10–2:40 | Part 4: variance is not relevance (T4, Q3) | O7 |
| 2:40–3:00 | Part 5: one outlier (T5); failure analysis and interpretation (Q4); AI-use log | O8 |

**Independent work (5 h):** problem set P5–P8 (2 h); project data audit for M2 (2 h); reading — Bro et al. (2008), sections on why naive cross-validation fails (1 h).

## 4. Datasets (all openly licensed; no download needed for the labs)

| Dataset | Use | Licence (verified 9 Nov 2026) |
|---|---|---|
| Hand example (5 × 2, defined in the lab) | Worked example A, lab task T1 | n/a |
| Wine (UCI 109, DOI 10.24432/C5PC7J; bundled with scikit-learn) | Covariance vs correlation PCA; choosing k; outliers | CC BY 4.0 |
| Digits (UCI 80, DOI 10.24432/C50P49; bundled with scikit-learn) | PCA for prediction | CC BY 4.0 |
| Synthetic data (generated with the course seed) | Leakage magnitudes; the "variance is not relevance" counterexample | n/a |

The Thai local-government revenue table is reserved as an extension case. It awaits licence confirmation (blueprint Q-D1).

## 5. Assessment links

* **Practical work:** labs L5 and L6, each graded with the lab rubric (blueprint §7.4).
* **Midterm:** hand computation (O2) and derivation (O1) item types (blueprint §7.2).
* **Final:** visualisation vs prediction (O7), and PCA computation and interpretation (pre-midterm share).
* **Project:** milestone M2 requires any PCA to be inside the validation boundary (O6).
