# Week 13 — High-performance computing on a laptop

| Status | Backlog item | Course CLOs | Blueprint |
|---|---|---|---|
| **Planned**: structure only; content not yet produced | B14 | CLO6 | [weekly plan](../../docs/blueprint/03-curriculum-blueprint.md#5-weekly-lecture-and-lab-plan-p) |

## Objectives (draft; finalise when the module is produced)

By the end of this module a student can:

1. **Profile** the time and memory of an analysis and **locate** the bottleneck.
2. **Speed up** a statistic by vectorisation and JIT compilation (Numba), reporting the measured speed-up.
3. **Parallelise** cross-validation with `joblib` and **explain** when parallelism slows things down.
4. **Process** data larger than comfortable memory with chunked or out-of-core tools (Parquet and DuckDB).
5. **Quantify** the accuracy–time trade-off of randomised SVD and `IncrementalPCA`.

## Lecture (2 h per week)

* Complexity and profiling (time, memory)
* Vectorisation, memory layout, Numba
* Parallel CV with joblib; overheads
* Out-of-core analytics: Parquet and DuckDB
* Randomised and incremental PCA (Halko et al. 2011); Spark only as an optional appendix

## Lab (3 h per week)

**L13:** loop vs vectorised vs Numba benchmark; out-of-core aggregation of a deterministic synthetic table; randomised vs full SVD error and time.

**Failure analysis (required in every lab):** Memory blow-up from naive `read_csv`; a parallelism slowdown on small tasks.

## Independent work (5 h per week)

Project integration (5 h).

## Datasets

| Dataset | Licence status |
|---|---|
| Deterministic synthetic 'large' table (generated) | n/a |
| nycflights13 `flights` | **Licence to verify** |

## Existing material to reuse or retire

Issue codes refer to the [evidence audit](../../docs/audit/01-evidence-audit.md).

| Source | Decision |
|---|---|
| PCA on spark notebook (N10) | Retire as required work (belongs to 040563105, fragile installer, S4); optional appendix only |

## Assessment links

L13; final item 6.

## Production notes

Add `duckdb`, `pyarrow` and `numba` to both environment pins; check the free Colab memory limit.
Before this module counts as done, it must meet the [definition of done](../../docs/blueprint/03-curriculum-blueprint.md#91-definition-of-done-applies-to-every-module) and follow the [authoring guide](../../docs/authoring-guide.md).

Planned layout, matching the PCA pilot: `lecture/outline.md`, `lab/labNN_*.ipynb` (built from a private source), `exercises/`, `references.md`, `EXECUTION-REPORT.md`.
