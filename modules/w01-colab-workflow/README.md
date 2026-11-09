# Week 1 — Reproducible Colab workflow and responsible AI-assisted coding

| Status | Backlog item | Course CLOs | Blueprint |
|---|---|---|---|
| **Planned**: structure only; content not yet produced | B07 | CLO2, CLO7 | [weekly plan](../../docs/blueprint/03-curriculum-blueprint.md#5-weekly-lecture-and-lab-plan-p) |

## Objectives (draft; finalise when the module is produced)

By the end of this module a student can:

1. **Open** a course notebook from GitHub in Colab, run the setup cell and **interpret** the environment check.
2. **Demonstrate** hidden notebook state and **produce** a notebook that passes *Restart and run all*.
3. **Load** a dataset through the course registry and **report** its licence and citation.
4. **Audit** a short AI-generated code cell: **identify** an error and **verify** the fix with a test.

## Lecture (2 h per week)

* Course design, outcomes, assessment and AI policy
* Notebooks as documents: execution order, hidden state, seeds
* Environments and versions: why the old course notebooks broke (audit §1.5)
* Data provenance and licences; the `tsds` registry
* AI-assisted coding: verification practices and the disclosure log

## Lab (3 h per week)

**L1 Workflow (pass/fail prerequisite):** open from GitHub in Colab, run the setup cell, load data through the registry, restart and run all, fill in the AI-use log.

**Failure analysis (required in every lab):** Repair an out-of-order notebook that only worked because of hidden state (the pattern found in the 2/2563 midterm key, audit S2).

## Independent work (5 h per week)

Python self-check (2 h); read the AI policy and Rule et al. (2019) (1.5 h); set up the local fallback environment (1.5 h).

## Datasets

| Dataset | Licence status |
|---|---|
| Iris / Air Quality (registry) | CC BY 4.0 (verified) |

## Existing material to reuse or retire

Issue codes refer to the [evidence audit](../../docs/audit/01-evidence-audit.md).

| Source | Decision |
|---|---|
| Lecture 0 and General presentation slides (S08, S09) | Retire: unfilled templates (P3) |

## Assessment links

L1 (pass/fail prerequisite for graded labs).

## Production notes

No additional dependencies expected.
Before this module counts as done, it must meet the [definition of done](../../docs/blueprint/03-curriculum-blueprint.md#91-definition-of-done-applies-to-every-module) and follow the [authoring guide](../../docs/authoring-guide.md).

Planned layout, matching the PCA pilot: `lecture/outline.md`, `lab/labNN_*.ipynb` (built from a private source), `exercises/`, `references.md`, `EXECUTION-REPORT.md`.
