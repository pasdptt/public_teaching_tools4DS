# Execution report — module m07

**Date:** 25 November 2026. Every result below comes from running the code **[V]**.

## 1. Environments

The two pinned environments of the [m04 execution report](../m04-pca/EXECUTION-REPORT.md#1-environments), with three additions to both pins (`environment/`): `networkx` 3.7 (preinstalled in Colab; the Colab-proxy pin assumes 3.x), `rdata` 1.1.0 (reads the nycflights13 `.rda` files; installed with the tsds helper package, so Colab gets it from the setup cell) and `statsmodels` (for module m08).

**Data.** `tsds.data.load("nycflights13_flights")` downloads the package's `flights.rda` from a pinned commit (df98ef2) of github.com/tidyverse/nycflights13, checks its SHA-256 and parses it (about 20 s once; the parsed frame is then cached). Licence: CC0, read in the package's DESCRIPTION file at that commit.

## 2. Results

| Check | Pinned local | Colab proxy |
|---|---|---|
| Student notebooks (7A, 7B): valid, no outputs, badge and setup cell, every task raises `NotImplementedError` | pass | pass |
| Student notebooks: given cells run top to bottom with every task and self-check removed | pass (7A 26 s with a cold data cache; 7B 2 s) | pass (27 s; 2 s) |
| Solution notebooks (private): run top to bottom, every self-check prints `OK`, ids match the student notebooks | pass (7A 3.6 s with the cache; 7B 6.3 s) | pass (3.6 s; 5.7 s) |
| Mutation test (private): 9 typical mistakes injected, one at a time (4 in 7A, 5 in 7B) | 9/9 caught | 9/9 caught |
| Auto-checker for G4 (private): solution scores 3/3 and 1/1 (25/25 hidden-test points); each 7B mutant loses correctness on its own task; a blank notebook scores 0 | pass | pass |
| Answer-key numbers (`key_numbers.py`, private) | identical | identical |

**The nine injected mistakes:** 7A: an undirected graph built (T1); the JAX → DFW path checked in the undirected graph (T2); the edge weight used instead of the path length in Dijkstra (T3); 2400 not wrapped to 0 (T4). 7B: right instead of left multiplication in PageRank (T1); the statistic computed on the observed graph instead of the null graphs (T2); a p-value of exactly 0 (T3); negatives drawn from the training graph's non-edges (T4); the full graph not used in the leakage comparison (T5).

## 3. Numbers quoted in the lecture outline and the labs

All identical in both environments.

| Quantity | Value |
|---|---|
| Flights: rows / flown (air time present) | 336,776 / 327,346 |
| Directed graph: airports / routes; out-degree EWR, JFK, LGA | 107 / 223; 85, 70, 68 |
| Destination in-degrees 1 / 2 / 3 | 27 / 35 / 42 airports |
| Undirected collapse: edges; reachable ordered pairs (directed vs undirected) | 224; 223 vs 11,342 |
| JFK–LAX air time: undirected (last row) vs directed mean (11,159 flights) | 298 vs 329.2 min |
| Old time conversion of 1630 (pandas 2.2 and 3.1) | `1630:30:00` |
| Dijkstra example from A: B, C, D, E, F | 3, 2, 8, 10, 12 |
| Karate: n, m; mean / median / max degree; diameter; mean shortest path | 34, 78; 4.59 / 3 / 17; 5; 2.408 |
| PageRank top 3 | 33 (0.101), 0 (0.097), 32 (0.072) |
| Betweenness, nodes 0 and 33; closeness, node 0 | 0.438, 0.304; 0.569 |
| Transitivity; Erdős–Rényi null mean (sd), z, p | 0.2557; 0.1342 (0.0300), 4.04, 0.005 |
| Transitivity; configuration null mean (sd), z, p | 0.2557; 0.2218 (0.0255), 1.33, 0.119 |
| Louvain: communities, Q; configuration null Q mean / max; p; ARI with the split | 4, 0.419; 0.292 / 0.336; 1/101; 0.392 |
| Fiedler split: agreement with the club split; misassigned; ARI; algebraic connectivity | 32/34; nodes 2 and 8; 0.772; 0.4685 |
| Block model: edges (within groups); hidden edges | 669 (567); 133 |
| Link-prediction AUC, training graph: Adamic–Adar, negative distance | 0.629, 0.630 |
| Link-prediction AUC, full graph (leak): Adamic–Adar, negative distance | 0.659, 1.000 |

## 4. Limitations

* **Not yet run in a real Colab runtime.** Before each session, open the lab from its badge in Colab and run *Restart session and run all* once. Lab 7A downloads 4.3 MB from raw.githubusercontent.com and installs `rdata` with the helper package.
* The Colab badges point to the `main` branch, so they work once this module is merged into `main`.
* nycflights13 contains only departures from NYC, so Lab 7A cannot show multi-hop paths on real flights; Dijkstra is practised on a small graph instead, and the lecture says why.
