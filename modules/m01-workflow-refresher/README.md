# Module m01 — Reproducible Colab workflow, statistical computing refresher and SQL

| Status | Graded lab | Backlog item | Course CLOs | When |
|---|---|---|---|---|
| **Planned**: structure only; content not yet produced | No (practice; includes an AI-audit task) | B07 | CLO2, CLO5, CLO7 | see the [schedule](../../course/schedule.md) |

## Objectives (draft; finalise when the module is produced)

By the end of this module a student can:

1. **Open** a course notebook from GitHub in Colab, run the setup cell and **interpret** the environment check.
2. **Produce** a notebook that passes *Restart and run all*, and **repair** one that only works because of hidden state.
3. **Load** a dataset through the course registry and **report** its licence and citation.
4. **Compute** and **choose** between arithmetic, geometric and harmonic means; **compute** the sample variance with the correct `ddof`.
5. **Detect** and **recode** sentinel missing-value codes before summarising.
6. **Write** SQL aggregations and window functions (DuckDB) that **reproduce** the corresponding pandas results.
7. **Audit** a short AI-generated code cell: **identify** an error and **verify** the fix with a test.

## Lecture (2 h per teaching week)

* Course design, outcomes, assessment and AI policy
* Notebooks as documents: execution order, hidden state, seeds, environments (why the old notebooks broke, audit §1.5)
* Data provenance and licences; the `tsds` registry
* Means, variance and `ddof`; missing values and sentinel codes; floating-point error
* SQL for statisticians in DuckDB: `GROUP BY`, window functions
* AI-assisted coding: verification practices and the disclosure log

## Lab (3 h per teaching week)

**Lab 1 (practice):** open from GitHub in Colab, run the setup cell, restart and run all; Air Quality data audit in pandas and DuckDB SQL.

**Failure analysis (required in every lab):** The −200 sentinel treated as data (minimum temperature −200 °C, audit M15); an out-of-order notebook (audit S2). **AI-audit task:** find the error in an instructor-supplied AI-generated cell.

## Independent work (5 h per teaching week)

Python and statistics self-check (2 h); SQL practice (1.5 h); read the AI policy and Rule et al. (2019) (1.5 h).

## Datasets

| Dataset | Licence status |
|---|---|
| Air Quality (UCI 360, registry `air_quality`, SHA-256 verified) | CC BY 4.0 (verified) |

## Existing material to reuse or retire

Issue codes refer to the [evidence audit](../../docs/audit/01-evidence-audit.md).

| Source | Decision |
|---|---|
| Lecture 0 and General presentation slides (S08, S09) | Retire: unfilled templates (P3) |
| Review: Python and Review: Python II notebooks (N01, N02) | Revise and merge: fix curly-quote errors (P6, S7); keep the `ddof` and NaN content |
| Final-exam item on means (S02 Q1) | Kept as an item type (key: AM 15.400, GM 6.608, HM 4.192) |

## Assessment links

Practice lab (not graded); midterm item 1.

## Production notes

Add `duckdb` to both environment pins.
Before this module counts as done, it must meet the [definition of done](../../docs/blueprint/03-curriculum-blueprint.md#91-definition-of-done-applies-to-every-module) and follow the [authoring guide](../../docs/authoring-guide.md).

Planned layout, matching the PCA pilot (`m04-pca`): `lecture/outline.md`, `lab/lab<module><part>_*.ipynb` (built from a private source), `exercises/`, `references.md`, `EXECUTION-REPORT.md`.
