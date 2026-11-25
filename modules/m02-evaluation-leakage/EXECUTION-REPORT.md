# Execution report — module m02

**Date:** 25 November 2026. Every result below comes from running the code **[V]**.

## 1. Environments

The two pinned environments are those of the [m04 execution report](../m04-pca/EXECUTION-REPORT.md#1-environments), with **imbalanced-learn 0.14.2** (and its helper `sklearn-compat` 0.1.6) added in both:

| Environment | scikit-learn | imbalanced-learn |
|---|---|---|
| `environment/requirements-local.txt` (pinned local) | 1.9.1 | 0.14.2 |
| `environment/requirements-colab-proxy.txt` (Colab proxy) | 1.6.1 | 0.14.2 |

The Colab-proxy imbalanced-learn version is an **assumption**, not a measured Colab snapshot; the lab's setup code installs imbalanced-learn if a runtime does not have it.

## 2. Results

| Check | Pinned local | Colab proxy |
|---|---|---|
| Student notebook: valid, no outputs, badge and setup cell, every task raises `NotImplementedError` | pass | pass |
| Student notebook: given cells run top to bottom with every task and self-check removed | pass | pass |
| Solution notebook (private): runs top to bottom, all 5 self-checks print `OK`, ids match the student notebook | pass | pass |
| Mutation test (private): 6 typical mistakes injected, one at a time | 6/6 caught | 6/6 caught |
| Auto-checker (private): solution scores 3/3 and 1/1 (23/23 hidden-test points); each mutant loses correctness on its own task; a blank notebook scores 0 | pass | pass |
| Answer-key numbers (`key_numbers.py`, private) | identical output | identical output |

**The six injected mistakes:** a Wald interval instead of Wilson, and a random-guess baseline instead of the majority class (T1); rows split at random inside the grouped scorer (T2); no leakage shown for the supervised step (T3); the SMOTE-before score not computed (T4); the wrong column removed in the audit (T5).

## 3. Numbers quoted in the lecture outline and the lab

| Quantity | Value |
|---|---|
| Digits, "is it a 9?" | 180 of 1,797 images (10.0%); test set 450 images |
| Majority baseline / logistic regression, test accuracy (95% Wilson) | 0.900 (0.869–0.924) / 0.973 (0.954–0.985) |
| Grouped patients (40 × 10), 1-NN: KFold / GroupKFold | 1.000 / 0.578 |
| Noise (100 × 1,000), repeated 5×5-fold CV: SelectKBest(20) before / inside | 0.776 / 0.410 |
| Same: StandardScaler before / inside | 0.506 / 0.516 |
| "Is it a 9?", 5-fold F1: plain / class weights / SMOTE inside / SMOTE before | 0.937 / 0.872 / 0.894 / 0.990 (0.9902 local, 0.9905 Colab proxy) |
| Clinic (600 patients): AI analysis / honest / majority baseline | 0.935 / 0.663 / 0.515 |

The only difference between the environments is the fourth decimal of the invalid SMOTE-before score; the hidden tests allow ±0.01.

## 4. Limitations

* **Not yet run in a real Colab runtime.** Before the session, open Lab 2 from its badge in Colab and run *Restart session and run all* once.
* The Colab badge points to the `main` branch, so it works once this module is merged into `main`.
* Run time: the whole solution notebook runs in about 4 seconds per run in the grader on a laptop CPU.
