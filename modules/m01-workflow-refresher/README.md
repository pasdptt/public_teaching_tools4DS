# Module m01 — Reproducible Colab workflow, statistical computing refresher and SQL

| Status | Graded lab | Backlog item | Course CLOs | When |
|---|---|---|---|---|
| **Built** (24 Nov 2026): lecture, Lab 1, exercises, references, execution report | No (practice; includes an AI-audit task) | B07 | CLO2, CLO5, CLO7 | week 1; see the [schedule](../../course/schedule.md) |

**Workspace:** Google Colab (open the lab with the badge below); a pinned local environment is the fallback.

| Material | Link |
|---|---|
| Lecture outline (2 h, with timings and worked examples) | [`lecture/outline.md`](lecture/outline.md) |
| Lab 1 — Reproducible workflow, statistics refresher and SQL (3 h, practice) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pasdptt/public_teaching_tools4DS/blob/main/modules/m01-workflow-refresher/lab/lab1_workflow_refresher.ipynb) [`lab/lab1_workflow_refresher.ipynb`](lab/lab1_workflow_refresher.ipynb) |
| Problem set (independent work) | [`exercises/problem-set.md`](exercises/problem-set.md) |
| Misconception checks (in lecture) | [`exercises/misconception-checks.md`](exercises/misconception-checks.md) |
| References (each verified against its DOI record) | [`references.md`](references.md) |
| Execution report | [`EXECUTION-REPORT.md`](EXECUTION-REPORT.md) |

The Lab 1 solution, the answer keys and the marking notes are kept in the private instructor material.

## Objectives

By the end of this module a student can:

| ID | Objective (observable) | Evidence |
|---|---|---|
| m01-O1 | **Open** a course notebook from GitHub in Colab, run the setup cell and **interpret** the environment check. | Lab 1 Q1 |
| m01-O2 | **Produce** a notebook that passes *Restart and run all*, and **repair** one that only works because of hidden state. | Lab 1 T1, Q2; problem set P7 |
| m01-O3 | **Load** a dataset through the course registry and **report** its licence and citation. | Lab 1 Part 3; project M1 |
| m01-O4 | **Compute** and **choose** between arithmetic, geometric and harmonic means; **compute** the sample standard deviation with the correct `ddof`. | Lab 1 T2, Q3; problem set P1–P5; midterm item 1 |
| m01-O5 | **Detect** and **recode** sentinel missing-value codes before summarising, and report coverage. | Lab 1 T3–T4, Q4 (failure analysis); problem set P4; midterm item 1 |
| m01-O6 | **Write** SQL aggregations and window functions (DuckDB) that **reproduce** the corresponding pandas results. | Lab 1 T5–T6; problem set P8–P12 |
| m01-O7 | **Audit** a short AI-generated code cell: **identify** the error and **prove** the fix with a test. | Lab 1 T7, Q5 |

## Lecture (2 h per teaching week)

* Course design, outcomes, assessment and AI policy
* Notebooks as documents: execution order, hidden state, seeds, environments (why the old notebooks broke, audit §1.5)
* Data provenance and licences; the `tsds` registry
* Means, variance and `ddof`; missing values and sentinel codes; floating-point error
* SQL for statisticians in DuckDB: `GROUP BY`, window functions
* AI-assisted coding: verification practices and the disclosure log

## Lab (3 h per teaching week)

**Lab 1 (practice):** environment check; hidden state; means and `ddof`; Air Quality sentinel audit; the same summaries in pandas and DuckDB SQL; an AI-audit task. Seven tasks with self-checks, five written answers.

**Failure analysis (required in every lab):** the −200 sentinel treated as data (mean temperature 9.78 °C instead of 18.32 °C; audit M15) and an out-of-order notebook (audit S2). **AI-audit task:** an AI-written "daily mean" that groups by day of the month (31 values instead of 391).

## Independent work (5 h per teaching week)

[Problem set](exercises/problem-set.md): statistics refresher (2 h), SQL practice (1.5 h), reading Rule et al. (2019) and the AI policy (1.5 h).

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

`duckdb` is pinned in both environments (`environment/`). The Colab-proxy pin (1.2.x) is an assumption until a real Colab snapshot exists; the lab installs DuckDB itself if a runtime lacks it.
