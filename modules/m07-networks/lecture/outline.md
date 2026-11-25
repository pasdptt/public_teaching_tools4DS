# Lecture outline — Network analysis (module m07)

**Slides:** [Part I deck](https://claude.ai/artifact/1bVvDRAKXpLhByejLDCDvq) (17 slides) · [Part II deck](https://claude.ai/artifact/Xm8kN1r4wGJ3th8rVhBrNf) (18 slides), for projection. Each deck matches its part of this outline section for section; the slide numbers are given in each section heading. Change both together.

**Length:** two lectures of 2 hours, delivered in Thai with English slides and terms. **Labs:** [Lab 7A](../lab/lab7a_graphs_paths.ipynb) (practice) and [Lab 7B](../lab/lab7b_centrality_communities.ipynb) (**graded lab G4**). Each is a guided run-through in the session, and each student then does the lab again as homework; Lab 7B's homework is marked.

Every number in this outline was produced by the lab code or the module's key-numbers script, and is the same in both CI environments (see [`../EXECUTION-REPORT.md`](../EXECUTION-REPORT.md)). Reference keys such as [New18] point to [`../references.md`](../references.md). The misconception checks (MC1–MC7) are in [`../exercises/misconception-checks.md`](../exercises/misconception-checks.md).

---

## Part I — Graphs from data, paths and Dijkstra

| Time | Section | Purpose |
|---|---|---|
| 0:00–0:20 | §1.1 From tables to graphs | Nodes, edges and weights are modelling decisions |
| 0:20–0:35 | §1.2 Representations and degree | Adjacency matrix, edge list; the handshake identity |
| 0:35–0:50 | §1.3 Degree distributions | Flights (a star) and the karate club |
| 0:50–1:00 | Break | |
| 1:00–1:35 | §1.4 Shortest paths: Dijkstra | Trace by hand; why it is correct; cost |
| 1:35–1:50 | §1.5 Failure analysis | The undirected collapse; a silent parsing change |
| 1:50–2:00 | §1.6 Lab 7A and this week | |

### §1.1 From tables to graphs (20 min) · slide 3

A graph $G = (V, E)$ is a set of nodes and a set of edges. A table of records does not determine it; we decide:

| Decision | Flights example (Lab 7A) |
|---|---|
| What is a node? | An airport |
| What is an edge? | At least one flight from $u$ to $v$: **directed** |
| Several records per edge? | 11,159 flights JFK → LAX: **aggregate** (count, mean air time) |
| Which rows count? | Flights that flew (9,430 rows, cancelled or diverted, have no air time) |

Graph types: undirected or directed; simple or multi-graph (several edges per pair); unweighted or weighted. networkx: `Graph`, `DiGraph`, `MultiGraph`, `MultiDiGraph` [New18].

### §1.2 Representations and degree (15 min) · slides 4–5

* **Adjacency matrix** $A$, $A_{ij} = 1$ (or the weight) if there is an edge $i \to j$; symmetric for an undirected graph. Memory $n^2$, so large sparse graphs are stored as **edge lists** or sparse matrices (memory proportional to $|E|$).
* **Degree:** undirected $k_i = \sum_j A_{ij}$; directed out-degree $d^+(i) = \sum_j A_{ij}$, in-degree $d^-(i) = \sum_j A_{ji}$.
* **Handshake identity.** Undirected: $\sum_i k_i = 2|E|$. Directed: $\sum_i d^+(i) = \sum_i d^-(i) = |E|$. **Proof:** count each edge once: a directed edge adds exactly 1 to its tail's out-degree and 1 to its head's in-degree. (The course's old notes argued by contradiction; the direct count is the proof, audit M20.)

> **MC1** (degrees in a directed graph) here.

### §1.3 Degree distributions (15 min) · slide 6

**Flights (Lab 7A).** 107 airports, 223 directed routes. All edges leave EWR (out-degree 85), JFK (70) or LGA (68); the 104 destinations have in-degree 1 (27 airports), 2 (35) or 3 (42) and out-degree 0. The data contain only **departures from NYC**, so the network is a star: it can answer "who serves where" but not questions about connections.

**Karate club** [Zac77]. 34 members, 78 friendships; mean degree 4.59, median 3, maximum 17. Two members (the administrator, node 33, degree 17; the instructor, node 0, degree 16) have far more ties than the rest: a **heavy-tailed** degree distribution in miniature. Diameter 5; average shortest path 2.41.

### §1.4 Shortest paths: Dijkstra (35 min) · slides 8–11 (slide 7: break)

**Problem.** Weighted graph with weights $w \ge 0$; find the shortest distance $d(v)$ from a source $s$ to every node [Dij59].

**Algorithm.** Tentative distances $d(s) = 0$, $d(v) = \infty$ otherwise (use ∞, not a large number such as 32767, audit M20). Repeatedly take the unfinished node $u$ with the smallest $d(u)$, finalise it, and **relax** its edges: $d(v) \leftarrow \min(d(v), d(u) + w(u, v))$.

**Worked example (trace on the board; Lab 7A T3).** Edges A→B 4, A→C 2, C→B 1, B→D 5, C→D 8, C→E 10, D→E 2, D→F 6, E→F 2.

| Step | Finalise | d(A) | d(B) | d(C) | d(D) | d(E) | d(F) |
|---|---|---|---|---|---|---|---|
| 0 | — | 0 | ∞ | ∞ | ∞ | ∞ | ∞ |
| 1 | A | **0** | 4 | 2 | ∞ | ∞ | ∞ |
| 2 | C | | 3 | **2** | 10 | 12 | ∞ |
| 3 | B | | **3** | | 8 | 12 | ∞ |
| 4 | D | | | | **8** | 10 | 14 |
| 5 | E | | | | | **10** | 12 |
| 6 | F | | | | | | **12** |

Shortest path to F: A → C → B → D → E → F, length 12.

**Why it is correct.** Invariant: every finalised node has its true distance. Take the next node $u$ (smallest tentative $d(u)$) and any path from $s$ to $u$. It leaves the finalised set at some edge $x \to y$ with $y$ unfinished; its length is at least $d(x) + w(x, y) \ge d(y) \ge d(u)$, because weights are non-negative. So no path beats $d(u)$. With a **negative** weight the last step fails (use Bellman–Ford instead).

**Cost.** With a binary-heap priority queue: $O((|V| + |E|) \log |V|)$.

> **MC2** (negative weights) here.

### §1.5 Failure analysis (15 min) · slides 12–14

**The undirected collapse (audit M19; Lab 7A Part 2).** The old notebook built `nx.from_pandas_edgelist(flights, "origin", "dest", edge_attr=True)`: an **undirected simple** graph. Three things go wrong:

| | Directed, aggregated (correct) | Undirected, one row per pair (old) |
|---|---|---|
| Edges | 223 | 224 |
| JFK–LAX air time | 329.2 min (mean of 11,159 flights) | 298 min (the last row only) |
| Reachable ordered pairs | 223 | 11,342 (every pair) |
| Route JAX → DFW | none: no flight leaves JAX in these data | JAX → EWR → DFW |

**A silent parsing change (audit S6; Lab 7A Part 4).** The old time conversion `s.str.replace("(\d{2}$)", "") + ":" + …` relied on `str.replace` treating the pattern as a regular expression. Since pandas 2.0 the default is `regex=False`: nothing matches, and 1630 becomes `1630:30:00`, with no error. Use integer arithmetic (`hhmm // 100`, `hhmm % 100`) and assert that results lie in range.

> **MC3** (the undirected collapse) here.

### §1.6 Lab 7A and this week (10 min) · slides 15–16 (slide 17: references)

**Lab 7A (practice):** four parts: the directed flights graph; the undirected collapse; Dijkstra; the time conversion. Run through in the session; redo it as homework and upload it to the Lab 7A practice assignment in Teams.

**Independent work this week (5 h):** redo Lab 7A (1.5 h); hand-Dijkstra exercises P1–P2 (2 h); project method work (1.5 h).

---

## Part II — Centrality, null models, communities and link prediction

| Time | Section | Purpose |
|---|---|---|
| 0:00–0:25 | §2.1 Centrality | Five measures; PageRank as an eigenproblem |
| 0:25–0:45 | §2.2 Null models | Is a statistic surprising? Erdős–Rényi vs configuration model |
| 0:45–0:55 | Break | |
| 0:55–1:20 | §2.3 Communities | Modularity, Louvain, spectral partitioning |
| 1:20–1:50 | §2.4 Link prediction and graph leakage | Edge splits; features from the full graph |
| 1:50–2:00 | §2.5 Graded lab G4 and this week | |

### §2.1 Centrality (25 min) · slides 3–5

| Measure | Idea | Karate: top member (value) |
|---|---|---|
| Degree | Number of ties | 33 (17) |
| Closeness | Inverse mean distance to everyone | 0 (0.569) |
| Betweenness | Share of shortest paths passing through | 0 (0.438) |
| Eigenvector | Central if connected to central nodes: leading eigenvector of $A$ | 33 (0.373) |
| PageRank | Stationary distribution of a random surfer | 33 (0.101) |

**PageRank** [BP98]. With probability $\alpha$ (0.85) follow a random out-edge; otherwise, and from a node without out-edges, jump to a random node. The stationary vector satisfies $\pi^\top = \pi^\top\big(\alpha P + (1-\alpha)\tfrac1n \mathbf 1 \mathbf 1^\top\big)$: the **leading left eigenvector** (eigenvalue 1) of the Google matrix, found by **power iteration**, the same idea as computing PCA's first component. Lab 7B T1 implements it; the top three are 33 (0.101), 0 (0.097) and 32 (0.072).

The measures disagree in instructive ways: node 2 is third by eigenvector centrality (it links well-connected members) but fourth by degree and PageRank; betweenness ranks 0 above 33 because 0 bridges more shortest paths.

> **MC4** (PageRank) here.

### §2.2 Null models (20 min) · slides 6–8

A statistic means little without a reference. Karate's **transitivity** (share of connected triples that close into triangles) is 0.256. Is that high?

| Null model | Keeps | Null mean (sd) | z | Empirical p |
|---|---|---|---|---|
| Erdős–Rényi $G(n, m)$ | $n = 34$, $m = 78$ | 0.134 (0.030) | 4.04 | 0.005 |
| Configuration model | every member's degree | 0.222 (0.026) | 1.33 | 0.119 |

200 null graphs each; $p = (1 + \#\{T_r \ge T_{obs}\})/(R + 1)$. Against random graphs, karate looks highly clustered; against graphs with **the same degrees**, it does not: the two hubs make many triangles by themselves. The configuration model [MR95] is sampled by **double-edge swaps** ($a\!-\!b, c\!-\!d \to a\!-\!d, c\!-\!b$), which keep every degree and keep the graph simple (Lab 7B T2). Choosing the null model is choosing the question.

> **MC5** (which null) here.

### §2.3 Communities (25 min) · slides 10–12 (slide 9: break)

**Modularity** [NG04] compares edges inside communities with the number expected given the degrees:

$$Q = \frac{1}{2m}\sum_{ij}\Big(A_{ij} - \frac{k_i k_j}{2m}\Big)[c_i = c_j].$$

**Louvain** [BGLL08] greedily moves nodes and merges communities to increase $Q$. On karate (Lab 7B T3): 4 communities, $Q = 0.419$. A search finds *some* structure in any graph: on 100 configuration-model graphs Louvain still reaches mean $Q = 0.292$ (maximum 0.336). So karate's communities are real (p = 1/101), but $Q$ must be judged against the null, not against 0. The 4 communities split each side of the actual 2-way split further (adjusted Rand index 0.39).

**Spectral partitioning** [Fie73]. The graph Laplacian $L = D - A$ has smallest eigenvalue 0; its second eigenvector (the Fiedler vector; eigenvalue 0.469 for karate) splits the graph by sign. On karate this 2-way split matches the actual split for 32 of 34 members (all but nodes 2 and 8; ARI 0.77). It is an eigenvector computation again, as in PCA.

> **MC6** (modularity of random graphs) here.

### §2.4 Link prediction and graph leakage (30 min) · slides 13–15

**Task.** Rank unconnected pairs by how likely an edge is [LNK07]. Scores for $(u, v)$: common neighbours; **Adamic–Adar** $\sum_{w \in N(u)\cap N(v)} 1/\log k_w$ [AA03]; negative shortest-path distance.

**Correct protocol (Lab 7B T4).** Hide a random 20% of edges (positives), sample as many non-edges of the **full** graph (negatives), compute every score on the **training graph** (hidden edges removed), and report AUC. Data: a stochastic block model [HLL83], 120 nodes in 3 groups, edge probability 0.25 within and 0.02 between (669 edges, 133 hidden).

| Score | AUC, training graph | AUC, full graph (leak) |
|---|---|---|
| Adamic–Adar | 0.629 | 0.659 |
| Negative distance | 0.630 | **1.000** |

On the full graph every hidden edge is still there, at distance 1, and every non-edge is at distance ≥ 2: perfect, and meaningless. Other graph leaks: random splits of **timestamped** edges (the model sees the future; split by time instead), and node features (degree, centrality, embeddings) computed on the full graph.

> **MC7** (where to compute features) here.

### §2.5 Graded lab G4 and this week (10 min) · slides 16–17 (slide 18: references)

**Graded lab G4 (Lab 7B).** Five parts: PageRank by power iteration; transitivity against the configuration-model null; Louvain communities against the null; link prediction with an edge split; the full-graph leak. In the session we run through the ideas on other examples; each student then does the lab **on their own as homework** and uploads the `.ipynb` to the G4 assignment in Teams. The homework is what is marked (3 + 1 points auto-checked, 2 + 2 points written answers).

**Independent work this week (5 h):** Lab 7B and submit it (2 h); problem set P3–P7 (1 h); project method work (2 h).
