# Module m03 — Dimension reduction I: feature selection vs feature extraction

| Status | Graded lab | Backlog item | Course CLOs | When |
|---|---|---|---|---|
| **Planned**: structure only; content not yet produced | No (practice) | B08 | CLO2, CLO3 | see the [schedule](../../course/schedule.md) |

## Objectives (draft; finalise when the module is produced)

By the end of this module a student can:

1. **Distinguish** feature selection (a subset of the original variables) from feature extraction (new variables) and **state** the consequences for interpretation.
2. **Apply** filter, wrapper and embedded selection inside cross-validation.
3. **Measure** the stability of the selected set across folds.
4. **Compute** permutation importance on held-out data and **contrast** it with impurity-based importance.
5. **Compare** every selection against an all-features baseline with uncertainty.

## Lecture (2 h per teaching week)

* The curse of dimensionality
* Filter, wrapper and embedded selection; selection inside CV
* Stability of selection
* Importance measures: coefficients (scaling and collinearity), impurity, permutation on held-out data

## Lab (3 h per teaching week)

**Lab 3 (practice):** RFE and `SelectKBest` in pipelines on Wine against an all-features baseline; stability of selected sets across folds.

**Failure analysis (required in every lab):** Selection outside CV on high-dimensional noise; impurity importance fitted to the wrong target (the bug in the old notebook, audit M12).

## Independent work (5 h per teaching week)

Selection exercises (2 h); **project proposal M1** (3 h).

## Datasets

| Dataset | Licence status |
|---|---|
| Wine (registry) | CC BY 4.0 (verified) |
| Synthetic high-dimensional noise | n/a |

## Existing material to reuse or retire

Issue codes refer to the [evidence audit](../../docs/audit/01-evidence-audit.md).

| Source | Decision |
|---|---|
| Dimensionality Reductions notebook (N03) | Revise: keep RFE in `Pipeline` with repeated CV (E6); fix the mislabelled regression importances and the training-data permutation importance (M12); add scaling and collinearity (M13); replace synthetic-only data |

## Assessment links

Practice lab; **project M1 (proposal) due** this week.

## Production notes

No additional dependencies expected.
Before this module counts as done, it must meet the [definition of done](../../docs/blueprint/03-curriculum-blueprint.md#91-definition-of-done-applies-to-every-module) and follow the [authoring guide](../../docs/authoring-guide.md).

Planned layout, matching the PCA pilot (`m04-pca`): `lecture/outline.md`, `lab/lab<module><part>_*.ipynb` (built from a private source), `exercises/`, `references.md`, `EXECUTION-REPORT.md`.
