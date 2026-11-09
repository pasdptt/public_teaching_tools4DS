# Module m07 — Network analysis (two teaching weeks)

| Status | Graded lab | Backlog item | Course CLOs | When |
|---|---|---|---|---|
| **Planned**: structure only; content not yet produced | Lab 7A: practice · **Lab 7B: graded lab G4** | B12 | CLO2, CLO3, CLO4 | see the [schedule](../../course/schedule.md) |

## Objectives (draft; finalise when the module is produced)

By the end of this module a student can:

1. **Build** a directed, weighted graph from tabular records, choosing what nodes, edges and weights mean.
2. **Represent** graphs as adjacency and sparse matrices and **compute** degree distributions.
3. **Run** Dijkstra's algorithm by hand and **justify** its correctness for non-negative weights.
4. **Compute and interpret** centrality, including PageRank as an eigenproblem, and **compare** with a null model.
5. **Detect** communities with modularity and **assess** them against a configuration-model null.
6. **Evaluate** link prediction with a correct edge split and **identify** graph-specific leakage.

## Lecture (2 h per teaching week)

* Part I: from tables to graphs; representations; degree distributions; paths and Dijkstra (correctness); connectivity
* Part II: centrality (degree, closeness, betweenness, eigenvector, PageRank); communities and modularity; null models (Erdős–Rényi, configuration model); spectral embedding; link prediction and edge-split leakage

## Lab (3 h per teaching week)

**Lab 7A (practice):** a flight network as a `DiGraph` with aggregated weights; Dijkstra by hand and in code. **Graded lab G4 (Lab 7B):** centrality and communities against a configuration-model null; link prediction with a correct edge split.

**Failure analysis (required in every lab):** Directed, repeated flights collapsed into an undirected simple graph (M19); silent regex parsing drift under pandas ≥ 2 (S6); evaluating on edges seen in training.

## Independent work (5 h per teaching week)

Hand-Dijkstra exercises (2 h per week); project method work (3 h per week).

## Datasets

| Dataset | Licence status |
|---|---|
| nycflights13 `flights` (336,776 rows) | **Licence to verify** (blueprint §8.3) |
| Zachary karate club (bundled with networkx) | Published data; citation Zachary (1977) |

## Existing material to reuse or retire

Issue codes refer to the [evidence audit](../../docs/audit/01-evidence-audit.md).

| Source | Decision |
|---|---|
| Intro2graphwithPython notebook (N07) | Revise substantially: directed weighted graph; fix parsing; add statistical network analysis (P4) |
| graph.pdf and handwritten graph notes (S10–S15) | Merge into concise reading notes; fix the in/out-degree proof (M20); cite the source textbook |
| Final-exam Dijkstra item (S02 Q5) | Kept as an item type, with a correctness justification added |

## Assessment links

Lab 7A practice; **graded lab G4 (Lab 7B)**; final item 4.

## Production notes

No additional dependencies expected.
Before this module counts as done, it must meet the [definition of done](../../docs/blueprint/03-curriculum-blueprint.md#91-definition-of-done-applies-to-every-module) and follow the [authoring guide](../../docs/authoring-guide.md).

Planned layout, matching the PCA pilot (`m04-pca`): `lecture/outline.md`, `lab/lab<module><part>_*.ipynb` (built from a private source), `exercises/`, `references.md`, `EXECUTION-REPORT.md`.
