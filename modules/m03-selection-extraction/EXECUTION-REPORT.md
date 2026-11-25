# Execution report — module m03

**Date:** 25 November 2026. Every result below comes from running the code **[V]**.

## 1. Environments

The two pinned environments of the [m04 execution report](../m04-pca/EXECUTION-REPORT.md#1-environments); this module needs no extra packages.

## 2. Results

| Check | Pinned local | Colab proxy |
|---|---|---|
| Student notebook: valid, no outputs, badge and setup cell, every task raises `NotImplementedError` | pass | pass |
| Student notebook: given cells run top to bottom with every task and self-check removed | pass | pass |
| Solution notebook (private): runs top to bottom, all 5 self-checks print `OK`, ids match the student notebook | pass | pass |
| Mutation test (private): 6 typical mistakes injected, one at a time | 6/6 caught | 6/6 caught |
| Lab outputs and answer-key numbers | identical | identical |

**The six injected mistakes:** row 0's distance to itself included (T1); a random-guess baseline, and a single 5-fold run instead of the repeated CV (T2); selection frequencies not sorted (T3); "test" importance computed on the training data (T4); training importance computed on the test data (T5).

## 3. Numbers quoted in the lecture outline and the lab

| Quantity | Value |
|---|---|
| Distance contrast, 500 random points, p = 2 / 10 / 100 / 1000 | 50.3 / 2.39 / 0.37 / 0.10 |
| Wine, repeated 5×5-fold CV, mean (sd): majority / all 13 / SelectKBest 5 / RFE 5 / PCA 5 | 0.399 (0.015) / 0.980 (0.023) / 0.975 (0.029) / 0.969 (0.032) / 0.967 (0.030) |
| Selection frequency over 25 folds, SelectKBest / RFE | alcohol, proline, flavanoids 1.00 / 1.00; colour intensity 0.88 / 0.96; OD280/OD315 1.00 / 0.24; hue 0.12 / 0.80 |
| Mean Jaccard similarity, SelectKBest / RFE | 0.927 / 0.868 |
| Synthetic signal and noise, random forest: train / test accuracy | 1.000 / 0.633 |
| Impurity importance: signal / noise_cont / noise_id / noise_bin | 0.159 / 0.402 / 0.411 / 0.028 |
| Permutation importance on training data | 0.314 / 0.281 / 0.291 / 0.134 |
| Permutation importance on test data | 0.119 / 0.000 / 0.021 / −0.026 |

## 4. Limitations

* **Not yet run in a real Colab runtime.** Before the session, open Lab 3 from its badge in Colab and run *Restart session and run all* once.
* The Colab badge points to the `main` branch, so it works once this module is merged into `main`.
* Part 3 refits two selectors on 25 folds and Part 4 computes permutation importance with 30 repeats; the whole solution notebook runs in about 12 seconds on a laptop CPU.
