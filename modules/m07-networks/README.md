# Module m07 — Network analysis (two teaching weeks)

| Status | Graded lab | Backlog item | Course CLOs | When |
|---|---|---|---|---|
| **Built** (25 Nov 2026): two lectures, Lab 7A, Lab 7B with hidden tests, exercises, references, execution report | Lab 7A: practice · **Lab 7B: graded lab G4** | B12 | CLO2, CLO3, CLO4 | two teaching weeks; see the [schedule](../../course/schedule.md) |

**Workspace:** Google Colab (open the labs with the badges below); a pinned local environment is the fallback.

| Material | Link |
|---|---|
| **Lecture slides** (for projection; each deck matches its part of the outline section for section) | [Part I deck](https://claude.ai/artifact/1bVvDRAKXpLhByejLDCDvq) (17 slides) · [Part II deck](https://claude.ai/artifact/Xm8kN1r4wGJ3th8rVhBrNf) (18 slides) |
| Lecture outline (two 2-hour lectures, with timings and worked examples) | [`lecture/outline.md`](lecture/outline.md) |
| Lab 7A — Graphs from tables, paths and Dijkstra (practice; run-through in the session, then redone as homework) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pasdptt/public_teaching_tools4DS/blob/main/modules/m07-networks/lab/lab7a_graphs_paths.ipynb) [`lab/lab7a_graphs_paths.ipynb`](lab/lab7a_graphs_paths.ipynb) |
| Lab 7B — Centrality, communities and link prediction (**graded lab G4**; run-through in the session, then done as homework and submitted in Teams) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pasdptt/public_teaching_tools4DS/blob/main/modules/m07-networks/lab/lab7b_centrality_communities.ipynb) [`lab/lab7b_centrality_communities.ipynb`](lab/lab7b_centrality_communities.ipynb) |
| Problem set (independent work; hand Dijkstra and final-exam practice) | [`exercises/problem-set.md`](exercises/problem-set.md) |
| Misconception checks (in lecture) | [`exercises/misconception-checks.md`](exercises/misconception-checks.md) |
| References (each verified against its DOI record) | [`references.md`](references.md) |
| Execution report | [`EXECUTION-REPORT.md`](EXECUTION-REPORT.md) |

The solutions, hidden tests, answer keys and marking notes are kept in the private instructor material.

## Objectives

By the end of this module a student can:

| ID | Objective (observable) | Evidence |
|---|---|---|
| m07-O1 | **Build** a directed, weighted graph from tabular records, choosing what nodes, edges and weights mean. | Lab 7A T1–T2, Q1–Q2 |
| m07-O2 | **Represent** graphs as adjacency matrices and **compute** degree distributions; **prove** the directed handshake identity. | Lab 7A T1; problem set P2 |
| m07-O3 | **Run** Dijkstra's algorithm by hand and **justify** its correctness for non-negative weights. | Lab 7A T3; problem set P1; final item 4 |
| m07-O4 | **Compute and interpret** centrality, including PageRank as an eigenproblem, and **compare** with a null model. | Lab 7B T1–T2, Q1–Q2; problem set P3; final item 4 |
| m07-O5 | **Detect** communities with modularity and **assess** them against a configuration-model null. | Lab 7B T3, Q2; problem set P4 |
| m07-O6 | **Evaluate** link prediction with a correct edge split and **identify** graph-specific leakage. | Lab 7B T4–T5, Q3–Q4; problem set P5 |

## Lecture (2 h per teaching week)

* Part I: from tables to graphs; representations; degree distributions; paths and Dijkstra (correctness); connectivity
* Part II: centrality (degree, closeness, betweenness, eigenvector, PageRank); null models (Erdős–Rényi, configuration model); communities and modularity; spectral partitioning; link prediction and edge-split leakage

## Lab (3 h per teaching week)

**Lab 7A (practice):** the 2013 NYC flights as a `DiGraph` with aggregated weights; the old notebook's undirected collapse; Dijkstra implemented and checked; a clock-time conversion that changed silently with pandas 2. **Graded lab G4 (Lab 7B):** PageRank by power iteration; transitivity and modularity against a configuration-model null (karate club); link prediction with a correct edge split on a stochastic block model.

**Failure analysis (required in every lab):** directed, repeated flights collapsed into an undirected simple graph (audit M19: 223 reachable airport pairs become 11,342, and JAX → EWR → DFW appears); the silent `str.replace` change (S6: `1630` becomes `1630:30:00`); features computed on the full graph in link prediction (AUC 0.630 becomes 1.000).

## Independent work (5 h per teaching week)

Week 1: redo Lab 7A (1.5 h); hand-Dijkstra exercises (2 h); project method work (1.5 h). Week 2: Lab 7B and submit it (2 h); problem set (1 h); project method work (2 h).

## Datasets

| Dataset | Licence status |
|---|---|
| nycflights13 `flights` (336,776 rows; registry `nycflights13_flights`, SHA-256 verified) | CC0 (verified in the package's DESCRIPTION file) |
| Zachary karate club (bundled with networkx) | Published data; cite Zachary (1977) |
| Stochastic block model (generated in the lab with the course seed) | n/a |

## Existing material to reuse or retire

Issue codes refer to the [evidence audit](../../docs/audit/01-evidence-audit.md).

| Source | Decision |
|---|---|
| Intro2graphwithPython notebook (N07) | Revised substantially: directed weighted graph; parsing fixed; statistical network analysis added (P4). Its undirected construction and time conversion are kept as failure-analysis exhibits |
| graph.pdf and handwritten graph notes (S10–S15) | Merged into the lecture outline; in/out-degree proof corrected to the direct count (M20); ∞ instead of 32767 |
| Final-exam Dijkstra item (S02 Q5) | Kept as an item type, with a correctness justification added |

## Assessment links

Lab 7A practice; **graded lab G4 (Lab 7B)**; final item 4.

## Production notes

Adds `networkx` (preinstalled in Colab) and `rdata` (installed with the tsds helper package; reads the `.rda` data files) to both environment pins. Hidden tests for G4: private repository, `grading/hidden/m07-networks/`.
