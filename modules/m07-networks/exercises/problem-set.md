# Problem set — module m07 (independent work)

**Week 1:** redo Lab 7A on your own and upload it in Teams (about 1.5 hours), work P1–P2 by hand (about 2 hours), and project method work (about 1.5 hours). **Week 2:** do Lab 7B (graded lab G4) and submit it in Teams (about 2 hours), P3–P7 (about 1 hour), and project method work (about 2 hours). Not graded. Items marked **[hand]** are the kind that appear on the paper final (item 4).

**P1 [hand] — Dijkstra.** An undirected weighted graph has edges s–a 7, s–b 2, b–a 3, a–c 1, b–c 8, c–t 2, b–d 4, d–t 9. Run Dijkstra's algorithm from s in a table like the one in the lecture (one row per finalised node). Give the distance to every node and the shortest path to t. At which step is the tentative distance of a first improved?

**P2 [hand] — Correctness and the handshake identity.** (a) Explain in three sentences why Dijkstra's algorithm is correct when all weights are non-negative, and give a three-node example with one negative weight where it returns a wrong distance. (b) Prove that in a directed graph $\sum_v d^+(v) = \sum_v d^-(v) = |E|$.

**P3 [hand] — PageRank of a small graph.** A directed graph has edges 1→2, 1→3, 2→3, 3→1. (a) Write the transition matrix $P$. (b) With $\alpha = 1$ (no jumps), find the stationary distribution $\pi$ with $\pi^\top P = \pi^\top$ and $\sum \pi = 1$. (c) Which node is most central, and why does node 2 score lowest?

**P4 [hand] — Modularity.** Two triangles {1, 2, 3} and {4, 5, 6} are joined by the single edge 3–4. Compute the modularity of the partition {1, 2, 3}, {4, 5, 6}, and of putting all six nodes in one community.

**P5 [hand] — AUC.** Three hidden edges score 0.9, 0.4, 0.4 and three non-edges score 0.4, 0.2, 0.1. Compute the AUC as the share of (edge, non-edge) pairs in which the edge scores higher, counting ties as one half.

**P6 — Temporal edges** *(optional)*. You have email messages with timestamps and want to predict who will email whom next month. Describe a split that cannot leak the future, and name two features that would leak under a random edge split.

**P7 — Another statistic, the same null** *(optional)*. Repeat Lab 7B Part 2 with `nx.average_clustering` instead of transitivity. Is the conclusion the same? Explain why the two clustering measures can disagree in a graph with a few hubs.

**P8 — Reading** *(optional)*. Newman (2018), the chapters on measures and metrics and on community structure ([references](../references.md)).
