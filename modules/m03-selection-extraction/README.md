# Module m03 — Dimension reduction I: feature selection vs feature extraction

| Status | Graded lab | Backlog item | Course CLOs | When |
|---|---|---|---|---|
| **Built** (25 Nov 2026): lecture, Lab 3, exercises, references, execution report | No (practice) | B08 | CLO2, CLO3 | see the [schedule](../../course/schedule.md) |

**Workspace:** Google Colab (open the lab with the badge below); a pinned local environment is the fallback.

| Material | Link |
|---|---|
| **Lecture slides** (for projection; match the outline section for section) | m03 lecture deck (link added when published) |
| Lecture outline (2 h, with timings and worked examples) | [`lecture/outline.md`](lecture/outline.md) |
| Lab 3 — Feature selection vs feature extraction (3 h guided run-through, then redone as homework; practice) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pasdptt/public_teaching_tools4DS/blob/main/modules/m03-selection-extraction/lab/lab3_selection_extraction.ipynb) [`lab/lab3_selection_extraction.ipynb`](lab/lab3_selection_extraction.ipynb) |
| Problem set (independent work) | [`exercises/problem-set.md`](exercises/problem-set.md) |
| Misconception checks (in lecture) | [`exercises/misconception-checks.md`](exercises/misconception-checks.md) |
| References (each verified against its DOI record) | [`references.md`](references.md) |
| Execution report | [`EXECUTION-REPORT.md`](EXECUTION-REPORT.md) |

The solution, answer keys and marking notes are kept in the private instructor material.

## Objectives

By the end of this module a student can:

| ID | Objective (observable) | Evidence |
|---|---|---|
| m03-O1 | **Show** how distances lose contrast as dimension grows, and **explain** the consequence for distance-based methods. | Lab 3 T1, Q1; problem set P1 |
| m03-O2 | **Distinguish** feature selection from feature extraction and **state** the consequences for interpretation and measurement cost. | Lab 3 Q2; problem set P2 |
| m03-O3 | **Apply** filter, wrapper and embedded selection inside cross-validation. | Lab 3 T2; problem set P6 |
| m03-O4 | **Measure** the stability of the selected set across folds (selection frequency, Jaccard). | Lab 3 T3, Q3; problem set P3 |
| m03-O5 | **Compute** permutation importance on held-out data and **contrast** it with impurity importance. | Lab 3 T4–T5, Q4; problem set P5, P7 |
| m03-O6 | **Compare** every reduction against an all-features baseline with uncertainty. | Lab 3 T2, Q2 |

## Lecture (2 h per teaching week)

* The curse of dimensionality
* Filter, wrapper and embedded selection; selection inside CV
* Stability of selection
* Importance measures: coefficients (scaling and collinearity), impurity, permutation on held-out data

## Lab (3 h per teaching week)

**Lab 3 (practice):** distance contrast; `SelectKBest`, RFE and PCA in pipelines on Wine against an all-features and a majority baseline; stability of selected sets across 25 folds; impurity vs permutation importance on a synthetic problem with a known answer. Five tasks with self-checks, four written answers.

**Failure analysis (required in every lab):** permutation importance computed on the training data (the old notebook's bug, audit M12): pure noise looks important (0.281) because the forest memorised it; on test data it is 0.000.

## Independent work (5 h per teaching week)

Redo Lab 3 and submit it (1.5 h); [problem set](exercises/problem-set.md) core items (1 h); **project proposal M1** (2.5 h).

## Datasets

| Dataset | Licence status |
|---|---|
| Wine (registry) | CC BY 4.0 (verified) |
| Synthetic random points and a signal-and-noise table (generated in the lab with the course seed) | n/a |

## Existing material to reuse or retire

Issue codes refer to the [evidence audit](../../docs/audit/01-evidence-audit.md).

| Source | Decision |
|---|---|
| Dimensionality Reductions notebook (N03) | Revise: keep RFE in `Pipeline` with repeated CV (E6); fix the mislabelled regression importances and the training-data permutation importance (M12); add scaling and collinearity (M13); replace synthetic-only data |

## Assessment links

Practice lab; **project M1 (proposal) due** this week.

## Production notes

No additional dependencies.
