# Misconception checks — module m07 (formative, in lecture)

Use these with a show of hands or a polling tool (for example a Microsoft Forms quiz in the class team). Students answer individually, discuss in pairs for one minute, then re-vote. Each item names the misconception it targets. Answers and discussion notes are kept with the instructor material.

**MC1 — Degrees in a directed graph** (Part I, §1.2). A directed graph has 50 edges. What is the sum of all in-degrees plus the sum of all out-degrees?
A. 50 · B. 100 · C. 25 · D. it depends on the graph

**MC2 — Negative weights** (Part I, §1.4). True or false: *"Dijkstra's algorithm also finds shortest paths when some edge weights are negative, as long as there is no negative cycle."* Explain in one sentence.

**MC3 — The undirected collapse** (Part I, §1.5). Flights are stored as rows (origin, destination, air time). Someone builds `nx.Graph` from all rows. Which statement is true?
A. nothing is lost: networkx sums the repeated rows · B. each pair of airports keeps one edge, with the attributes of the last row, and direction is lost · C. networkx raises an error for repeated pairs · D. the graph becomes a multigraph

**MC4 — PageRank** (Part II, §2.1). PageRank is best described as:
A. the number of incoming links · B. the stationary distribution of a random walk with random jumps, a leading eigenvector · C. the share of shortest paths through a node · D. the number of triangles at a node

**MC5 — Which null?** (Part II, §2.2). A network's clustering is far above that of Erdős–Rényi graphs with the same number of nodes and edges, but not above that of configuration-model graphs. What is the most defensible conclusion?
A. the network is strongly clustered for a social reason · B. the high clustering is largely explained by the degree sequence · C. the configuration model is wrong · D. clustering cannot be tested

**MC6 — Modularity of random graphs** (Part II, §2.3). True or false: *"A community-detection method that finds modularity Q = 0.3 has found real communities, because random graphs have Q = 0."* Explain.

**MC7 — Where to compute features** (Part II, §2.4). For link prediction, the scores of the test pairs should be computed on:
A. the full graph, which has the most information · B. the training graph, with the test edges removed · C. the test edges only · D. it does not matter for AUC
