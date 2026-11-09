# Execution Report — existing 040563107 notebooks

**Date:** 9 November 2026. **Status:** every figure below was produced by running code **[V]**. Machine-readable results are in [`execution/reports/`](execution/reports/); the targeted checks are in [`execution/targeted-checks.txt`](execution/targeted-checks.txt).

## 1. What was executed

* Twelve notebooks retrieved read-only from the lecturer's Google Drive: N01–N12 in [`01-evidence-audit.md` §1.3](01-evidence-audit.md#13-notebooks-and-data).
* Downloaded byte counts matched the Drive metadata for every file.
* The notebooks themselves are **not** committed to this public repository: two are examination papers and they contain the lecturer's unpublished material.

## 2. Protocol

1. **Fresh kernel.** Each notebook ran top to bottom in a new kernel with `nbclient` 0.11.0. Every cell ran even after earlier errors (`allow_errors=True`), so every failure point was recorded. Each cell had a 1,500 s timeout.
2. **Shell commands neutralised, not executed.** Every line beginning with `!`, `%pip` or `%%bash` was replaced by a logged no-op: `apt-get update/upgrade`, `pip install`, `wget` of Spark, `kaggle … download` and `unzip`. Reasons: `apt-get upgrade` must not run on the audit host, and the stored Kaggle credential was deliberately not used. Each report's `skipped_shell_lines` lists what was skipped.
3. **Three modes:**

| Mode | Packages | `google.colab` and Drive paths | Purpose |
|---|---|---|---|
| **A — clean local** | Latest releases on 9 Nov 2026: Python 3.12.3, numpy 2.5.4, pandas 3.1.1, scikit-learn 1.9.1, scipy 1.18.1, Matplotlib 3.11.2, seaborn 0.13.2, statsmodels 0.15.0, networkx 3.7, imbalanced-learn 0.14.2, TensorFlow 2.21.0 / Keras 3.15.1, PySpark 4.3.0, OpenJDK 21 | Absent; empty working directory | A student's laptop today. |
| **B — Colab-simulated, latest** | As A | A stub `google.colab.drive.mount` (`tools/audit/colabstub/`); `/content/...` paths mapped to local copies of AirQualityUCI.csv (Drive copy), `train.csv` (Drive copy) and `mushrooms.csv` (rebuilt from UCI id 73, SHA-256 of zip `face32f3…1f60b1a`) | Removes data-access failures. |
| **C — Colab-simulated, Colab-era pins** | numpy 2.2.6, pandas 2.2.3, scikit-learn 1.6.1, Matplotlib 3.10.9, statsmodels 0.14.6, networkx 3.4.2, imbalanced-learn 0.14.0, scipy 1.18.1, TensorFlow 2.21.0 | As B | Removes version drift; whatever still fails is a defect in the notebook. |

The mode-C pins were inferred from the warnings stored in the notebooks' own last Colab outputs **[A — Colab's exact package list for those runs is not recorded]**. The inferences were:

* pandas `'A'` FutureWarning → pandas 2.x;
* Matplotlib `labels→tick_labels` deprecation → 3.9–3.10;
* scikit-learn `TSNE n_iter` FutureWarning → scikit-learn 1.5–1.6;
* Python 3.12 paths and imbalanced-learn 0.14.1, both printed directly.

**Network:** UCI and OpenML hosts were added to the session's allow-list during the audit. Kaggle and Colab hosts were not reachable from the audit machine.

**Harness corrections (disclosed):**

* The first mode-B run of FeatureExtraction was invalid: my stub created a regular `google` package that shadowed `google.protobuf`. The stub was changed to a namespace package and the notebook rerun; only the rerun is reported.
* The first mode-A runs of four notebooks could see the `/content` staging link. Those notebooks were rerun with the link disabled; only the clean reruns are reported.

## 3. Results matrix

Errors are counted as cells that raised an exception out of all code cells.

| Notebook | Mode A errors | Mode B errors | Mode C errors | First error in mode C (or in A where C is clean) |
|---|---|---|---|---|
| N01 Review: Python | 3/114 | 3/114 | 3/114 | [C] cell 26: `SyntaxError: invalid character '‘' (U+2018)`. Cell 124 (`StatisticsError` for a negative harmonic mean) appears to be an intended demonstration. |
| N02 Review: Python II | 0/74 | 0/74 | 0/74 | none |
| N03 Dimensionality Reductions | 1/19 | 1/19 | **0/19** | [A] cell 23: `TypeError: boxplot() got an unexpected keyword argument 'labels'` (removed in Matplotlib 3.11) |
| N04 PCAinAction | 17/53 | 17/53 | **0/53** | [A] cell 60: `fetch_openml('mnist_784')` raises a `TypeError` inside scikit-learn's ARFF parser under pandas 3.1.1. With pandas 2.3.3 and scikit-learn 1.9.1 it loads (70,000 × 784) in 3.7 s. |
| N05 FeatureExtraction | 23/32 | 4/32 | **0/32** | [A] cell 5: `ModuleNotFoundError: google.colab` (the Kaggle and Drive pathway). [B] cell 38: `TSNE(n_iter=)` removed. |
| N06 smoothing_and_aggregation | 9/28 | 6/28 | **0/28** | [A] cell 11: `freq='A'` invalid in pandas 3 |
| N07 Intro2graphwithPython | 15/29 | 15/29 | 15/29 | [C] cell 32: `FileNotFoundError` for `Airlines.csv` on Drive (the file was not retrievable byte for byte) |
| N07 with substitute data* | — | — | 3/29 | cells 46–48: `NodeNotFound: JAX`. Dijkstra is hard-coded to airports present only in the original 100-row sample. |
| N08 Imbalanced | 0/24 | 0/24 | 0/24 | none |
| N09 SES | 11/15 | 11/15 | 11/15 | [C] cell 2: `FileNotFoundError: Cleandata.csv` (not found anywhere) |
| N10 PCA on spark | 13/17 | 13/17 | 13/17 | [C] cell 2: `ModuleNotFoundError: kora`; Spark installer and Java 8 path hard-coded |
| N11 FN_2021_2 (exam paper) | 1/9 | 1/9 | 1/9 | [C] cell 14: example call `plotpca(df,”target”,5)` is invalid Python |
| N12 TakehomeMT_2020_2 (answer key) | 21/27 | 6/27 | 6/27 | [C] cell 14: `groupby().mean()` on text columns (pandas ≥ 2); cell 25: `NameError: finalDf` (displayed before it is defined); cell 26: length mismatch 1000 vs 183 (`y` was overwritten by a synthetic placeholder) |

\* *Substitute data:* a 100-row random sample (`random_state=2013`) of `nycflights13.flights` with the same 16 columns. Its results are **not** comparable with the original sample's numbers.

## 4. Reproducibility of numbers (mode C against the outputs stored in the notebooks)

| Notebook | Comparable text outputs: identical / different | Cause of differences |
|---|---|---|
| N04 PCAinAction | **27 / 0** | — (no stochastic steps without seeds; MNIST gives 327 components at 95% variance, accuracy 0.9201, as stored) |
| N02 Review: Python II | 62 / 10 | Cosmetic only: NumPy 2 scalar repr (`np.float64(…)`) |
| N06 smoothing_and_aggregation | 14 / 4 | `np.random.randn` without a seed (aggregation demo) |
| N03 Dimensionality Reductions | 6 / 12 | No seeds (synthetic data without `random_state`, unseeded trees and forests); for example, CV accuracy 0.885 stored vs 0.887 rerun |
| N05 FeatureExtraction | 3 / 14 | Unseeded random forests and ICA; timing lines. Confusion matrices shift slightly (ICA: 10/40 errors stored vs 9/42 rerun). |
| N08 Imbalanced | 7 / 14 | Unseeded `make_classification` and samplers |

## 5. Targeted checks (`tools/audit/checks.py`)

| Check | Result [V] | Audit issue |
|---|---|---|
| C1 | N07's time parsing under pandas 3.1.1 produces `['1630:30:00', '755:55:00', '600:00:00']` instead of `16:30:00`, etc. | S6 |
| C2 | AirQualityUCI after `dropna`: 9,357 rows, 366 temperature values equal to −200. The taught EMA reaches −195.3 °C, compared with a minimum of 1.0 °C once −200 is recoded to missing; maximum difference 205.8 °C. | M15 |
| C3 | Titanic `dropna()` keeps 183 of 891 rows. The test set has n = 27; accuracy 21/27 = 0.778, 95% Wilson interval 0.59–0.89; majority-class baseline 0.672. | M21 |
| C4 | `np.linalg.eig` on the Iris petal covariance returns complex dtype; `eigh` returns ascending real eigenvalues. Uncentred projection mean 3.929 vs 0 (variance unchanged). | M2, M3 |
| C5 | On pure-noise labels (n = 200, p = 150), LDA fitted before the split gives test accuracy **0.97**; LDA inside a CV pipeline gives **0.51**. | E1 |
| C6 | Mushroom (5-fold CV): majority 0.518; a depth-2 tree on raw one-hot 0.906; LDA(1) + RF in a pipeline 0.972; **`odor` alone 0.985**. | E5 |
| C6b | On the notebook's own 70/30 split, LDA fitted before the split and LDA fitted on training data **both give 1.000** for three forest seeds: on this dataset the leak is numerically invisible. | E1, E5 |
| C7 | The "regression" importance models in N03 see a target taking only the values {0, 1}. | M12 |
| C8 | Exam data A = (2, 3, 5, 7, 60): arithmetic mean 15.400, geometric mean 6.608, harmonic mean 4.192. | Key for the retained item type |

## 6. How to reproduce

The notebooks are not public. The lecturer, or anyone given copies, can rerun the audit as follows. Run each command from the repository root.

Create an environment with the mode-C pins:

```bash
uv venv -p 3.12 .audit-env
```

```bash
. .audit-env/bin/activate
```

```bash
uv pip install "numpy<2.3" "pandas>=2.2,<2.3" "scikit-learn==1.6.1" "matplotlib>=3.10,<3.11" "statsmodels>=0.14,<0.15" "networkx>=3.4,<3.5" "imbalanced-learn==0.14.0" "seaborn==0.13.2" scipy tensorflow-cpu nbclient nbformat ipykernel
```

Register the kernel the runner uses:

```bash
python -m ipykernel install --user --name colabera312
```

Run one notebook in mode C (Drive stub on the path; data copies under `/content` as described in §2):

```bash
PYTHONPATH=tools/audit/colabstub AUDIT_KERNEL=colabera312 MPLBACKEND=Agg python tools/audit/runnb.py "path/to/PCAinAction.ipynb" out/PCAinAction.ipynb /content C
```

The runner writes the executed notebook and a `.report.json` file next to it. `tools/audit/compare.py <original.ipynb> <executed.ipynb>` produces the §4 comparison. `tools/audit/checks.py <data-dir>` produces §5; it expects `AirQualityUCI.csv` under `<data-dir>/drive/MyDrive/Colab Notebooks/ExampleData/`, and `train.csv` and `mushrooms.csv` directly in `<data-dir>`.
