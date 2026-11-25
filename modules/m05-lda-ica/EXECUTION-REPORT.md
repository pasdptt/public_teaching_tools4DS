# Execution report — module m05

**Date:** 25 November 2026. Every result below comes from running the code **[V]**.

## 1. Environments

The two pinned environments of the [m04 execution report](../m04-pca/EXECUTION-REPORT.md#1-environments); this module needs no extra packages.

## 2. Results

| Check | Pinned local | Colab proxy |
|---|---|---|
| Student notebook: valid, no outputs, badge and setup cell, every task raises `NotImplementedError` | pass | pass |
| Student notebook: given cells run top to bottom with every task and self-check removed | pass | pass |
| Solution notebook (private): runs top to bottom, all 5 self-checks print `OK`, ids match the student notebook | pass (3.2 s) | pass (2.6 s) |
| Mutation test (private): 5 typical mistakes injected, one at a time | 5/5 caught | 5/5 caught |
| Auto-checker (private): solution scores 3/3 and 1/1 (25/25 hidden-test points); each mutant loses correctness on its own task; a blank notebook scores 0 | pass | pass |
| Answer-key numbers (`key_numbers.py`, private) | identical | identical |

**The five injected mistakes:** the smallest generalised eigenvalues kept (T1); PCA used in place of LDA (T2); no leakage shown for LDA (T3); the sign of recovered components not ignored in the recovery score (T4); the Gaussian case not computed (T5).

## 3. Numbers quoted in the lecture outline and the lab

| Quantity | Pinned local | Colab proxy |
|---|---|---|
| Wine generalised eigenvalues (standardised) | 9.0817, 4.1285 | same |
| Wine, repeated 5×5-fold CV: majority / all 13 / PCA(2) / LDA(2), mean (sd) | 0.399 (0.015) / 0.980 (0.023) / 0.961 (0.031) / **0.988 (0.016)** | 0.399 / 0.980 / 0.961 / **0.986 (0.018)** |
| Noise (100 × 200, 3 classes): LDA(2) before / inside the pipeline | 0.810 / 0.310 | same |
| Source excess kurtosis (sine, square, sawtooth) | −1.365, −1.991, −1.200 | same |
| Recovery of the three signals: FastICA / PCA | 0.998 / 0.745 | same |
| Gaussian sources, FastICA seeds 0–4: recovery | 0.815, 0.815, 0.799, 0.791, 0.816 | same |
| Gaussian sources: agreement of runs 1–4 with run 0 | 1.000, 0.849, 0.877, 1.000 | same |

The only difference between the environments is the LDA(2) accuracy in the third decimal; the hidden tests allow ±0.012.

## 4. Limitations

* **Not yet run in a real Colab runtime.** Before the session, open Lab 5 from its badge in Colab and run *Restart session and run all* once.
* The Colab badge points to the `main` branch, so it works once this module is merged into `main`.
* FastICA prints convergence warnings on the Gaussian data; the lab silences them in Part 5 and the lecture explains them.
