# Execution report — module m06

**Date:** 25 November 2026. Every result below comes from running the code **[V]**.

## 1. Environments

The two pinned environments of the [m04 execution report](../m04-pca/EXECUTION-REPORT.md#1-environments); this module needs no extra packages (the autoencoder is scikit-learn's `MLPRegressor`).

## 2. Results

| Check | Pinned local | Colab proxy |
|---|---|---|
| Student notebook: valid, no outputs, badge and setup cell, every task raises `NotImplementedError` | pass | pass |
| Student notebook: given cells run top to bottom with every task and self-check removed | pass | pass |
| Solution notebook (private): runs top to bottom, all 5 self-checks print `OK`, ids match the student notebook | pass (about 50 s; tanh autoencoder 14 s) | pass (about 47 s) |
| Mutation test (private): 5 typical mistakes injected, one at a time | 5/5 caught | 5/5 caught |
| Answer-key numbers (`key_numbers.py`, private) | as below | as below |

**The five injected mistakes:** PCA used in place of t-SNE (T1); accuracy computed on the training data (T2); the second t-SNE run not used (T3); the autoencoder stopped after 20 iterations (T4); the softmax bound divided by p instead of p² (T5).

## 3. Numbers quoted in the lecture outline and the lab

| Quantity | Pinned local | Colab proxy |
|---|---|---|
| Trustworthiness (k = 10): PCA / kernel PCA / Isomap / LLE / t-SNE | 0.830 / 0.828 / 0.837 / 0.925 / 0.993 | same |
| t-SNE trustworthiness at perplexity 5 / 30 / 100 | 0.991 / 0.993 / 0.991 | 0.991 / 0.993 / **0.990** |
| 5-NN accuracy, 5-fold CV: majority / raw 64 / PCA(2) / kernel PCA(2) / Isomap(2) / LLE(2) / PCA(10) | 0.101 / 0.986 / 0.620 / 0.635 / 0.776 / 0.868 / 0.974 | same |
| AI-generated pipeline (t-SNE on all rows + random forest, 5-fold CV) | 0.991 | same |
| Forest trained on t-SNE run A: test on run A / on run B | 0.991 / 0.289 | **0.984 / 0.287** |
| Test MSE, k = 10: PCA / linear autoencoder / tanh autoencoder | 0.0196 / 0.0196 / 0.0101 | same |
| Test MSE by k (PCA / tanh AE): 2, 5, 20 | 0.0529 / 0.0366; 0.0333 / 0.0178; 0.0080 / 0.0045 | same |
| Test pixel row sums: mean (min, max); softmax MSE bound | 19.52 (11.56, 26.69); 0.0848 | same |

The environments differ only in the t-SNE run-to-run accuracies and one trustworthiness value, in the second or third decimal; the self-checks allow for this.

## 4. Limitations

* **Not yet run in a real Colab runtime.** Before the session, open Lab 6 from its badge in Colab and run *Restart session and run all* once; the tanh autoencoder takes about 15 s on this machine's CPU and may take longer in Colab.
* The Colab badge points to the `main` branch, so it works once this module is merged into `main`.
* Objective m06-O4 (pretrained embeddings of Thai text) is not yet taught: it waits for a corpus with a verified open licence (backlog B20). The lecture covers the idea without data.
