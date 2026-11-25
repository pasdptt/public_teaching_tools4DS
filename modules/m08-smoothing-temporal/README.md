# Module m08 — Smoothing, aggregation and temporal evaluation (one teaching week)

| Status | Graded lab | Backlog item | Course CLOs | When |
|---|---|---|---|---|
| **Built** (25 Nov 2026): lecture, Lab 8 with hidden tests, exercises, references, execution report | **Yes — graded lab G5** (includes an AI-audit task) | B13 | CLO2, CLO3, CLO5 | see the [schedule](../../course/schedule.md) |

**Workspace:** Google Colab (open the lab with the badge below); a pinned local environment is the fallback.

| Material | Link |
|---|---|
| **Lecture slides** (23 slides, for projection; match the outline section for section) | [m08 lecture deck](https://claude.ai/artifact/H7ZhEaMiQzZBQua2Lc1YPj) |
| Lecture outline (2 h, with timings and worked examples) | [`lecture/outline.md`](lecture/outline.md) |
| Lab 8 — Smoothing, aggregation and temporal evaluation (**graded lab G5**, with an AI-audit task; run-through in the session, then done as homework and submitted in Teams) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pasdptt/public_teaching_tools4DS/blob/main/modules/m08-smoothing-temporal/lab/lab8_smoothing_temporal.ipynb) [`lab/lab8_smoothing_temporal.ipynb`](lab/lab8_smoothing_temporal.ipynb) |
| Problem set (independent work; final-exam practice) | [`exercises/problem-set.md`](exercises/problem-set.md) |
| Misconception checks (in lecture) | [`exercises/misconception-checks.md`](exercises/misconception-checks.md) |
| References (each verified against its DOI record) | [`references.md`](references.md) |
| Execution report | [`EXECUTION-REPORT.md`](EXECUTION-REPORT.md) |

The solution, hidden tests, answer keys and marking notes are kept in the private instructor material.

## Objectives

By the end of this module a student can:

| ID | Objective (observable) | Evidence |
|---|---|---|
| m08-O1 | **Distinguish** trailing from centred smoothers and **state** which can be used for forecasting. | Lab 8 T2, Q1; problem set P2 |
| m08-O2 | **Fit** exponential smoothing and Holt–Winters models with parameters estimated from data. | Lab 8 T3, Q2; problem set P1 |
| m08-O3 | **Apply** a kernel or LOESS smoother and **choose** its bandwidth by a stated criterion, explaining the bias–variance role. | Lab 8 T2, Q1; problem set P5 |
| m08-O4 | **Aggregate** irregular records to a regular time grid, with sentinel handling and a coverage rule, before modelling. | Lab 8 T1, Q4 |
| m08-O5 | **Evaluate** forecasts with rolling-origin validation against naive baselines and **identify** temporal leakage. | Lab 8 T3–T4, Q2–Q3; problem set P3–P4; final item 5 |

## Lecture (2 h per teaching week)

* Data before smoothing: sentinels; a regular grid with a coverage rule
* Smoothers as estimators: trailing vs centred MA, EWMA, kernel and LOESS; bandwidth and how to choose it
* SES, Holt and Holt–Winters with estimated parameters
* Rolling-origin evaluation; naive baselines; MAE, RMSE, MASE; the random walk as a process and baseline; temporal leakage

## Lab (3 h per teaching week)

**Graded lab G5 (Lab 8):** Air Quality, benzene: sentinels recoded and hourly records aggregated to daily means with an 18-hour coverage rule; trailing and centred means; a Gaussian kernel smoother with its bandwidth chosen by leave-one-out and by leave-a-week-out; naive, seasonal naive, SES and weekly Holt–Winters compared by rolling origin. Four tasks with self-checks and hidden tests, four written answers.

**Failure analysis (required in every lab):** sentinels treated as data (audit M15: an EWMA of temperature at −199.9 °C); exponential smoothing on irregular rows (M18). **AI-audit task:** an AI-generated forecast evaluation with a same-day predictor, a centred window and shuffled K-fold (MAE 0.535 vs an honest 2.552).

## Independent work (5 h per teaching week)

Lab 8 and submit it (2 h); reading on forecast evaluation and the problem set (1 h); **project M3** method comparison (2 h).

## Datasets

| Dataset | Licence status |
|---|---|
| Air Quality (registry, SHA-256 verified) | CC BY 4.0 (verified) |

## Existing material to reuse or retire

Issue codes refer to the [evidence audit](../../docs/audit/01-evidence-audit.md).

| Source | Decision |
|---|---|
| smoothing_and_aggregation notebook (N06) | Revised: 'random walk as smoothing' removed (M14); sentinels recoded (M15); kernel smoothing and a bandwidth criterion added (M16); the aliasing code dropped (M17) |
| SES notebook (N09) | Merged: its data file is missing (D08); SES is now fitted to a regular daily series with α estimated (M18) |

## Assessment links

**Graded lab G5**; final item 5; **project M3 due** this week.

## Production notes

`statsmodels` is pinned in both environments (preinstalled in Colab). Hidden tests for G5: private repository, `grading/hidden/m08-smoothing-temporal/`.
