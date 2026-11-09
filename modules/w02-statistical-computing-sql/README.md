# Week 2 — Statistical computing refresher with Python and SQL

| Status | Backlog item | Course CLOs | Blueprint |
|---|---|---|---|
| **Planned**: structure only; content not yet produced | B07 | CLO2, CLO5 | [weekly plan](../../docs/blueprint/03-curriculum-blueprint.md#5-weekly-lecture-and-lab-plan-p) |

## Objectives (draft; finalise when the module is produced)

By the end of this module a student can:

1. **Compute** and **choose** between arithmetic, geometric and harmonic means for a stated purpose.
2. **Compute** the sample variance with the correct divisor and **explain** the role of `ddof`.
3. **Detect** and **recode** sentinel missing-value codes before summarising or smoothing.
4. **Write** SQL aggregations and window functions (DuckDB) that **reproduce** the corresponding pandas results.
5. **Demonstrate** catastrophic cancellation in the naive variance formula.

## Lecture (2 h per week)

* Means and when each is meaningful; variance and `ddof`; robust summaries
* Missing data and sentinel codes
* Floating-point arithmetic and numerically stable formulas
* SQL for statisticians: `GROUP BY`, window functions (DuckDB in Colab)

## Lab (3 h per week)

**L2 Data audit:** Air Quality in pandas and DuckDB SQL; summaries before and after recoding the sentinel; matching SQL and pandas results.

**Failure analysis (required in every lab):** The −200 sentinel treated as data: the minimum temperature becomes −200 °C and an exponential moving average reaches −195 °C (audit M15, check C2).

## Independent work (5 h per week)

Summary-statistics exercises (2 h); SQL practice (2 h); revision of matrix algebra for week 5 (1 h).

## Datasets

| Dataset | Licence status |
|---|---|
| Air Quality (UCI 360, registry `air_quality`, SHA-256 verified) | CC BY 4.0 (verified) |

## Existing material to reuse or retire

Issue codes refer to the [evidence audit](../../docs/audit/01-evidence-audit.md).

| Source | Decision |
|---|---|
| Review: Python and Review: Python II notebooks (N01, N02) | Revise and merge: fix curly-quote errors (P6, S7); keep the `ddof` and NaN content |
| Final-exam item on means (S02 Q1) | Kept as an item type (key: AM 15.400, GM 6.608, HM 4.192) |

## Assessment links

L2 (lab rubric); midterm item 1.

## Production notes

Add `duckdb` to both environment pins before building this lab.
Before this module counts as done, it must meet the [definition of done](../../docs/blueprint/03-curriculum-blueprint.md#91-definition-of-done-applies-to-every-module) and follow the [authoring guide](../../docs/authoring-guide.md).

Planned layout, matching the PCA pilot: `lecture/outline.md`, `lab/labNN_*.ipynb` (built from a private source), `exercises/`, `references.md`, `EXECUTION-REPORT.md`.
