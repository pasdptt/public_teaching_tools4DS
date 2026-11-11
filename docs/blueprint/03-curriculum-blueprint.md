# Curriculum Blueprint — 040563107 Tools for Statistical Data Science (proposal)

**Status:** Proposal for lecturer review. Nothing here changes the approved course requirements until it is adopted through the department's TQF revision process.

> **Superseded in part by the lecturer's decisions of 9 November 2026** — see [`../decisions.md`](../decisions.md). In particular: 12 teaching weeks plus 3 adjustment weeks (not 15); module folders named `m01`–`m11`; about 100 students; six graded labs, all counting; teams of 5–6 (at most 20); live presentations with random-member Q&A; no Spark. The operational documents in [`../../course/`](../../course/) are current; this blueprint is kept as the reasoning record.
**Builds on:** [`../audit/01-evidence-audit.md`](../audit/01-evidence-audit.md) (issue IDs M·, E·, P·, S·, A·, C·, D·) and [`../audit/02-execution-report.md`](../audit/02-execution-report.md).
**Labels:** **[V]** verified fact · **[R]** recommendation · **[A]** assumption · **[P]** proposal that changes an approved TQF3 element.

## 0. Fixed parameters and design principles

### 0.1 Fixed parameters (from the brief and the TQF3)

| Parameter | Value | Source |
|---|---|---|
| Credits | 3 (2-3-5) | TQF3 [V] |
| Instructional weeks | 15, with examinations scheduled separately | Brief (provisional) |
| Contact per week | 2 h lecture + 3 h lab, i.e. 30 h + 45 h per semester, exactly the TQF3 hours | Brief; TQF3 [V] |
| Independent study | 5 h per week = 75 h, the TQF3 self-study hours | TQF3 [V] |
| Assessment weights | Midterm 20%, final 35%, project 25%, practical work 20% | Brief; TQF3 [V] |
| Scope | Dimension reduction, PCA, ICA, feature extraction, network analysis, smoothing and aggregation, HPC applications, streaming algorithms | TQF3 course description [V] |
| Resource envelope | Ordinary student laptops plus **Google Colab (primary workspace)**; no paid API and no GPU in required work | Brief and lecturer instruction |
| Terminology | English technical terms | Brief |

### 0.2 Design principles (all [R])

1. **Statistics first.** Every method is presented as an estimator or optimisation problem. Each comes with its assumptions, a derivation suited to third-year statistics students, and a hand-computable case.
2. **Fitted operations respect validation boundaries.** Scaling, imputation, dimension reduction, feature selection, resampling and smoothing parameters are fitted on training data only, inside `Pipeline` objects and cross-validation. Temporal and graph-specific forms of leakage get explicit treatment.
3. **Baselines before advanced methods.** Every comparison includes a simple baseline (majority class, raw features, naive forecast, degree centrality, exact computation) and an uncertainty estimate.
4. **Failure analysis and interpretation in every lab.** Each lab ends with a "What can go wrong?" task and a short written interpretation.
5. **Distinctions taught explicitly:**
   * feature selection vs feature extraction;
   * PCA (unsupervised, second-order, orthogonal) vs ICA (unsupervised, higher-order, independence);
   * LDA (supervised) vs unsupervised methods;
   * visualisation quality vs predictive usefulness.
6. **Colab-first reproducibility.** Every notebook opens from GitHub in Colab and runs top to bottom in a fresh runtime. It does not depend on Drive mounts, Kaggle tokens or hidden state, and it gets the same results locally from a pinned environment.
7. **Bounded modern content.** Embeddings and autoencoders take one bounded session. There are no agents, no transformer training and no MLOps beyond what reproducibility requires.

---

## 4. Course learning outcomes (CLOs) [P]

The TQF3 lists domain outcomes but no course-specific measurable outcomes (audit A1). The proposed CLOs map onto the TQF3 domain codes used in its assessment table (§5.2 of S01).

On successful completion, students will be able to:

| CLO | Statement (observable behaviour) | Bloom level | TQF3 domains | Evidence of attainment |
|---|---|---|---|---|
| **CLO1** | **Derive and explain** PCA, LDA and ICA as optimisation problems: state the objective, constraints, solution method (eigen/SVD decomposition, generalised eigenproblem, non-Gaussianity maximisation) and assumptions. **Compute** small cases by hand, including explained variance, loadings and LDA directions. | Understand, Apply | 2.1, 2.2, 3.1 | Midterm and final derivation and computation items; lab checkpoints |
| **CLO2** | **Construct** reproducible Colab workflows in which every fitted operation is fitted inside the training folds. **Detect and correct** data leakage, including temporal and graph-specific leakage. | Apply, Analyse | 3.1, 5.1, 5.2 | Lab rubric "validity" criterion; midterm code-review item; project M2 |
| **CLO3** | **Compare** feature-selection, feature-extraction and representation methods against simple baselines, with appropriate resampling and uncertainty. **Justify** whether a method helps prediction, interpretation or visualisation. | Analyse, Evaluate | 3.1, 3.2 | Labs 4–8; project M3; final item |
| **CLO4** | **Represent** relational data as directed, weighted or multi-graphs. **Compute and interpret** shortest paths, centrality and community structure relative to a null model. | Apply, Analyse | 2.2, 3.2 | Labs 9–10; final item (hand Dijkstra plus interpretation) |
| **CLO5** | **Apply** moving-average, exponential and kernel or local-regression smoothing and temporal aggregation. **Select** smoothing parameters by forward-chaining validation, and **compare** with naive baselines. | Apply, Evaluate | 2.2, 3.2, 5.1 | Labs 11–12; final item |
| **CLO6** | **Measure** time and memory cost and **apply** laptop-scale high-performance techniques (vectorisation, chunked or out-of-core processing, parallelism, randomised and incremental algorithms) and one-pass streaming algorithms. **Quantify** the accuracy–resource trade-off. | Apply, Analyse | 5.1, 5.2 | Labs 13–14; final item; project component |
| **CLO7** | **Communicate** an end-to-end analysis with limitations and failure analysis, and **document** any AI assistance in a verifiable way. | Create, Evaluate | 1.1, 4.1, 5.2 | Project M4–M5; AI-use logs; final project-reflection item |

**Attainment target [R]:** at least 70% of students reach the "Proficient" level or above on each CLO's primary evidence. The CLO attainment report feeds the TQF5.

---

## 5. Weekly lecture-and-lab plan [P]

Every week has 2 h of lecture, a 3 h lab and 5 h of independent work. The midterm sits between weeks 8 and 9 and the final after week 15, both in the university examination periods.

| Wk | Lecture (2 h) | Lab (3 h) — each lab ends with failure analysis and interpretation | CLOs | Independent work (5 h) | Assessment touchpoint |
|---|---|---|---|---|---|
| 1 | **Course design, reproducible Colab workflow, responsible AI-assisted coding.** Notebook state and execution order; seeds; environment checks; data provenance and licences; how to verify AI-generated code. | **L1 Workflow:** open from GitHub in Colab, run the setup and version-check cell, load data through the checksum-verified loader, restart and run all. *Failure analysis:* reproduce and fix an out-of-order notebook. | 2, 7 | Python refresher self-check; read the course AI policy | L1 (ungraded prerequisite) |
| 2 | **Statistical computing refresher with Python and SQL.** Means (arithmetic, geometric, harmonic) and when each is meaningful; variance and `ddof`; robust summaries; missing-value codes and sentinels; floating-point error. SQL with DuckDB: `GROUP BY` and window functions. | **L2 Data audit:** Air Quality (UCI) in pandas and DuckDB SQL. *Failure analysis:* the −200 sentinel (M15) and what it does to summaries. | 2, 5 | Exercises on summary statistics | L2 |
| 3 | **Evaluation and leakage.** Train/validation/test, k-fold, repeated, grouped and nested CV; baselines; uncertainty for test metrics (binomial intervals); leakage taxonomy (preprocessing, target, temporal, group, graph). Resampling for imbalance as a fitted operation. | **L3 Leakage lab:** the pure-noise leakage demonstration (audit C5), refitted with `Pipeline`; SMOTE and class weights inside CV. *Failure analysis:* identify leakage in an AI-generated notebook supplied by the instructor. | 2, 3 | Read Kapoor & Narayanan (2023) | L3 |
| 4 | **Dimension reduction I: selection vs extraction.** Curse of dimensionality; filter, wrapper and embedded selection; stability of selection; permutation importance on held-out data; selection inside CV. | **L4:** RFE and `SelectKBest` in pipelines on Wine (UCI), compared with an all-features baseline. *Failure analysis:* selection outside CV on high-dimensional noise. | 2, 3 | Project team formation | L4; **Project M1** (proposal) due |
| 5 | **PCA I: theory** *(pilot module)*. Variance maximisation via the Rayleigh quotient and Lagrange multipliers; spectral decomposition of S; equivalence with minimum reconstruction error; SVD of the centred data matrix; covariance vs correlation PCA; scores, loadings, explained variance; geometry. | **L5:** PCA from scratch (`eigh`/SVD) vs `sklearn.decomposition.PCA`; hand-check a 2×2 case. *Failure analysis:* uncentred projection, unscaled mixed-unit data, `eig` vs `eigh` (M2, M3). | 1 | Derivation problem set | L5 |
| 6 | **PCA II: practice** *(pilot module)*. Choosing k (scree, parallel analysis, CV reconstruction error); PCA inside predictive pipelines vs raw-feature baselines; visualisation vs prediction; outliers and robustness; compositional data (log-ratio before PCA); randomised and incremental PCA as a preview of week 13. | **L6:** PCA plus logistic regression on digits or MNIST with CV and baseline; a real-data case (Thai local-government revenue, subject to licence Q-D1, otherwise UCI Wine). *Failure analysis:* PCA fitted before the split; components chosen on the test set. | 1, 2, 3 | Project data audit | L6 |
| 7 | **Supervised vs unsupervised extraction: LDA and ICA.** Fisher criterion and the generalised eigenproblem; at most K−1 directions; LDA as classifier vs projection. ICA: latent-source model, whitening, non-Gaussianity (kurtosis, negentropy), FastICA, identifiability and its failure with Gaussian sources; PCA vs ICA on the same mixtures. | **L7:** blind source separation of synthetic signals with known ground truth (PCA vs FastICA); LDA inside a pipeline vs PCA plus classifier. *Failure analysis:* Gaussian sources; LDA fitted before the split (E1). | 1, 2, 3 | Midterm revision set | L7; **Project M2** (data audit and baseline) due |
| 8 | **Nonlinear and learned representations (bounded).** Kernel PCA, LLE and Isomap, t-SNE: what each preserves; trustworthiness metrics; why t-SNE is not a feature extractor. A small autoencoder (linear output, MSE) compared with PCA on reconstruction error. Precomputed pretrained embeddings as a modern representation, CPU only. | **L8:** t-SNE and UMAP-style views vs PCA on digits, with trustworthiness and k-NN accuracy on held-out data; a CPU autoencoder with a time cap. *Failure analysis:* the M9 loss bug; a "beautiful clusters, useless features" case. | 1, 3 | Midterm revision | L8 |
| — | **Midterm examination** (examination period) | — | 1, 2, 3 | — | Midterm 20% |
| 9 | **Network analysis I.** From tables to graphs (directed, weighted, multi-graphs); adjacency and incidence matrices, sparse storage; degree distributions; paths and Dijkstra (correctness argument); connectivity. Concise notes revised from the graph-theory material (S10). | **L9:** a flight network from nycflights13 (or an approved alternative) as a `DiGraph` with aggregated weights; Dijkstra by hand and in code. *Failure analysis:* the undirected collapse of directed flights (M19); regex parsing drift (S6). | 4, 2 | Hand-Dijkstra exercises | L9 |
| 10 | **Network analysis II.** Centrality (degree, closeness, betweenness, eigenvector, PageRank as an eigenproblem, linking back to PCA); communities and modularity; null models (Erdős–Rényi, configuration model); spectral embedding; **graph leakage** in link prediction (edge splits, temporal edges). | **L10:** centrality and communities compared with a configuration-model null; link prediction with a correct edge split. *Failure analysis:* evaluating on edges seen in training. | 4, 2, 3 | Project method work | L10 |
| 11 | **Smoothing and aggregation I.** Smoothers as estimators of a signal; trailing vs centred moving averages; exponential smoothing, Holt and ETS as models with estimated parameters; kernel (Nadaraya–Watson) and LOESS smoothers; bandwidth bias–variance; temporal aggregation, resampling and window functions. | **L11:** Air Quality with sentinel handling; MA, EWMA and LOESS with bandwidth chosen by a stated criterion; aggregate to daily. *Failure analysis:* sentinels treated as data; centred windows used for "forecasting". | 5, 2 | Project method work | L11; **Project M3** (method comparison) due |
| 12 | **Temporal evaluation.** Rolling-origin (forward-chaining) validation; naive and seasonal-naive baselines; forecast accuracy measures; **temporal leakage** (full-series scaling, centred windows, look-ahead features); random walk as a process and baseline (corrects M14). | **L12:** SES and Holt vs naive with rolling-origin CV on a regularly aggregated series. *Failure analysis:* SES on irregular transaction rows (M18); a shuffled K-fold on a time series. | 5, 2, 3 | Read Hyndman & Athanasopoulos, chapters on evaluation | L12 |
| 13 | **High-performance computing on a laptop.** Complexity and profiling (time, memory); vectorisation; Numba; parallel CV with `joblib`; chunked and out-of-core processing (Parquet plus DuckDB); randomised SVD and `IncrementalPCA` with the accuracy–time trade-off. Distributed engines (Spark) only as an optional appendix. | **L13:** benchmark a loop vs vectorised vs Numba statistic; out-of-core aggregation of a dataset larger than comfortable RAM (generated deterministically); randomised vs full SVD error and time. *Failure analysis:* memory blow-up from naive `read_csv`; a parallelism slowdown. | 6 | Project integration | L13 |
| 14 | **Streaming algorithms.** One-pass model and memory bounds; Welford's online mean and variance (stability vs the naive formula); reservoir sampling (proof of uniformity); Count-Min sketch (ε, δ bounds); HyperLogLog (relative error ≈ 1.04/√m); EWMA as a streaming smoother; incremental PCA on a stream; a simple drift check. | **L14:** replay Air Quality or flights as a stream; compare sketches with exact answers across memory budgets. *Failure analysis:* catastrophic cancellation; a biased "sample the first n" approach. | 6, 5 | Final report drafting | L14 |
| 15 | **Project presentations and synthesis.** Course synthesis; how the methods connect (eigenproblems in PCA, LDA, spectral graphs and PageRank). | Presentations with individual oral defence. | 7 | Final revision | **Project M4 + M5** due |
| — | **Final examination** (examination period) | — | 1–7 | — | Final 35% |

**Contact-hour check:** 15 × 2 = 30 lecture hours and 15 × 3 = 45 lab hours, matching the TQF3 **[V]**.

**Independent-work check:** 15 × 5 = 75 hours, matching the TQF3 **[V]**. It consists of reading (about 1.5 h), problem sets or lab completion (about 2 h) and project work (about 1.5 h) **[R]**.

### 5.1 Changes relative to the TQF3 weekly plan [P]

| TQF3 (2/2563) | Proposal | Reason |
|---|---|---|
| W1 Introduction; W2–3 Python & SQL | W1 workflow; W2 Python + SQL refresher | Frees a week for evaluation; SQL is actually delivered (C3). |
| — | W3 Evaluation and leakage | C5; a brief requirement. |
| W4 Dimension reduction, W5 PCA | W4 selection vs extraction; W5–6 PCA (two weeks) | PCA is the mathematical core (M4). |
| W6 ICA, W7 Feature extraction 1, W10 Feature extraction 2 | W7 LDA + ICA; W8 nonlinear and learned representations | Consolidated before the midterm. |
| W8 Project proposal & review | Proposal moved to W4; M2 at W7 | Earlier, staged milestones (A5). |
| W11–12 Network analysis 1–2 | W9–10 (statistical network analysis added) | P4. |
| W13 Smoothing & aggregation | W11–12 (adds temporal evaluation) | M14–M18, E8. |
| *(no HPC week)* | W13 HPC on a laptop | C1: a scope item with no allocated week. |
| W14 Streaming algorithm | W14 Streaming algorithms | C2 (content created). |
| W15 Final project presentation | W15 Presentations and synthesis | Unchanged. |

---

## 6. Outcome → topic → assessment mapping [P]

● = primary evidence, ○ = supporting evidence.

| | W1 | W2 | W3 | W4 | W5 | W6 | W7 | W8 | W9 | W10 | W11 | W12 | W13 | W14 | W15 | Labs (20%) | Project (25%) | Midterm (20%) | Final (35%) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CLO1 Derive and compute PCA/LDA/ICA | | | | ○ | ● | ● | ● | ○ | | ○ | | | ○ | | | ○ | ○ | ● | ● |
| CLO2 Reproducible, leakage-free workflows | ● | ○ | ● | ● | ○ | ● | ● | ○ | ○ | ● | ○ | ● | | | | ● | ● | ● | ○ |
| CLO3 Compare against baselines | | | ● | ● | | ● | ● | ● | | ○ | | ● | | | | ● | ● | ○ | ● |
| CLO4 Network analysis | | | | | | | | | ● | ● | | | | | | ● | ○ | | ● |
| CLO5 Smoothing and aggregation | | ○ | | | | | | | | | ● | ● | | ○ | | ● | ○ | | ● |
| CLO6 HPC and streaming | | | | | | ○ | | | | | | | ● | ● | | ● | ○ | | ● |
| CLO7 Communication and AI disclosure | ● | | ○ | ○ | | | | | | | | | | | ● | ○ | ● | | ○ |

**TQF3 assessment-table repair (A1) [P]:** practical work (20%) is mapped to domains 3.1, 5.1 and 5.2 (CLO2, CLO3, CLO6); it was previously unmapped.

---

## 7. Assessment blueprint

### 7.1 Overview (weights unchanged)

| Component | Weight | Format [R] | CLOs |
|---|---|---|---|
| Practical work | 20% | 13 graded labs (L2–L14), best **10** count at 2% each; L1 is a pass/fail prerequisite | 2–6 |
| Project | 25% | Teams of 2–3 (Q-A3); five milestones (§7.3) | 2, 3, 7 (+ one of 4/5/6) |
| Midterm | 20% | **In person**, 2 h, closed book with one A4 double-sided sheet (current practice); covers W1–W7 | 1, 2, 3 |
| Final | 35% | **In person**, 3 h, closed book with one A4 double-sided sheet; cumulative, about 30% pre-midterm and 70% post-midterm (current practice) | 1–7 |

**No bonus points [R].** A2 found that a bonus could take the paper to 42 of 35 points.

### 7.2 Examination blueprints

Each blueprint lists items as types and points, not as questions. A new paper is written each term from an item bank that is kept **outside** the public repository.

**Midterm: 20 points**

| Item | Type | CLO | Cognitive level | Points |
|---|---|---|---|---|
| 1 | Hand computation: means and variance with sentinel handling; 2×2 covariance → eigenvalues, explained variance, first principal-component direction | 1 | Apply | 5 |
| 2 | Derivation: PCA variance maximisation via a Lagrange multiplier, *or* the LDA Fisher criterion | 1 | Understand / Apply | 5 |
| 3 | Code review: find and fix the leakage in a short pipeline excerpt (print-based, no computer) | 2 | Analyse | 4 |
| 4 | Interpretation: scree plot and loadings output; selection vs extraction decision | 3 | Analyse / Evaluate | 3 |
| 5 | PCA vs ICA on a described mixing scenario; identifiability | 1 | Understand | 3 |

**Final: 35 points** (11 pre-midterm = 31%, 24 post-midterm = 69%)

| Item | Type | CLO | Points |
|---|---|---|---|
| 1 | PCA, LDA or ICA computation and interpretation (pre) | 1 | 6 |
| 2 | Validation design for a new scenario, including grouped or temporal splits (pre) | 2, 3 | 5 |
| 3 | Visualisation vs predictive usefulness of a nonlinear embedding (post) | 3 | 4 |
| 4 | Network: Dijkstra by hand with a correctness justification; centrality interpretation against a null model (post) | 4 | 5 |
| 5 | Smoothing: compute SES or EWMA by hand; choose a parameter; spot temporal leakage (post) | 5 | 5 |
| 6 | Streaming and HPC: Welford, reservoir or Count-Min reasoning; complexity and memory trade-off (post) | 6 | 6 |
| 7 | Individual project reflection: limitations and what you would change (post; retains the current practice) | 7 | 4 |

### 7.3 Project milestones (25%)

| Milestone | Week due | Weight | Deliverable | Pass requirements |
|---|---|---|---|---|
| M1 Proposal | 4 | 2% | 1 page: question, dataset with licence and citation, unit of analysis, intended methods | Dataset licence verified; question answerable |
| M2 Data audit and baseline | 7 | 5% | Colab notebook: data audit (missingness, sentinels, leakage risks), a baseline with a valid protocol | Restart-and-run-all succeeds; baseline and uncertainty reported |
| M3 Method comparison | 11 | 6% | At least one dimension-reduction or feature method *and* at least one of network / smoothing / HPC / streaming, compared against the baseline | All fitted steps inside validation; failure analysis section |
| M4 Final repository and report | 15 | 8% | Reproducible notebook(s) plus a report of 8 pages or fewer, with an AI-use appendix | Clean rerun from the README instructions; claims supported by outputs |
| M5 Presentation and oral defence | 15 | 4% | 10-min team talk plus 5-min individual questioning on the team's code | Each member explains any cell chosen by the examiner |

**Individual marks [R]:** the M5 oral score and a peer-assessment factor between 0.8 and 1.1 (Q-A3) adjust individual project marks.

### 7.4 Grading rubrics

**Lab rubric (each graded lab /8 → 2%)**

| Criterion | 4 Exemplary | 3 Proficient | 2 Developing | 1 Beginning |
|---|---|---|---|---|
| **Correctness and validity** (×0.75, max 3) | All steps correct; every fitted operation inside validation; baseline and uncertainty reported | Minor error that does not change conclusions; validation correct | Validation flaw or missing baseline | Leakage or wrong method invalidates the results |
| **Reproducibility** (×0.25, max 1) | Restart-and-run-all clean; seeds set; data through the registry | Runs with a trivial fix | Runs only out of order | Does not run |
| **Failure analysis** (×0.5, max 2) | Diagnoses the failure mechanism and demonstrates the fix with evidence | Identifies the failure and its fix | Names a failure without evidence | Missing |
| **Interpretation** (×0.5, max 2) | Statistically precise, states limitations, separates visualisation from prediction | Mostly precise | Descriptive only | Missing or wrong |

**Project report rubric (M4, scaled to 8%):**

| Criterion | Share |
|---|---|
| Problem framing and data provenance | 15% |
| Validity of the evaluation design | 25% |
| Methodological depth and correctness | 20% |
| Failure analysis and limitations | 15% |
| Reproducibility | 15% |
| Communication | 10% |

Each criterion uses the four performance levels above.

**Presentation and oral rubric (M5, 4%):**

| Criterion | Share |
|---|---|
| Clarity | 25% |
| Accuracy of answers about the team's own code and method | 50% |
| Handling of limitations | 25% |

### 7.5 AI-use policy [R]

| Context | Permitted | Conditions |
|---|---|---|
| Labs and project | **Yes**: code completion, explanation, debugging; this includes Colab's built-in assistant where the student's account offers it. **Not required**, because required work never depends on any AI tool or paid API. | (1) An **AI-use log** cell in every submission: tool, purpose, what was accepted or changed, and **how it was verified** (test, hand check, comparison with the documented API). (2) The student must be able to explain any submitted cell; this is checked in M5 and by spot oral checks. (3) Do not paste non-public data or other students' work into AI tools. (4) Fabricated outputs or citations are academic misconduct. |
| Lab "AI audit" tasks (L1, L3, L8, L12) | Required **critique** of instructor-supplied AI-generated code containing planted errors (leakage, sentinels, wrong loss) | Teaches verification, not prompting. |
| Midterm and final | **No AI and no internet** | In-person examinations (resolves A4). |
| Undisclosed or unverifiable use | — | Handled under the faculty's existing academic-integrity procedures. **[A]** This blueprint does not restate institutional rules. |

---

## 8. Repository structure, dataset strategy and reproducible environment

### 8.1 Proposed structure of this public repository

> **Implemented** (structure, course documents, module skeletons, CI). See the [repository map](../../README.md#repository-map). One name differs from the plan below: the Colab environment file is `environment/requirements-colab-proxy.txt` until a real Colab snapshot replaces it.

```
public_teaching_tools4DS/
├── README.md                       course overview, Open-in-Colab index
├── LICENSE / LICENSE-content       code and content licences (decision Q-R1)
├── course/                         syllabus, schedule, assessment, rubrics, ai-policy, glossary (EN–TH)
├── modules/
│   └── wNN-<topic>/
│       ├── README.md               objectives, timing, prerequisites, references
│       ├── lecture/outline.md      equations, worked examples, misconception checks
│       ├── lab/lab.ipynb           STUDENT notebook (outputs stripped; Open-in-Colab badge)
│       └── exercises/              problem sets (questions only)
├── datasets/
│   ├── registry.yaml               name, URL, licence, citation/DOI, sha256, size, loader
│   └── ATTRIBUTION.md
├── src/tsds/                       small helper package: env check, seeded RNG, checksum-verified loaders
├── environment/
│   ├── requirements-colab.txt      the few extras not preinstalled in Colab, pinned
│   ├── colab-snapshot-<term>.txt   frozen package list of a fresh Colab runtime at term start
│   └── requirements-local.txt      full pinned local fallback (uv lock), Python 3.12
├── tests/                          notebook execution and solution-consistency tests
├── tools/audit/                    audit harness used for this report
├── docs/audit/, docs/blueprint/    this audit and blueprint
└── .github/workflows/notebooks.yml CI: execute all student notebooks in a clean environment
```

**Instructor solutions, answer keys and the examination item bank live in a separate private repository** [R], for example `pasdptt/tools4ds-instructor` (decision Q-R1). It mirrors the same `modules/` paths, and its CI runs every solution against the public student notebook. That check is what keeps the solutions consistent with the questions.

### 8.2 Colab-first environment design [R]

1. **Launch.** Each notebook opens directly from GitHub via a Colab badge such as `colab.research.google.com/github/pasdptt/public_teaching_tools4DS/blob/main/modules/m04-pca/lab/lab4a_pca_theory.ipynb`. No Drive mount is needed.
2. **First cell.** It installs only the pinned course extras (`environment/requirements-colab.txt` and the `tsds` helper at a tagged release). It then runs `tsds.env.check()`, which prints the Python, numpy, pandas, scikit-learn and Matplotlib versions and warns if any is outside the CI-tested range.
3. **Do not downgrade Colab's core packages.** Downgrading pandas or numpy inside Colab forces runtime restarts and can conflict with Colab's own packages **[A — to be confirmed during the pilot]**. Instead:
   * the course code is written to be compatible with Colab's current core versions;
   * at the start of each term, `pip freeze` from a fresh runtime is committed as `colab-snapshot-<term>.txt`;
   * CI executes every notebook against **that snapshot** *and* against the pinned local environment.

   This directly prevents the drift failures in audit S1.
4. **Local fallback.** Using `uv` with `requirements-local.txt` (Python 3.12, CPU only) gives the same results on an 8 GB RAM laptop. This also serves offline work and examinations of practical skills if they are ever needed.
5. **No hidden state.** Student notebooks are committed with outputs stripped. CI runs top to bottom in a fresh kernel. Submissions must include a restart-and-run-all execution, and execution counts are checked to run consecutively from 1.
6. **Determinism.** Every stochastic step takes the `tsds` seed. Labs report run-to-run variation where it matters.
7. **Runtime budget.** Each lab executes end to end in 10 minutes or less on Colab's free CPU runtime **[A — to be measured; MNIST PCA plus logistic regression took about 30 s in the audit, mode C]**.

### 8.3 Dataset strategy [R]

**Rules:**

* Openly licensed data only, with verified licence and citation.
* Downloaded by URL with a SHA-256 checksum; mirrored in-repo when the licence permits (CC BY 4.0 does, with attribution) so that Colab never depends on a third-party host.
* No Kaggle tokens, no Drive paths.
* Synthetic generators for leakage, ICA and streaming demonstrations, where ground truth is needed.

| Week(s) | Dataset | Source | Licence status | Purpose |
|---|---|---|---|---|
| 2, 11–12, 14 | Air Quality (9,358 hourly records) | UCI id 360, DOI 10.24432/C59K5F | CC BY 4.0 **[V]** | Sentinels, smoothing, streaming replay |
| 4–7 | Wine | UCI id 109, DOI 10.24432/C5PC7J | CC BY 4.0 **[V]** | Selection, PCA, LDA |
| 5 | Iris | UCI id 53, DOI 10.24432/C56C76 (or `sklearn` bundled) | CC BY 4.0 **[V]** | Hand-sized PCA; provenance lesson (M7) |
| 6, 8 | Digits (`sklearn` bundled) / MNIST | OpenML 554 | MNIST "Public" on OpenML **[V]**; bundled digits licence to verify **[A]** | PCA for prediction; nonlinear embeddings |
| 3 | Synthetic noise and `make_classification` | generated | n/a | Leakage demonstrations |
| 7 | Synthetic source signals | generated | n/a | ICA with ground truth |
| 6, project | Thai local-government revenue FY2562 (7,853 × 42) | Drive copy; origin unknown | **Unverified** (Q-D1) | Local, high-dimensional PCA case |
| 8 | Precomputed text embeddings of a small open corpus | TBD | **TBD** (Q-D2) | Modern representations, CPU only |
| 9–10, 13 | nycflights13 `flights` (336,776 rows) | nycflights13 package | **Licence to verify** **[A]** | Directed weighted network; HPC scaling |
| 10 | Zachary karate club | `networkx` bundled; Zachary (1977) | Published data **[A]** | Communities with known split |
| 13–14 | Deterministic synthetic "large" table and streams | generated | n/a | Out-of-core and streaming at controllable scale |
| *Retired* | Titanic (Kaggle), Pima, `Cleandata.csv`, the 100-row Airlines sample | — | — | Audit D-1, D-2, D08, D02 |

---

## 9. Prioritised production backlog and acceptance criteria

### 9.1 Definition of done (applies to every module)

A module is done when all of the following hold:

1. CI executes the student notebook and the private solution top to bottom **in a fresh kernel** under both `colab-snapshot-<term>` and `requirements-local`, with no errors.
2. Data comes only through `datasets/registry.yaml`; checksums are verified; licences are confirmed.
3. No hidden state: student notebooks are committed with outputs stripped, and the solution's execution counts run consecutively.
4. Every fitted operation is inside the validation boundary, and an automated test checks this where feasible.
5. Every comparison has a baseline and an uncertainty estimate.
6. Every lab contains objectives, tasks, a failure-analysis task and an interpretation prompt.
7. The solution answers every question in the student notebook; a CI check matches question IDs to solution IDs.
8. References are verified (DOI, ISBN or stable URL checked), and no third-party text is copied without permission.
9. The lab fits a 3 h session, piloted with a teaching assistant or a student.
10. The runtime is 10 minutes or less on Colab's free CPU runtime.

### 9.2 Backlog

| ID | Priority | Item | Acceptance criteria (in addition to §9.1) | Depends on |
|---|---|---|---|---|
| B01 | **P0** | Lecturer decisions in §10 | Q-L1, Q-R1, Q-A1, Q-D1 answered in writing | — |
| B02 | **P0** | Repository skeleton, `tsds` helper (env check, seeds, loaders), CI workflow, Colab badge template | A sample notebook passes CI under both environments; the Colab badge opens and runs it | B01 (Q-R1) |
| B03 | **P0** | Dataset registry and attribution for the week 2–7 datasets | Licence, citation, size and SHA-256 recorded; the loader fails loudly on a checksum mismatch | B02 |
| B04 | **P0** | **PCA pilot module (W5–6)**: lesson plan, lecture outline with derivations and worked examples, student lab, separate instructor solution, exercises, misconception checks, assessment items, verified references, execution report | The brief's PCA pilot requirements plus §9.1; corrects M1–M7 and E4 | B02, B03 |
| B05 | P1 | Course documents: syllabus, schedule, assessment, rubrics (§7.4), AI policy (§7.5), project brief and milestone templates | Lecturer-approved; consistent with the TQF3 weights; TQF3 revision draft prepared | B01 |
| B06 | P1 | W3 evaluation and leakage module (includes the imbalance material) | Contains the leakage-on-noise demonstration; metric consistency (fixes E7) | B02 |
| B07 | P1 | W1–2 workflow and refresher modules (Python + DuckDB SQL) | SQL delivered (C3); sentinel lab (M15) | B02, B03 |
| B08 | P1 | W4 selection vs extraction | M12 and M13 fixed; permutation importance on held-out data | B06 |
| B09 | P1 | W7 LDA and ICA | Ground-truth source separation; Gaussian failure case; LDA inside the pipeline (fixes M8, M10, E1) | B04 |
| B10 | P1 | Midterm item bank (private) and marking keys | 3 or more variants per item type; keys verified by a second marker | B04, B06, B09 |
| B11 | P2 | W8 nonlinear and learned representations (bounded) | M9 and M11 fixed; trustworthiness metric; time-capped CPU autoencoder | B04 |
| B12 | P2 | W9–10 network analysis (with revised graph notes) | Directed weighted graph; null-model comparison; edge-split link prediction (fixes M19, M20, S6, E9) | B03 |
| B13 | P2 | W11–12 smoothing, aggregation and temporal evaluation | Sentinel handling; LOESS and bandwidth selection; rolling-origin CV vs naive (fixes M14–M18, E8) | B03 |
| B14 | P2 | W13 HPC on a laptop | Benchmarks report time *and* memory; randomised SVD error vs time; runs within the free Colab memory limit | B02 |
| B15 | P2 | W14 streaming algorithms | Sketch errors compared with exact answers across memory budgets; the Welford stability demonstration | B13 |
| B16 | P2 | Final examination item bank (private) | Follows the §7.2 blueprint; no item reused verbatim from 2/2563–2/2564 | B10–B15 |
| B17 | P3 | Optional appendix: UMAP (Spark removed by decision D16) | Clearly marked optional; not assessed | B14 |
| B19 | **P1** | Hidden-test auto-checking for graded labs G1–G6 (decision D12): hidden tests per graded lab (private), a grader that reruns each submission in a fresh kernel, checks restart-and-run-all and scores the code criteria | Grader reproduces the rubric's auto-checked criteria on the PCA Lab 4B solution (full marks) and on the mutation-test variants (marks lost); runs 100 submissions in under 1 h on a laptop | B02 |
| B20 | P2 | Openly licensed Thai text corpus for module m06 (decision D19): source, licence verification, CPU-precomputed embeddings, registry entry | Licence verified and recorded; embeddings reproducible from a script; lecturer approval | B03 |
| B21 | **P0 — done 11 Nov 2026** | Move instructor material to the private repository (decision D1) and enable solution tests in its CI | Private CI runs the solution and mutation tests on every push | Lecturer creates the repository |
| B18 | P3 | Bilingual glossary (EN–TH) and accessibility review | Glossary covers all assessed terms | B01 (Q-L1) |

---

## 10. Assumptions, unresolved questions and decisions for lecturer review

### 10.1 Decisions requiring the lecturer (with my recommendation)

| ID | Decision | Recommendation [R] |
|---|---|---|
| **Q-L1** | Teaching language: Thai delivery with English terminology, or English-medium? Examination language? | Thai lecture delivery; English slides, notebooks and technical terms; bilingual glossary; exams bilingual or English, **subject to programme regulations** **[A]**. |
| **Q-R1** | Where instructor solutions and examination banks live; licences for this public repository | A private companion repository; MIT for code and CC BY 4.0 for original teaching text. |
| **Q-A1** | Examination mode | In-person, closed book with one A4 sheet for both exams; no take-home or online open-internet exams (A4). |
| Q-A2 | Keep the individual project-reflection item in the final? | Yes, 4 points; it evidences individual contribution. |
| Q-A3 | Team size; peer-assessment factor | Teams of 2–3; factor between 0.8 and 1.1. |
| Q-A4 | Lab scoring | Best 10 of 13 graded labs. |
| Q-S1 | Adopt the revised weekly schedule (§5.1) via the TQF3 revision | Yes. It is the only way to give HPC and streaming explicit coverage. |
| Q-S2 | Keep imbalance and SMOTE (outside the TQF scope)? | Only inside W3, as an example of resampling as a fitted operation. |
| Q-S3 | Spark | Optional appendix only (it belongs to 040563105). |
| **Q-D1** | Source and licence of `revenue_thlg_2562.xlsx`; may it be published? | Use it if the licence is confirmed; otherwise fall back to UCI Wine. |
| Q-D2 | Corpus for precomputed embeddings in W8 | An openly licensed corpus, preferably Thai, after a licence check. |
| Q-AI1 | Allow Colab's built-in AI assistant in labs? | Yes, under the disclosure log (§7.5). |

### 10.2 Assumptions [A]

1. Students have completed linear algebra (eigen-decomposition) and introductory statistical inference before year 3, although the TQF3 lists no prerequisite. *This needs confirming against the programme structure.*
2. Students can use Google Colab with their university or personal Google accounts, and Colab's free CPU runtime remains available.
3. Class size allows 5-minute individual oral questioning in week 15, roughly 40 students or fewer, or a teaching assistant is available.
4. Examination periods are scheduled by the university outside the 15 instructional weeks.
5. The Drive search found all relevant existing material; files stored under other names may exist.
6. Colab's package versions at the time of the lecturer's last runs matched the mode-C pins inferred from the stored warnings.

### 10.3 Unresolved questions arising from the audit

1. Is there a project brief or rubric from earlier terms that is not on Drive (A5)?
2. What is the source of the SES `Cleandata.csv` (D08), and should that example be kept at all?
3. Which textbook is `graph.pdf` summarised from (S10)? It should be cited.
4. Were lecture slides for weeks 4–14 delivered from another platform? None were found (P3).
5. The 2/2564 midterm question paper was only partly decoded during the audit (S05). Does it differ from 2/2563?

### 10.4 Candidate core references

Bibliographic details were written from memory and **must be verified (DOI or ISBN) in backlog B04 and later items before use**. None is yet cited as verified.

| Topic | References |
|---|---|
| PCA | Jolliffe, I. T. (2002). *Principal Component Analysis* (2nd ed.). Springer. · Jolliffe, I. T., & Cadima, J. (2016). Principal component analysis: a review and recent developments. *Phil. Trans. R. Soc. A*, 374. |
| ICA | Hyvärinen, A., & Oja, E. (2000). Independent component analysis: algorithms and applications. *Neural Networks*, 13(4–5). |
| General statistical learning | Hastie, T., Tibshirani, R., & Friedman, J. (2009). *The Elements of Statistical Learning* (2nd ed.). Springer. · James, G., Witten, D., Hastie, T., Tibshirani, R., & Taylor, J. (2023). *An Introduction to Statistical Learning with Applications in Python*. Springer. |
| Leakage | Kaufman, S., Rosset, S., Perlich, C., & Stitelman, O. (2012). Leakage in data mining. *ACM TKDD*, 6(4). · Kapoor, S., & Narayanan, A. (2023). Leakage and the reproducibility crisis in machine-learning-based science. *Patterns*, 4(9). |
| Networks | Newman, M. (2018). *Networks* (2nd ed.). Oxford University Press. |
| Smoothing and forecasting | Cleveland, W. S. (1979). Robust locally weighted regression and smoothing scatterplots. *JASA*, 74(368). · Hyndman, R. J., & Athanasopoulos, G. (2021). *Forecasting: Principles and Practice* (3rd ed.). OTexts. |
| HPC and streaming | Halko, N., Martinsson, P.-G., & Tropp, J. A. (2011). Finding structure with randomness. *SIAM Review*, 53(2). · Cormode, G., & Yi, K. (2020). *Small Summaries for Big Data*. Cambridge University Press. · Leskovec, J., Rajaraman, A., & Ullman, J. D. (2020). *Mining of Massive Datasets* (3rd ed.). Cambridge University Press. · Vitter, J. S. (1985). Random sampling with a reservoir. *ACM TOMS*, 11(1). · Welford, B. P. (1962). Note on a method for calculating corrected sums of squares and products. *Technometrics*, 4(3). |
| Reproducible notebooks | Rule, A., et al. (2019). Ten simple rules for writing and sharing computational analyses in Jupyter notebooks. *PLoS Computational Biology*, 15(7). |

The TQF3's current recommended texts (Severance 2016; Knaflic 2015) would move to "supplementary" status (C9) **[P]**.

---

**Next step:** after the lecturer reviews §10.1, I will produce the PCA pilot module (backlog B04): lesson plan and measurable objectives; lecture outline with equations, assumptions and worked examples; student notebook and separate instructor solutions; practical exercises, misconception checks and assessment items; verified references; and an execution report.
