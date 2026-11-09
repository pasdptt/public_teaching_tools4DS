# Module m08 — Smoothing, aggregation and temporal evaluation (one teaching week)

| Status | Graded lab | Backlog item | Course CLOs | When |
|---|---|---|---|---|
| **Planned**: structure only; content not yet produced | **Yes — graded lab G5** (includes an AI-audit task) | B13 | CLO2, CLO3, CLO5 | see the [schedule](../../course/schedule.md) |

## Objectives (draft; finalise when the module is produced)

By the end of this module a student can:

1. **Distinguish** trailing from centred smoothers and **state** which can be used for forecasting.
2. **Fit** exponential smoothing and Holt models with parameters estimated from data.
3. **Apply** a kernel or LOESS smoother and **explain** the bias–variance role of the bandwidth.
4. **Aggregate** irregular records to a regular time grid before modelling.
5. **Evaluate** forecasts with rolling-origin cross-validation against a naive baseline and **identify** temporal leakage.

## Lecture (2 h per teaching week)

* Smoothers as estimators: MA (trailing vs centred), exponential smoothing and Holt; kernel and LOESS; bandwidth
* Aggregation and window functions
* Rolling-origin evaluation; naive baselines; temporal leakage; random walk as a process and baseline

## Lab (3 h per teaching week)

**Graded lab G5:** Air Quality with sentinel handling, aggregated to daily; MA, EWMA and LOESS with a stated bandwidth criterion; SES and Holt vs naive with rolling-origin CV.

**Failure analysis (required in every lab):** Sentinels treated as data (M15); SES on irregular transaction rows (M18). **AI-audit task:** an AI-generated forecast evaluated with shuffled K-fold and a centred window.

## Independent work (5 h per teaching week)

Reading on forecast evaluation (2 h); **project M3** method comparison (3 h).

## Datasets

| Dataset | Licence status |
|---|---|
| Air Quality (registry, SHA-256 verified) | CC BY 4.0 (verified) |

## Existing material to reuse or retire

Issue codes refer to the [evidence audit](../../docs/audit/01-evidence-audit.md).

| Source | Decision |
|---|---|
| smoothing_and_aggregation notebook (N06) | Revise: remove 'random walk as smoothing' (M14); sentinel handling (M15); add kernel/LOESS and parameter selection (M16); fix the aliasing bug (M17) |
| SES notebook (N09) | Merge: its data file is missing (D08) and the series is not aggregated (M18) |

## Assessment links

**Graded lab G5**; final item 5; **project M3 due** this week.

## Production notes

Add `statsmodels` to both environment pins. The merged week is dense: keep the lecture to the listed topics.
Before this module counts as done, it must meet the [definition of done](../../docs/blueprint/03-curriculum-blueprint.md#91-definition-of-done-applies-to-every-module) and follow the [authoring guide](../../docs/authoring-guide.md).

Planned layout, matching the PCA pilot (`m04-pca`): `lecture/outline.md`, `lab/lab<module><part>_*.ipynb` (built from a private source), `exercises/`, `references.md`, `EXECUTION-REPORT.md`.
