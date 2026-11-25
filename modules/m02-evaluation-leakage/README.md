# Module m02 — Evaluation and leakage

| Status | Graded lab | Backlog item | Course CLOs | When |
|---|---|---|---|---|
| **Built** (25 Nov 2026): lecture, Lab 2 with hidden tests, exercises, references, execution report | **Yes — graded lab G1** (includes an AI-audit task) | B06 | CLO2, CLO3 | see the [schedule](../../course/schedule.md) |

**Workspace:** Google Colab (open the lab with the badge below); a pinned local environment is the fallback.

| Material | Link |
|---|---|
| **Lecture slides** (for projection; match the outline section for section) | m02 lecture deck (link added when published) |
| Lecture outline (2 h, with timings and worked examples) | [`lecture/outline.md`](lecture/outline.md) |
| Lab 2 — Evaluation and leakage (**graded lab G1**; run-through in the session, then done as homework and submitted in Teams) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pasdptt/public_teaching_tools4DS/blob/main/modules/m02-evaluation-leakage/lab/lab2_evaluation_leakage.ipynb) [`lab/lab2_evaluation_leakage.ipynb`](lab/lab2_evaluation_leakage.ipynb) |
| Problem set (independent work) | [`exercises/problem-set.md`](exercises/problem-set.md) |
| Misconception checks (in lecture) | [`exercises/misconception-checks.md`](exercises/misconception-checks.md) |
| References (each verified against its DOI record) | [`references.md`](references.md) |
| Execution report | [`EXECUTION-REPORT.md`](EXECUTION-REPORT.md) |

The solution, hidden tests, answer keys and marking notes are kept in the private instructor material.

## Objectives

By the end of this module a student can:

| ID | Objective (observable) | Evidence |
|---|---|---|
| m02-O1 | **Design** a validation scheme (k-fold, grouped, time-ordered or nested) suited to a stated data structure. | Lab 2 T2, Q2; problem set P3 |
| m02-O2 | **Compute** a confidence interval for a test-set accuracy and **interpret** it against a baseline. | Lab 2 T1, Q1; problem set P1–P2 |
| m02-O3 | **Build** `Pipeline`s in which every fitted step is fitted inside the training folds. | Lab 2 T3–T4; problem set P5; midterm item 3 |
| m02-O4 | **Classify** a described leakage by type (preprocessing, target, temporal, group, graph, test-set reuse). | Lab 2 T5, Q5; problem set P4 |
| m02-O5 | **Quantify** leakage on pure-noise data and **explain** why its size depends on whether the step uses $y$. | Lab 2 T3, Q3; problem set P6 |
| m02-O6 | **Fit** resampling for class imbalance (SMOTE) and class weights inside cross-validation, as an example of a fitted operation. | Lab 2 T4, Q4 |

## Lecture (2 h per teaching week)

* Train/validation/test; k-fold, repeated, grouped, time-ordered and nested CV
* Baselines and uncertainty for test metrics (binomial intervals)
* Leakage taxonomy, with examples from the old course notebooks
* Class imbalance only as an example: resampling is a fitted operation (not a standalone topic)

## Lab (3 h per teaching week)

**Graded lab G1 (Lab 2):** a baseline and the Wilson interval; grouped data (KFold vs GroupKFold); leakage on noise (supervised selection vs scaling, before vs inside CV); SMOTE and class weights inside CV with one metric; an AI-audit task (target leakage). Five tasks with self-checks and hidden tests, five written answers.

**Failure analysis (required in every lab):** Q4 (why SMOTE before the split cannot be trusted) and Q5, the **AI-audit task**: an AI-written analysis reports 0.935 accuracy using a column recorded after the diagnosis (honest: 0.663; baseline 0.515).

## Independent work (5 h per teaching week)

Do Lab 2 and submit it (2.5 h); read Kapoor & Narayanan (2023) (1 h); [problem set](exercises/problem-set.md) core items (1 h); project dataset and licence (0.5 h).

## Datasets

| Dataset | Licence status |
|---|---|
| Synthetic grouped patients, noise and a synthetic clinic table (generated in the lab with the course seed) | n/a |
| Digits (registry) | CC BY 4.0 (verified) |

## Existing material to reuse or retire

Issue codes refer to the [evidence audit](../../docs/audit/01-evidence-audit.md).

| Source | Decision |
|---|---|
| Imbalanced notebook (N08) | Merge: keep the correct `imblearn` pipelines (E6); fix the macro- vs micro-F1 comparison and the k selection on the reporting CV (E7) |
| Leakage pattern in FeatureExtraction (N05, LDA fitted before the split) | Used as the motivating case study (E1, check C5) |

## Assessment links

**Graded lab G1**; midterm item 3 (code review).

## Production notes

`imbalanced-learn` is pinned in both environments; the Colab-proxy pin (0.14.x) is an assumption until a real Colab snapshot exists, and the lab installs it if a runtime lacks it. Hidden tests for G1: private repository, `grading/hidden/m02-evaluation-leakage/`.
