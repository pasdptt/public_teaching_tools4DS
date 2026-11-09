# Evidence Audit — 040563107 Tools for Statistical Data Science

**Status:** Draft for lecturer review — audit stage only (no course materials have been rewritten yet).
**Audit date:** 9 November 2026 (Buddhist Era 2569).
**Scope:** Outputs 1–3 of the revamp brief: source inventory, keep/revise/merge/retire/add mapping, and evidence-based issues.
Outputs 4–10 are in [`../blueprint/03-curriculum-blueprint.md`](../blueprint/03-curriculum-blueprint.md).
The full execution log is in [`02-execution-report.md`](02-execution-report.md).

### Evidence labels used throughout

| Label | Meaning |
|---|---|
| **[V]** | **Verified**: I inspected the source directly, executed it, or reproduced the numbers with code that is kept under `tools/audit/`. |
| **[R]** | **Recommendation**: my pedagogical or technical judgement; it needs lecturer review. |
| **[A]** | **Assumption**: not verifiable from the available evidence and stated so it can be checked. |

### Confidentiality choices for this public repository

`pasdptt/public_teaching_tools4DS` is a **public** repository. This audit therefore:

* describes examination papers by structure, topic and points only, without question wording;
* contains no student names, student IDs or student work;
* contains no Google Drive file IDs or links to private files;
* does not commit copies of any data files.

Student submissions, the class roster, grade sheets and a stored Kaggle API credential were found. They were **listed by title only and not opened** (see §1.4).

---

## 1. Source inventory

### 1.1 Where the evidence came from

| Location | Access status | Notes |
|---|---|---|
| GitHub `pasdptt/public_teaching_tools4DS` | Accessible, **empty** (no commits or branches on 9 Nov 2026) **[V]** | The brief's "supplied" materials were not in the repository. |
| Session uploads / attachments | **Empty** **[V]** | — |
| Google Drive (lecturer account, read-only via connector) | **Accessible** **[V]** | Course folder `Tools4statDS` (with `Lecture/` and `2021_2/`), plus the Colab Notebooks root, its `Teaching/` folder, and `ExampleData/`. |
| Dropbox | Accessible; no matching files **[V]** | Searched for the course code. |
| Other lecturer repos (`public_teaching_bdandspark`, `PasdPublicNB`, …) | Searched by code search only **[V]** | They hold course 040563105 (Statistical Analysis for Big Data) material. Only `PCA on spark.ipynb`, which also exists on Drive, is relevant here. |

**Limitation:** I identified the source files by searching Drive for the course code, course title and Thai TQF titles. Course files stored under other names may have been missed **[A]**.

### 1.2 Course specification, assessment and lecture sources

| ID | Source (Drive location) | Type / date | Access | Inspected content | Execution |
|---|---|---|---|---|---|
| S01 | `Tools4statDS/มคอ 3 Tools4DS_2_2563.docx` | TQF3, updated 21 Dec 2563 (2020) | Read in full **[V]** | Credits 3 (2-3-5); 30 lecture, 45 practice and 75 self-study hours; semester 2, year 3; no prerequisites; 16-week plan; assessment 20/35/25/20; two recommended texts. | n/a |
| S01b | `Tools4statDS/มคอ 3 Tools4DS_2_2563.pdf` | PDF of S01 | Listed; not read separately | Assumed to be an export of S01 **[A]**. | n/a |
| S02 | `Tools4statDS/040563107_2020_02_FN.docx` | Final paper, 2/2563 | Read in full **[V]** | 6 questions, 35 points, closed book plus one A4 sheet. | n/a |
| S03 | Colab root `FN_2021_2.ipynb` | Final paper, 2/2564 (online, Colab) | Read and executed **[V]** | The same six questions as S02, plus a +7 bonus. | §1.5 |
| S04 | Colab root `TakehomeMT_2020_2.ipynb` | Take-home midterm 2/2563, containing **instructor working answers** | Read and executed **[V]** | 3 questions (6 + 7 + 7 points) on the Titanic `train.csv`. | §1.5 |
| S05 | `KMUTNB_2021_2_midterm/MT_2021_2.ipynb` | Midterm 2/2564 question paper (7 KB) | Downloaded; **header decoded only** **[V]** | Colab provenance metadata shows it was copied from S04. The body was not decoded, a tooling limitation **[V]**. | not run |
| S06 | `Lecture/Midterm-review` (Slides) | Review deck | Read **[V]** | 3 questions, 20%, one A4 sheet. Topic list includes LDA, LLE and autoencoders. | n/a |
| S07 | `Lecture/Final-review` (Slides, modified Mar 2026) | Review deck | Read **[V]** | 6 questions, 35%, split "30% before / 70% after midterm", 1 question from the project. Topics include smoothing, graphs, imbalance and SMOTE. | n/a |
| S08 | `Tools4statDS/Lecture 0: Introduction to Tools` | Slides | Read **[V]** | **Unfilled template** (placeholder lorem ipsum text). | n/a |
| S09 | `Tools4statDS/General presentation` | Slides | Read **[V]** | The same unfilled template as S08. | n/a |
| S10 | `Lecture/graph.pdf` | Typeset notes, ch. 12, pp. 65–77 | Read (text extraction partly garbled) **[V]** | Discrete-mathematics graph theory: definitions, representations, connectivity, Euler and Hamilton paths, planarity, Dijkstra. Textbook exercises cite page numbers of an **unnamed** textbook. | n/a |
| S11–S15 | `Lecture/20210319.pdf`, `20210409.pdf`, `Note9and10.pdf` (Apr 2022), `Note Feb 28, 2023…pdf`, `Note Mar 7, 2023…pdf` | Handwritten lecture notes | OCR text read; **topics only** **[V]** | All five cover graph theory as in S10. No other course topic appears in them. | n/a |

### 1.3 Notebooks and data

Execution modes are defined in §1.5.

| ID | Notebook (last modified) | Origin noted in notebook | Inspected | Mode A (clean local) | Mode B (Colab-sim, latest packages) | Mode C (Colab-sim, Colab-era pins) |
|---|---|---|---|---|---|---|
| N01 | `Teaching/Review: Python.ipynb` (Dec 2025) | none stated | full **[V]** | 3 / 114 cells error | 3 / 114 | 3 / 114 |
| N02 | `Teaching/Review: Python II.ipynb` (Dec 2025) | none stated | full **[V]** | 0 / 74 | 0 / 74 | 0 / 74 |
| N03 | `Dimensionality Reductions.ipynb` (Dec 2025) | MachineLearningMastery (2 URLs) | full **[V]** | 1 / 19 | 1 / 19 | **0 / 19** |
| N04 | `Teaching/PCAinAction.ipynb` (Dec 2025) | Caltech BE/Bi 103 tutorial, TDS article, mGalarnyk GitHub | full **[V]** | 17 / 53 | 17 / 53 | **0 / 53** |
| N05 | `FeatureExtraction.ipynb` (Jan 2026) | none stated | full **[V]** | 23 / 32 | 4 / 32 | **0 / 32** |
| N06 | `Teaching/smoothing_and_aggregation.ipynb` (Jan 2026) | mlcourse.ai, MachineLearningMastery | full **[V]** | 9 / 28 | 6 / 28 | **0 / 28** |
| N07 | `Teaching/Intro2graphwithPython.ipynb` (Feb 2026) | Analytics Vidhya | full **[V]** | 15 / 29 | 15 / 29 | 15 / 29 (data file unavailable) |
| N08 | `Teaching/Imbalanced.ipynb` (Feb 2026) | none stated (style matches MachineLearningMastery **[A]**) | full **[V]** | 0 / 24 | 0 / 24 | 0 / 24 |
| N09 | `Teaching/SES.ipynb` (Nov 2021) | none stated | full **[V]** | 11 / 15 | 11 / 15 | 11 / 15 |
| N10 | `Teaching/PCA on spark.ipynb` (Oct 2022) | none; belongs to 040563105 | full **[V]** | 13 / 17 | 13 / 17 | 13 / 17 |
| N11 | S03 `FN_2021_2.ipynb` | — | full **[V]** | 1 / 9 | 1 / 9 | 1 / 9 |
| N12 | S04 `TakehomeMT_2020_2.ipynb` | — | full **[V]** | 21 / 27 | 6 / 27 | 6 / 27 |

| ID | Data file | Size | Inspected | Facts established |
|---|---|---|---|---|
| D01 | `ExampleData/AirQualityUCI.csv` | 785,065 B | Profiled **[V]** | 9,471 × 17 raw (two empty trailing columns); 9,357 rows after `dropna`. **366 temperature values and 8,530 rows contain the missing-value code −200.** UCI Air Quality, CC BY 4.0, DOI 10.24432/C59K5F **[V]**. |
| D02 | `ExampleData/Airlines.csv` | 6,822 B | Viewed via Drive text rendering; **bytes not downloaded** | 100 rows × 16 columns matching the R package nycflights13 `flights` table **[V]**. The nycflights13 licence was not verified **[A]**. |
| D03 | `ExampleData/revenue_thlg_2562.xlsx` | 2.8 MB | Profiled **[V]** | One sheet, 7,853 Thai local administrative organisations × 42 columns (revenue categories, FY2562, population, area). **Source and licence are not stated in the file** **[V]**. Not used by any inspected notebook. |
| D04 | `Tools4statDS/train.csv` | 61,194 B | Profiled **[V]** | Kaggle Titanic training set, 891 × 12; `dropna()` keeps 183 rows. OpenML 40945 lists Titanic as "Public" **[V]**. |
| D05 | `Tools4statDS/pima-indians-diabetes.csv` + `.names.txt` | 23 KB | Read **[V]** | 768 × 9, no header, **0 used for missing values** (e.g. blood pressure, insulin). Original owner is NIDDK; no licence stated. Not used by any inspected notebook. |
| D06 | UCI Mushroom (Kaggle copy in N05) | — | Rebuilt from UCI for execution **[V]** | 8,124 × 23. UCI CC BY 4.0, DOI 10.24432/C5959T. The Kaggle copy reports CC0 in N05's own output **[V]**. |
| D07 | MNIST via `fetch_openml('mnist_784')` (N04) | — | Fetched **[V]** | OpenML id 554, licence field "Public", 70,000 × 784 **[V]**. |
| D08 | SES `Cleandata.csv` (N09) | — | **Not found** in any searched location **[V]** | Columns visible in the stored outputs resemble a supermarket-sales transaction table **[A]**. |

### 1.4 Located but deliberately not opened

| Item (title only) | Reason not opened |
|---|---|
| Folders `2021_2/`, `Midterm/`, student files in `KMUTNB_2021_2_midterm/` and `KMUTNB_2021_1_final/`, and the 110 MB final-exam submission archive | Student work; not needed for curriculum design. |
| `Class Roaster`, `StudentList.pdf`, `Class Score`, `Grade/`, and the workbooks `KMUTNB_2020_02_Tools4DS.xlsx`, `KMUTNB_2021_02.xlsx`, `Tool4StatDS_2021_2` | Names indicate student records. I did not open them to check. |
| `kaggle.json` (Colab root) | API credential. **[R]** Rotate this key, because the course design below removes the need for it. |
| `Intro2Spark-*`, `PySpark_Testing & Sampling`, `Modeling_(un)supervised`, `Customer_segmentation`, `Analyzing Online Retail` (+ answer), `Python Example`, `Flask` | Belong to other courses (mainly 040563105). Listed only. |

### 1.5 Execution status (summary)

Full per-cell results, environment versions and the reproduction commands are in [`02-execution-report.md`](02-execution-report.md).

**Execution protocol [V].** Every notebook was run top to bottom in a fresh kernel. Each cell ran even after earlier errors, so that every failure could be recorded. Shell lines (`!apt-get`, `!pip`, `!wget`, `!kaggle`) were **neutralised and logged, not executed**: `!apt-get upgrade` must not run on the audit host, and the Kaggle token was deliberately not used.

| Mode | Environment | Purpose |
|---|---|---|
| A — clean local | Python 3.12.3 with the latest packages (pandas 3.1.1, scikit-learn 1.9.1, Matplotlib 3.11.2, statsmodels 0.15.0, networkx 3.7, imbalanced-learn 0.14.2, TensorFlow 2.21); no `google.colab`, no Drive, no Kaggle token | What a student on an ordinary laptop experiences today. |
| B — Colab-simulated, latest packages | As A, plus a stub `google.colab.drive.mount` and the course's Drive paths mapped to local copies of D01, D04 and D06 | Separates data-access failures from code failures. |
| C — Colab-simulated, Colab-era pins | As B, but with pandas 2.2.3, scikit-learn 1.6.1, Matplotlib 3.10.9, statsmodels 0.14.6, networkx 3.4.2, imbalanced-learn 0.14.0, numpy 2.2.6. These versions match the deprecation warnings recorded in the notebooks' own last Colab outputs. | Separates version drift from genuine defects. |

**Findings [V]:**

1. **No required notebook runs from a clean, documented environment as delivered.** On an ordinary laptop (mode A) every notebook that loads data fails at the data step: Drive paths, the Kaggle API, a missing file, or the blocked or broken MNIST fetch.
2. **Version drift alone breaks several notebooks.** With Drive simulated but the latest packages, mode B fails on:
   * N03: `boxplot(labels=)` was removed in Matplotlib 3.11;
   * N06: `freq='A'` was removed in pandas 3;
   * N04: `fetch_openml` raises a `TypeError` with scikit-learn 1.9.1 and pandas 3.1.1. With pandas 2.3.3 and the same scikit-learn it succeeds in 3.7 s;
   * N05: `TSNE(n_iter=)` was removed.

   All four run cleanly under the Colab-era pins (mode C).
3. **Genuine defects remain in every environment:**
   * N01: curly quotes `‘ ’` turn intended `TypeError` demonstrations into `SyntaxError`s.
   * N07: the data file sits on an unmounted Drive path.
   * N09: its data file does not exist.
   * N10: depends on the unavailable `kora` package and a hard-coded Spark 3.3.0 download URL and Java 8 path.
   * N11: the exam prompt's example call contains curly quotes and is not valid Python.
   * N12: the instructor's answer key **fails in a fresh top-to-bottom run**. One cell displays `finalDf` before it is defined, and `y` is overwritten by a synthetic placeholder dataset, i.e. hidden state. It also uses pandas 1.x-only `groupby().mean()` and `corr()` on text columns.
4. **Reproducibility of numbers.** Under mode C, N04 reproduces its stored outputs exactly (27 of 27 comparable outputs identical). N03, N05, N06 and N08 produce different numbers on every run because no random seeds are set; for example, 12 of 18 comparable outputs differ in N03. Their qualitative conclusions were unchanged in the reruns **[V]**.

---

## 2. Keep / revise / merge / retire / add mapping

All entries are **[R]** recommendations for lecturer review.

| Existing material | Decision | Destination in the blueprint | Rationale (issue IDs refer to §3) |
|---|---|---|---|
| S01 TQF3 description and topic list | **Keep** (scope) / **revise** (weekly plan, CLOs, mapping) | Course spec | The approved scope is preserved. The schedule, outcome mapping and references need revision (A1, C1–C3). |
| S01 assessment weights 20/35/25/20 | **Keep** | §7 | Required by the brief. |
| N01 + N02 Python reviews | **Revise and merge** into one refresher, adding SQL | Week 1–2 labs | Sound statistical content (ddof, nan handling, harmonic and geometric means). Fix the curly quotes (S7) and add the SQL that the TQF promises (C3). |
| N03 Dimensionality Reductions | **Revise** | Week 4 (selection vs extraction) | Keep the correct `Pipeline` + CV RFE pattern (E6). Fix the mislabelled regression importances (M12) and move permutation importance to held-out data. Replace synthetic-only data with one real dataset. |
| N04 PCA in Action | **Revise (pilot module)** | Weeks 5–6 | The strongest notebook and fully reproducible. Add the derivation (M4), use `eigh`/SVD (M3), centre the projections (M2), remove the hard-coded table (M6), and add baselines and CV (E4). |
| N05 Feature Extraction: ICA part | **Revise (replace example)** | Week 7 | ICA on one-hot mushroom data is inappropriate (M8). Use a source-separation example with known ground truth. |
| N05: LDA part | **Revise** | Week 7 | Keep LDA as the supervised contrast to PCA; fit it inside the pipeline (E1). |
| N05: LLE, t-SNE | **Revise** | Week 8 | Use them for visualisation with trustworthiness metrics, not as predictive features (M11). |
| N05: autoencoder | **Revise and bound** | Week 8 (one lab segment) | Correct the loss and output layer (M9); compare against PCA reconstruction error; CPU only. |
| N05: mushroom dataset as the comparison benchmark | **Retire for method comparison** | — | A ceiling effect hides every difference (E5). Keep it only as a "too-easy data" failure-analysis case. |
| N06 smoothing and aggregation | **Revise and split** | Weeks 11–12 | Keep the exponential smoothing and moving-average code. Fix the −200 sentinel (M15), remove random walk as a "smoothing method" (M14), add kernel smoothing/LOESS and parameter selection (M16), and add temporal evaluation (E8). |
| N09 SES | **Merge** into the week 12 lab | Week 12 | Its data file is missing (D08) and the series is not aggregated (M18). Keep the train/test-by-time idea. |
| N07 graph notebook | **Revise substantially** | Weeks 9–10 | Keep the networkx basics and the "tabular data to edge list" idea. Build directed, weighted graphs (M19), fix the parsing bug (S6), and add statistical network analysis (C4). |
| S10 + S11–S15 graph-theory notes | **Merge** into concise reading notes | Week 9 reading | Keep definitions and Dijkstra (examined). Fix the proof (M20) and cite the source textbook. |
| N08 Imbalanced | **Merge** into the evaluation module | Week 3 (resampling as a fitted operation) | Imbalance is not in the TQF scope, but it is the clearest demonstration of resampling inside CV (E6). Fix the metrics (E7). |
| N10 PCA on Spark | **Retire as required** / **optional appendix** | Week 13 (optional) | It belongs to 040563105, needs a fragile installer (S4), and the brief excludes required distributed infrastructure. |
| S08, S09 slide templates | **Retire** | — | Empty. |
| S02/S03 final paper and S04/S05 midterms | **Retire as reusable papers** / **mine for item types** | §7 item bank | They were reused verbatim (A2), are available online, and the keys have defects (M22, S2). The hand-computation items (means, Dijkstra) survive as item types. |
| D01 Air Quality | **Keep** (with sentinel handling) | Weeks 11–12, 14 | Openly licensed, real, and teaches missing-value codes. |
| D02 Airlines sample | **Replace** with the full nycflights13 network (or the OpenFlights route network, licence permitting) | Weeks 9–10 | A 100-row sample gives a star graph with no meaningful structure. |
| D03 Thai local-government revenue | **Add (conditional)** | Week 6 PCA case, project option | A strong, local, high-dimensional case study, *subject to confirming its source and licence* (Q-D1). |
| D04 Titanic, D05 Pima | **Retire** | — | Kaggle account required (D04); unclear licence and sensitive Indigenous health data (D05). |
| D06 Mushroom, D07 MNIST | **Keep** (download from UCI/OpenML with checksums, not Kaggle) | Weeks 5–8 | Open, stable sources. |
| — (absent) | **Add** | Week 3 | Evaluation and leakage module (C5). |
| — (absent) | **Add** | Week 13 | High-performance computing on a laptop (C1). |
| — (absent) | **Add** | Week 14 | Streaming algorithms (C2). |
| — (absent) | **Add** | Weeks 1, 3, labs | Responsible AI-assisted coding exercises (§7.5). |
| — (absent) | **Add** | Week 8 | Contemporary representation example: precomputed embeddings, CPU only. |
| — (absent) | **Add** | Throughout | Project brief, milestone specifications, rubrics, instructor solutions (A5). |

---

## 3. Issues supported by inspected evidence

Severity: **Critical** = invalidates a conclusion students are taught to trust; **High** = wrong or missing core content; **Medium** = misleading or fragile; **Low** = polish.
Cell numbers are 0-based indices in the original notebooks.

### 3.1 Mathematical and statistical issues

| ID | Severity | Evidence [V] | Issue | Recommendation [R] |
|---|---|---|---|---|
| M1 | Medium | N04 cells 1, 17–18 | Step 1 says "standardize" but the code only centres. The choice between covariance-matrix and correlation-matrix PCA is never discussed. | Teach both explicitly; tie the choice to measurement units. |
| M2 | Medium | N04 cell 26; check C4 | The 1-D projection multiplies **uncentred** data by the eigenvector. The scores are shifted by a constant (mean 3.93 instead of 0) and no longer match the definition of principal-component scores. | Use centred data. |
| M3 | Medium | N04 cell 21; check C4 | `np.linalg.eig` is used on a symmetric covariance matrix. It does not guarantee ordering, and in the audit environment it returned a **complex** dtype. | Use `np.linalg.eigh` or the SVD of the centred data, and sort explicitly. |
| M4 | High | N04 cell 19: "We won't cover the math behind this procedure" | There is no derivation of PCA: variance maximisation, the Rayleigh quotient, the equivalence with minimum reconstruction error, or the SVD link. That is not adequate rigour for third-year statistics students. | Pilot module (§9, P0). |
| M5 | Low | N04 cell 22 | The `quiver` arrows pass rows of `eig_vecs`. The drawing is correct only by the symmetry of a 2×2 rotation matrix. | Plot columns explicitly. |
| M6 | Medium | N04 cell 94 (never executed) | A hand-typed results table (variance retained, components, seconds, accuracy) appears to have been copied from the source tutorial. It contradicts the notebook's own result: 330 components versus the computed **327** (rerun confirmed 327 and 0.9201) **[V]**. | Generate every reported number with code. |
| M7 | Low | N04 eigenvalue 3.65937 (UCI file) vs 3.66124 (`sklearn.datasets.load_iris`), check C4 | The two Iris sources differ numerically **[V]**. scikit-learn documents corrections to the UCI file **[A — citation to be verified in the pilot]**. | Use this as a provenance teaching point. |
| M8 | High | N05 cells 16, 20 | ICA is introduced as "similar to PCA… a very subtle difference" and then applied to standardised **one-hot** categorical data. ICA's model is a linear mixture of independent, non-Gaussian, continuous sources. The notebook covers no identifiability conditions (at most one Gaussian source; sign, scale and order indeterminacy), no whitening and no ground truth. | Cocktail-party or signal-separation example with known sources; a failure case with Gaussian sources. |
| M9 | High | N05 cell 45 | The autoencoder pairs a **softmax** output with **binary cross-entropy** on standardised inputs that take negative values. Reconstructions are forced onto the probability simplex. In the original run the downstream accuracy fell to 0.87 and this was not diagnosed. | Linear output with MSE (or sigmoid with BCE on 0/1 inputs); compare against PCA reconstruction error. |
| M10 | Medium | N05 cells 24–25 | There is no Fisher criterion and no generalised eigenproblem, and the bound of at most K−1 components is not explained. LDA's shared-covariance assumption is not checked; on one-hot data the within-class covariance is singular. | Derive LDA; contrast it with PCA on the same data. |
| M11 | High | N05 cells 38–41 | t-SNE coordinates are used as **predictive features** for a random forest. t-SNE has no out-of-sample transform, and between-cluster distances are not interpretable. | Use t-SNE for visualisation only, with trustworthiness or neighbourhood-preservation metrics. |
| M12 | Medium | N03 cells 38, 42; check C7 | The "regression" decision-tree and random-forest importances are fitted on the **previous classification data** (the `make_regression` line is commented out; the target takes only 0/1). Permutation importance is computed on **training** data (cells 46, 48). | Correct the data; compute permutation importance on held-out data. |
| M13 | Medium | N03 cell 36; N12 cell 23 | Coefficients are presented as "importance" with no discussion of scaling or collinearity (the data has `n_redundant=5`). | Discuss standardised coefficients, collinearity and instability. |
| M14 | High | N06 cells 5, 37–48 | Smoothing is defined as "eliminating outliers". Random walk is taught as a "smoothing method", and its equation is given as the regression form y(t) = B0 + B1·X(t−1) + e(t). | Present random walk as a stochastic process and naive forecasting baseline, not a smoother. |
| M15 | High | N06 cells 28–34; check C2 | The UCI missing-value code −200 is treated as a temperature. **The exponential moving average taught reaches −195 °C; the maximum distortion is 205.8 °C.** | Recode sentinels before smoothing; make this a failure-analysis exercise. |
| M16 | Medium | N06 | Trailing and centred windows are not distinguished; no smoothing parameter is selected by a criterion; kernel smoothing and LOESS are absent. | Add bias–variance analysis of the bandwidth and parameter selection by temporal validation. |
| M17 | Low | N06 cell 48 | `x = w = np.random.normal(...)` aliases two arrays, and `x[t-1]` at t=0 wraps to the last element. The output is correct only by coincidence, and there is no seed. | Rewrite. |
| M18 | High | N09 cells 3–5 | SES is fitted to **transaction-level** rows with several per day, not to a regular time series. α is fixed at 0.6 rather than estimated, and there is no naive baseline. | Aggregate to a regular frequency, estimate α, compare with naive. |
| M19 | High | N07 cells 38–48 | Directed, repeated flights are stored in an **undirected simple** `nx.Graph`; each edge keeps only the last row's attributes. "Shortest" routes such as JAX→JFK→SEA→EWR→DFW are artefacts of this construction. | Build a `DiGraph` or `MultiDiGraph` with aggregated weights; discuss what a path means. |
| M20 | Medium | S10, theorem on in-degree and out-degree sums | The result is "proved" by contradiction via a pigeonhole argument. The standard proof is a direct count: each directed edge adds exactly one to each sum. Dijkstra's pseudocode uses 32767 as infinity. | Correct the proof; use ∞. |
| M21 | High | N12 cells 22, 28–35; check C3 | `df.dropna()` keeps **183 of 891** rows, because of `Cabin`, with no discussion. The reported accuracy of 0.778 rests on **n = 27** test rows (95% Wilson interval 0.59–0.89) against a **majority-class baseline of 0.672**. 90% and 80% PCA give identical accuracy, so the comparison is uninformative. | Assessment keys must model valid inference (A4). |

### 3.2 Evaluation and leakage

| ID | Severity | Evidence [V] | Issue | Recommendation [R] |
|---|---|---|---|---|
| E1 | **Critical** (pattern) | N05 cells 25–29; checks C5, C6b | **Supervised LDA is fitted on all rows before the train/test split.** On the mushroom data the reported test accuracy is 1.000 whether or not the leak is present (C6b), because the data are separable. On pure-noise labels, the same pattern reports **0.97** accuracy where the true value is 0.5; inside a CV pipeline it gives **0.51** (C5). | Put every fitted transformation inside `Pipeline` and cross-validation. |
| E2 | Medium | N05 cell 12; N12 cell 22 | `StandardScaler` is fitted on all rows before the split. | As E1. |
| E3 | Medium | N05 cells 20, 33, 38, 45 | ICA, LLE, t-SNE and the autoencoder are fitted on all rows, including the test rows (transductive leakage). | Fit on training folds; state when transductive use is acceptable (pure visualisation). |
| E4 | High | N04 MNIST; N05; N12 | Every comparison uses a single split, with no baseline and no uncertainty. | Require a baseline and an uncertainty estimate in every lab. |
| E5 | High | N05; check C6 | Ceiling effect on mushroom: a majority classifier scores 0.518, but **`odor` alone scores 0.985** and the raw random forest scores 1.000. Every dimensionality-reduction method looks perfect. | Choose data where methods can be distinguished. |
| E6 | — (strength) | N03 cells 17–23, 53; N04 cells 72–82; N08 cells 19–45 | **Correct practice already present:** RFE inside `Pipeline` with repeated stratified CV; `SelectFromModel` fitted on the training split; scaler and PCA fitted on training data only; `imblearn` resampling inside the CV pipeline. | **Keep and generalise** these patterns. |
| E7 | Medium | N08 cells 19, 23, 28, 45 | Macro-F1 (cell 19) is compared with micro-F1 (cells 23, 28); for binary problems micro-F1 equals accuracy. The SMOTE `k` is chosen on the same CV used for reporting. There is no PR-AUC, calibration or class-weight baseline. | Use consistent metrics, nested CV and a cost-sensitive baseline. |
| E8 | Medium | N06, N09 | No forecast evaluation (rolling origin); leakage from centred windows or full-series statistics is never discussed. | Week 12. |
| E9 | Medium | N07 | No graph-specific evaluation (edge-split link prediction, temporal edges). | Week 10. |
| E10 | Medium | N03, N05, N06, N08 (§1.5 item 4) | No random seeds, so numbers differ on every run. | Seed everything and report run-to-run variability. |

### 3.3 Pedagogical issues

| ID | Severity | Evidence [V] | Issue | Recommendation [R] |
|---|---|---|---|---|
| P1 | High | All notebooks | No learning objectives. Few student tasks: N04 cell 46 is the only explicit analytical question. No failure-analysis or interpretation prompts. | Every lab gets objectives, tasks, a "what can go wrong" section and an interpretation write-up. |
| P2 | High (for publication) | N03, N04, N06, N07, N08 | Large passages appear to be reproduced from blogs and tutorials, with source URLs but no licence statements. The licensing of such reuse in a **public** repository is unverified **[A]**. | Rewrite in original wording; cite sources as references. |
| P3 | High | S08, S09; Drive search | No lecture slides exist for any core topic (the two decks are unfilled templates). Lecture content for most weeks is undocumented. | Produce lecture outlines (backlog P0/P1). |
| P4 | High | S10–S15 (three academic years) | Network analysis is taught as discrete-mathematics graph theory. Statistical network analysis (degree distributions, centrality, communities, null models) is absent. | Weeks 9–10. |
| P5 | Medium | S02–S05 (Thai instructions); notebooks (English) | Language practice is mixed and undocumented. | Decision Q-L1. |
| P6 | Medium | N01 cells 26, 61 | Curly quotes defeat the intended demonstrations of strong typing (`1 + '1'`) and tuple immutability: students see a `SyntaxError` instead of the intended `TypeError`. | Fix. |
| P7 | Low | S06 vs S07 | LDA, LLE and autoencoders are listed as midterm topics in one review deck and as post-midterm topics in the other. | Align the schedule with the reviews. |

### 3.4 Software and reproducibility issues

| ID | Severity | Evidence [V] | Issue |
|---|---|---|---|
| S1 | High | §1.5 item 2 | No pinned environment exists. Four notebooks are broken by package releases since their last run. |
| S2 | High | N12 (cells 25–26 fail top to bottom); execution counts out of order in N03, N09, N12 | Hidden notebook state: outputs, including an answer key, were produced by out-of-order execution. |
| S3 | High | N05, N12 (Kaggle API with a token on Drive); N06, N07 (unmounted Drive paths); N09 (missing file) | Data access depends on personal credentials, the lecturer's Drive layout, or a file that no longer exists. |
| S4 | Medium | N05 cells 1–2 (`!apt-get update/upgrade`); N10 (Spark tarball URL, `kora`, Java 8 path) | System-level installers inside notebooks are slow, fragile, and unnecessary for the course. |
| S5 | Low | N04, N12 (unused `numba`, `bokeh`, `scipy.special`); N06 (`tqdm_notebook`, `np.sum` in `rolling.aggregate`) | Unused heavy imports and deprecated APIs. |
| S6 | Medium | N07 cell 37; check C1 | Under pandas ≥ 2, `str.replace` no longer treats the pattern as a regex by default. The time conversion **silently produces `1630:30:00` instead of `16:30:00`**. Invalid `\d` escapes also raise `SyntaxWarning`. |
| S7 | Low | N11 cell 14; N01 cells 26, 61 | Code in an exam paper and in the review notebook is not valid Python (typographic quotes). |
| S8 | — (strength) | N04 under mode C | A reproducible reference exists: 27 of 27 outputs are identical. It is the natural pilot. |

### 3.5 Assessment issues

| ID | Severity | Evidence [V] | Issue |
|---|---|---|---|
| A1 | Medium | S01 §5.2 | Practical work (20%) maps to **no** TQF learning-outcome code. Exams are scheduled "weeks 9, 17, 18" while the teaching plan places the final in week 16. |
| A2 | High | S02 vs S03 | The 2/2563 final paper was **reused verbatim** in 2/2564. The 2/2564 version adds a +7 bonus, so the maximum is 42 points against a 35% weight; the scaling is undocumented. |
| A3 | Low | S02 header | The paper is labelled semester 1/2563, but the course runs in semester 2 and the file name says `2020_02`. |
| A4 | High | S03, S04 (internet allowed; similarity checking is the only control) | Under current generative AI, unsupervised open-internet Colab exams cannot evidence individual achievement. |
| A5 | High | Drive search | No project brief, milestone specification, rubric or answer key with marking scheme was found. Only the S04 working notebook exists, and it does not run (S2). |
| A6 | Medium | S02 | The exam items cover means, PCA coding, a feature-extraction essay, a smoothing essay, hand Dijkstra and project reflection. **None** covers ICA computation, high-performance computing, streaming, or evaluation and leakage. |
| A7 | Low | S02 vs S07 | The 2/2563 paper puts 14 of 35 points (40%) on pre-midterm items, against the review deck's "30% before midterm". The deck was edited in March 2026, possibly for a later paper **[A]**. |

### 3.6 Coverage against the approved TQF scope

| ID | TQF topic (S01) | Material found [V] | Gap |
|---|---|---|---|
| C1 | Application of high-performance computing | **None** for this course (N10 belongs to 040563105) | **Critical gap.** No week in S01 is allocated to it. |
| C2 | Streaming algorithms (S01 week 14) | **None** | **Critical gap.** |
| C3 | "Revisit: Python & SQL" (S01 weeks 2–3) | Python only (N01, N02); no SQL | Gap. |
| C4 | Network analysis (S01 weeks 11–12) | Discrete graph theory (S10–S15), a basic networkx demo (N07) | Statistical content missing. |
| C5 | Evaluation methodology (implied by "analysis of large data sets"; required by the brief) | Scattered (N03, N08) | No dedicated treatment of leakage or baselines. |
| C6 | Independent component analysis (S01 week 6) | Three cells in N05 | Superficial (M8). |
| C7 | Smoothing and aggregation (S01 week 13) | N06, N09 | Partial (M14–M18). |
| C8 | Dimension reduction, PCA, feature extraction (S01 weeks 4–7, 10) | N03, N04, N05 | Present; needs the corrections above. |
| C9 | References (S01 §6) | *Python for Everybody* (Severance 2016); *Storytelling with Data* (Knaflic 2015) | Neither covers the mathematical core of the course. |

### 3.7 Data, licensing and intellectual-property issues

| ID | Evidence [V] | Issue | Recommendation [R] |
|---|---|---|---|
| D-1 | D04, N05, N12 | Kaggle-hosted data needs a personal account and API token; Titanic is competition data. | Use OpenML or UCI sources with checksums. |
| D-2 | D05 | Pima: no licence stated, sensitive Indigenous health data, zeros used as missing values. | Retire. |
| D-3 | D03 | Thai local-government revenue data: source and licence not stated in the file. | Confirm before publishing (Q-D1). |
| D-4 | D02 | Airlines sample: probable nycflights13 origin; licence not verified. | Verify, or use another open network dataset. |
| D-5 | P2 | Reused blog text and code in public teaching material. | Rewrite and cite. |
| D-6 | `kaggle.json` | A stored API credential. | Rotate the key and remove the file. |
