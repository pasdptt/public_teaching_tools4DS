# Week 14 — Streaming algorithms

| Status | Backlog item | Course CLOs | Blueprint |
|---|---|---|---|
| **Planned**: structure only; content not yet produced | B15 | CLO5, CLO6 | [weekly plan](../../docs/blueprint/03-curriculum-blueprint.md#5-weekly-lecture-and-lab-plan-p) |

## Objectives (draft; finalise when the module is produced)

By the end of this module a student can:

1. **State** the one-pass model and its memory bound.
2. **Implement** Welford's online mean and variance and **demonstrate** its stability against the naive formula.
3. **Prove** that reservoir sampling is uniform and **confirm** it by simulation.
4. **Implement** Count-Min sketch and HyperLogLog and **compare** their error with exact answers across memory budgets.
5. **Use** EWMA as a streaming smoother and `IncrementalPCA` on a stream, with a simple drift check.

## Lecture (2 h per week)

* One-pass model; memory bounds
* Welford (1962); reservoir sampling (Vitter 1985)
* Count-Min sketch (ε, δ guarantees); HyperLogLog (relative error ≈ 1.04/√m)
* Streaming smoothing and incremental PCA; concept drift

## Lab (3 h per week)

**L14:** replay Air Quality as a stream; compare sketches with exact answers across memory budgets.

**Failure analysis (required in every lab):** Catastrophic cancellation in the naive variance; a biased 'keep the first n' sample.

## Independent work (5 h per week)

Final report drafting (5 h).

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

L14; final item 6.

## Production notes

No additional dependencies expected.
Before this module counts as done, it must meet the [definition of done](../../docs/blueprint/03-curriculum-blueprint.md#91-definition-of-done-applies-to-every-module) and follow the [authoring guide](../../docs/authoring-guide.md).

Planned layout, matching the PCA pilot: `lecture/outline.md`, `lab/labNN_*.ipynb` (built from a private source), `exercises/`, `references.md`, `EXECUTION-REPORT.md`.
