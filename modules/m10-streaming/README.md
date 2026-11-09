# Module m10 — Streaming algorithms

| Status | Graded lab | Backlog item | Course CLOs | When |
|---|---|---|---|---|
| **Planned**: structure only; content not yet produced | **Yes — graded lab G6** (streaming plus an HPC benchmark task) | B15 | CLO5, CLO6 | see the [schedule](../../course/schedule.md) |

## Objectives (draft; finalise when the module is produced)

By the end of this module a student can:

1. **State** the one-pass model and its memory bound.
2. **Implement** Welford's online mean and variance and **demonstrate** its stability against the naive formula.
3. **Prove** that reservoir sampling is uniform and **confirm** it by simulation.
4. **Implement** Count-Min sketch and HyperLogLog and **compare** their error with exact answers across memory budgets.
5. **Use** EWMA as a streaming smoother and `IncrementalPCA` on a stream, with a simple drift check.

## Lecture (2 h per teaching week)

* One-pass model; memory bounds
* Welford (1962); reservoir sampling (Vitter 1985)
* Count-Min sketch (ε, δ guarantees); HyperLogLog (relative error ≈ 1.04/√m)
* Streaming smoothing and incremental PCA; concept drift

## Lab (3 h per teaching week)

**Graded lab G6:** replay Air Quality as a stream; compare sketches with exact answers across memory budgets; one timed HPC benchmark task from module m09.

**Failure analysis (required in every lab):** Catastrophic cancellation in the naive variance; a biased 'keep the first n' sample.

## Independent work (5 h per teaching week)

**Project M4** final report and repository (5 h).

## Datasets

| Dataset | Licence status |
|---|---|
| Air Quality replayed as a stream (registry) | CC BY 4.0 (verified) |
| Synthetic streams (seeded) | n/a |

## Existing material to reuse or retire

Issue codes refer to the [evidence audit](../../docs/audit/01-evidence-audit.md).

| Source | Decision |
|---|---|
| — none found (audit C2) | New content |

## Assessment links

**Graded lab G6**; final item 6; **project M4 due** at the end of this week.

## Production notes

No additional dependencies expected.
Before this module counts as done, it must meet the [definition of done](../../docs/blueprint/03-curriculum-blueprint.md#91-definition-of-done-applies-to-every-module) and follow the [authoring guide](../../docs/authoring-guide.md).

Planned layout, matching the PCA pilot (`m04-pca`): `lecture/outline.md`, `lab/lab<module><part>_*.ipynb` (built from a private source), `exercises/`, `references.md`, `EXECUTION-REPORT.md`.
