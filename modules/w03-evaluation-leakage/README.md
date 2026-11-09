# Week 3 — Evaluation and leakage

| Status | Backlog item | Course CLOs | Blueprint |
|---|---|---|---|
| **Planned**: structure only; content not yet produced | B06 | CLO2, CLO3 | [weekly plan](../../docs/blueprint/03-curriculum-blueprint.md#5-weekly-lecture-and-lab-plan-p) |

## Objectives (draft; finalise when the module is produced)

By the end of this module a student can:

1. **Design** a validation scheme (k-fold, grouped, time-ordered or nested) suited to a stated data structure.
2. **Compute** a confidence interval for a test-set accuracy and **interpret** it against a baseline.
3. **Build** `Pipeline`s in which every fitted step is fitted inside the training folds.
4. **Classify** a described leakage by type (preprocessing, target, temporal, group, graph).
5. **Quantify** leakage on pure-noise data and **explain** why its size depends on whether the step uses $y$.
6. **Fit** resampling for class imbalance (SMOTE, undersampling) and class weights inside cross-validation.

## Lecture (2 h per week)

* Train/validation/test; k-fold, repeated, grouped, time-ordered and nested CV
* Baselines and uncertainty for test metrics (binomial intervals)
* Leakage taxonomy, with examples from the old course notebooks
* Class imbalance: resampling as a fitted operation; consistent metrics (PR-AUC, macro-F1)

## Lab (3 h per week)

**L3 Leakage lab:** supervised selection before vs inside CV on noise (0.91 vs 0.52 in the PCA pilot); SMOTE vs class weights inside CV with consistent metrics.

**Failure analysis (required in every lab):** Find the leakage in an instructor-supplied, AI-generated notebook (the AI-audit task).

## Independent work (5 h per week)

Read Kapoor & Narayanan (2023) (1.5 h); validation-design exercises (2 h); project team formation and dataset search (1.5 h).

## Datasets

| Dataset | Licence status |
|---|---|
| Synthetic noise and `make_classification` | n/a |
| Digits (registry) | CC BY 4.0 (verified) |

## Existing material to reuse or retire

Issue codes refer to the [evidence audit](../../docs/audit/01-evidence-audit.md).

| Source | Decision |
|---|---|
| Imbalanced notebook (N08) | Merge: keep the correct `imblearn` pipelines (E6); fix the macro- vs micro-F1 comparison and the k selection on the reporting CV (E7) |
| Leakage pattern in FeatureExtraction (N05, LDA fitted before the split) | Used as the motivating case study (E1, check C5) |

## Assessment links

L3; midterm item 3 (code review); project M2.

## Production notes

Add `imbalanced-learn` to both environment pins.
Before this module counts as done, it must meet the [definition of done](../../docs/blueprint/03-curriculum-blueprint.md#91-definition-of-done-applies-to-every-module) and follow the [authoring guide](../../docs/authoring-guide.md).

Planned layout, matching the PCA pilot: `lecture/outline.md`, `lab/labNN_*.ipynb` (built from a private source), `exercises/`, `references.md`, `EXECUTION-REPORT.md`.
