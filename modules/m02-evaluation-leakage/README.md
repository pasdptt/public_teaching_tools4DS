# Module m02 — Evaluation and leakage

| Status | Graded lab | Backlog item | Course CLOs | When |
|---|---|---|---|---|
| **Planned**: structure only; content not yet produced | **Yes — graded lab G1** (includes an AI-audit task) | B06 | CLO2, CLO3 | see the [schedule](../../course/schedule.md) |

## Objectives (draft; finalise when the module is produced)

By the end of this module a student can:

1. **Design** a validation scheme (k-fold, grouped, time-ordered or nested) suited to a stated data structure.
2. **Compute** a confidence interval for a test-set accuracy and **interpret** it against a baseline.
3. **Build** `Pipeline`s in which every fitted step is fitted inside the training folds.
4. **Classify** a described leakage by type (preprocessing, target, temporal, group, graph).
5. **Quantify** leakage on pure-noise data and **explain** why its size depends on whether the step uses $y$.
6. **Fit** resampling for class imbalance (SMOTE, undersampling) and class weights inside cross-validation, as an example of a fitted operation.

## Lecture (2 h per teaching week)

* Train/validation/test; k-fold, repeated, grouped, time-ordered and nested CV
* Baselines and uncertainty for test metrics (binomial intervals)
* Leakage taxonomy, with examples from the old course notebooks
* Class imbalance only as an example: resampling is a fitted operation (not a standalone topic)

## Lab (3 h per teaching week)

**Graded lab G1:** supervised selection before vs inside CV on noise; SMOTE vs class weights inside CV with consistent metrics.

**Failure analysis (required in every lab):** **AI-audit task:** find the leakage in an instructor-supplied, AI-generated notebook.

## Independent work (5 h per teaching week)

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

**Graded lab G1**; midterm item 3 (code review).

## Production notes

Add `imbalanced-learn` to both environment pins. Graded labs need hidden auto-check tests (backlog B19).
Before this module counts as done, it must meet the [definition of done](../../docs/blueprint/03-curriculum-blueprint.md#91-definition-of-done-applies-to-every-module) and follow the [authoring guide](../../docs/authoring-guide.md).

Planned layout, matching the PCA pilot (`m04-pca`): `lecture/outline.md`, `lab/lab<module><part>_*.ipynb` (built from a private source), `exercises/`, `references.md`, `EXECUTION-REPORT.md`.
