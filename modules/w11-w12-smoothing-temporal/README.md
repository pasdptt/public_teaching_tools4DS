# Week 11–12 — Smoothing, aggregation and temporal evaluation

| Status | Backlog item | Course CLOs | Blueprint |
|---|---|---|---|
| **Planned**: structure only; content not yet produced | B13 | CLO2, CLO3, CLO5 | [weekly plan](../../docs/blueprint/03-curriculum-blueprint.md#5-weekly-lecture-and-lab-plan-p) |

## Objectives (draft; finalise when the module is produced)

By the end of this module a student can:

1. **Distinguish** trailing from centred smoothers and **state** which can be used for forecasting.
2. **Fit** exponential smoothing and Holt models with parameters estimated from data.
3. **Apply** kernel (Nadaraya–Watson) and LOESS smoothers and **explain** the bias–variance role of the bandwidth.
4. **Aggregate** irregular records to a regular time grid before modelling.
5. **Evaluate** forecasts with rolling-origin cross-validation against naive and seasonal-naive baselines.
6. **Identify** temporal leakage: full-series scaling, centred windows, look-ahead features.

## Lecture (2 h per week)

* Week 11: smoothers as estimators; MA (trailing vs centred), exponential smoothing, Holt/ETS; kernel and LOESS; bandwidth; aggregation and window functions
* Week 12: rolling-origin evaluation; naive baselines; forecast accuracy measures; temporal leakage; random walk as a process and as a baseline

## Lab (3 h per week)

**L11:** Air Quality with sentinel handling; MA, EWMA and LOESS with a stated bandwidth criterion; aggregation to daily. **L12:** SES and Holt vs naive with rolling-origin CV.

**Failure analysis (required in every lab):** Sentinels treated as data (M15); centred windows used for forecasting; SES on irregular transaction rows (M18); shuffled K-fold on a time series.

## Independent work (5 h per week)

Project method comparison M3 (week 11, 3 h); reading on forecast evaluation (2 h per week).

## Datasets

| Dataset | Licence status |
|---|---|
| Air Quality (registry, SHA-256 verified) | CC BY 4.0 (verified) |

## Existing material to reuse or retire

Issue codes refer to the [evidence audit](../../docs/audit/01-evidence-audit.md).

| Source | Decision |
|---|---|
| smoothing_and_aggregation notebook (N06) | Revise and split: remove 'random walk as smoothing' (M14); sentinel handling (M15); add kernel/LOESS and parameter selection (M16); fix the aliasing bug (M17) |
| SES notebook (N09) | Merge into L12: its data file is missing (D08) and the series is not aggregated (M18) |

## Assessment links

L11, L12; final item 5; **project M3 (method comparison) due in week 11**.

## Production notes

`statsmodels` must be added to both environment pins.
Before this module counts as done, it must meet the [definition of done](../../docs/blueprint/03-curriculum-blueprint.md#91-definition-of-done-applies-to-every-module) and follow the [authoring guide](../../docs/authoring-guide.md).

Planned layout, matching the PCA pilot: `lecture/outline.md`, `lab/labNN_*.ipynb` (built from a private source), `exercises/`, `references.md`, `EXECUTION-REPORT.md`.
