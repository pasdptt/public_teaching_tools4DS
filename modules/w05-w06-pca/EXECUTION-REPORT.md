# Execution report — PCA pilot module (weeks 5–6)

**Date:** 9 November 2026. Every result below comes from running the code **[V]**.

## 1. Environments

Both environments use Python 3.12.3 and CPU only, and both install the course helper `tsds` from `src/`.

| Environment | Pins | Represents |
|---|---|---|
| `environment/requirements-local.txt` (pinned local) | numpy 2.5.4, pandas 3.1.1, scipy 1.18.1, scikit-learn 1.9.1, Matplotlib 3.11.2, PyYAML 6.0.3 | Latest releases; the local fallback |
| `environment/requirements-colab-proxy.txt` (Colab proxy) | numpy 2.2.6, pandas 2.2.3, scipy 1.16.3, scikit-learn 1.6.1, Matplotlib 3.10.9, PyYAML 6.0.3 | The Colab-era package set inferred during the audit. **It is a proxy, not a real Colab snapshot**; Colab was not reachable from the build machine. |

**To reproduce:**

```bash
uv venv -p 3.12 .venv-local
```

```bash
uv pip install -p .venv-local/bin/python -r environment/requirements-local.txt -e src
```

```bash
.venv-local/bin/python -m ipykernel install --user --name python3
```

```bash
.venv-local/bin/python -m pytest -q tests
```

## 2. Test results

| Test | Pinned local | Colab proxy |
|---|---|---|
| Student notebooks: structure (badge, setup cell, no outputs, no solution text, task cells raise `NotImplementedError`) | 2/2 pass | 2/2 pass |
| Student notebooks: all given code runs top to bottom in a fresh kernel (task and check cells removed) | 2/2 pass (Lab 05 2.7 s, Lab 06 3.4 s) | 2/2 pass (2.4 s, 3.0 s) |
| Instructor solutions: identical task/check/answer IDs to the student notebooks, every self-check passes, strictly top-to-bottom execution | 2/2 pass (Lab 05 3.0 s, **Lab 06 55–59 s**) | 2/2 pass (2.6 s, 43–44 s) |
| Public-only run (no instructor material, as in public CI) | 4 pass, 2 skipped by design | — |

**Runtime.** The slowest notebook (Lab 06, mostly the nested CV and 20 × 4 repeated CVs) completes in under one minute on the 4-core build machine. That is well inside the 10-minute budget of blueprint §8.2. **[A]** Colab's free CPU runtime may be 2–4 times slower; this has not been measured.

## 3. Reproducibility across environments

Text outputs of the executed solutions were compared between the two environments. The setup cell's version printout is excluded because it differs by design.

| Notebook | Identical outputs | Different |
|---|---|---|
| Lab 05 | 14 | 1: the `np.linalg.eig` demonstration returns `complex128` under numpy 2.5.4 and `float64` under numpy 2.2.6. This is **intended**: it is the version-dependence that failure 2 teaches. |
| Lab 06 | 14 | 0 |

Every number quoted in `lecture/outline.md` and in the model answers matches the executed solutions.

**One reproducibility defect was found and fixed during the build.** For wide data, scikit-learn's `PCA` switches automatically to a randomised solver. In the leakage experiment it was unseeded, giving 0.488 in one run and 0.485 in another. All `PCA` calls on wide data now pass `random_state`, and the lecture outline documents this as a teaching point.

## 4. Do the self-checks catch wrong answers? (mutation testing)

Ten typical student mistakes were injected into the solutions; each targeted self-check must fail.

| Lab | Task | Injected mistake | Result |
|---|---|---|---|
| 05 | T1.1 | Divisor $n$ instead of $n-1$ | caught |
| 05 | T1.2 | Eigenvalues left in ascending order | caught |
| 05 | T2 | SVD of uncentred data | caught (**initially missed**: the check only used already-centred data; a raw-data check was added) |
| 05 | T3 | Off-by-one in the discarded eigenvalues | caught |
| 05 | T4 | "Covariance" PCA run on standardised data | caught |
| 06 | T1 | Unseeded permutations | caught |
| 06 | T2 | k tuned on the outer split | caught |
| 06 | T3 | Supervised step placed inside the pipeline for the "before" case | caught |
| 06 | T4 | LDA replaced by PCA | caught |
| 06 | T5 | Angle depends on the component's sign | caught |

**Result: 10 of 10 caught.** The self-checks test consistency, not interpretation; written answers carry half of each lab's marks.

## 5. Acceptance criteria (brief and blueprint §9.1)

| Criterion | Status |
|---|---|
| Runs from a clean, documented environment | **Met**, in both pinned environments (§1–2). The **first-run install path** was also tested: a fresh Colab-proxy environment *without* `tsds` executed both student notebooks' setup cells, which installed `tsds` 0.1.0 from GitHub (with `COURSE_REF` set to the pushed branch for the test), and all given code ran. **Not verified on Colab itself**: Colab is unreachable from the build machine, and the `main`-branch badge links and the default `COURSE_REF = "main"` work only after merging. |
| Accessible, appropriately licensed data | **Met.** Wine (UCI 109) and Digits (UCI 80) are bundled with scikit-learn and CC BY 4.0, verified on the UCI pages; the rest is synthetic. No Drive, Kaggle or network access is needed to run the labs. |
| No hidden notebook state | **Met.** Student notebooks are committed without outputs; solutions are tested for strictly sequential execution. |
| Demonstrates valid evaluation | **Met.** Nested CV, a fixed shared split, baselines (majority class and all features), uncertainty reported as fold standard deviation, and a leakage experiment. |
| Instructor solutions consistent with the questions | **Met.** Student and solution notebooks are built from one source; IDs are tested; all self-checks pass; mutation tests pass. |
| Verified references | **Met.** All 17 DOIs were checked against Crossref (§6). |
| Lab fits 3 hours | **Not yet verified.** It needs a pilot with a teaching assistant or students. |

## 6. Reference verification (Crossref)

All 17 entries in `references.md` resolved on `api.crossref.org` (9 Nov 2026). Authors, year, title, venue, volume, issue and pages matched, apart from the two documented deviations:

* the Cadima & Jolliffe (1995) title is mistyped in Crossref's metadata;
* Crossref lists no author for the Jolliffe (2002) book record.
